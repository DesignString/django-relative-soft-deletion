
from django.core.exceptions import FieldDoesNotExist
from django.db import models
from django.db.models import Q
from django.db.models.query import QuerySet
from django.utils import timezone


class SoftDeletionQuerySet(QuerySet):

    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


def _get_kwargs_from_args(args):
    keywords = []
    if len(args):
        for arg in args:
            if isinstance(arg, tuple):
                keywords = [arg[0]]
            elif isinstance(arg, Q):
                my_path, my_args, my_kwargs = arg.deconstruct()
                if len(my_args):
                    keywords.extend(_get_kwargs_from_args(my_args))
                elif my_kwargs:
                    keywords.extend(my_kwargs.keys())
    return keywords


def _get_delete_filters_kwargs(model, *args, **kwargs):
    from django.db.models import ForeignKey
    filter_kwargs = {}
    kwargs_all = list(_get_kwargs_from_args(args)) + list(kwargs.keys())
    filter_keys = list(filter(lambda x: '__' in x, kwargs_all))
    for filter_key in filter_keys:
        current_model = model
        filter_lookups = filter_key.split('__')
        add_lookup = ''
        for lookup in filter_lookups:
            try:
                if current_model:
                    field = current_model._meta.get_field(lookup)
                    if field and hasattr(field, 'related_model') and not (isinstance(field, ForeignKey) and '_id' in lookup):
                        current_model = field.related_model
                        add_lookup = '__'.join([add_lookup, lookup]) if add_lookup else lookup
                        if current_model and has_field(current_model, 'deleted_at'):
                            filter_kwargs.update({'__'.join([add_lookup, 'deleted_at']): None})
                else:
                    break
            except FieldDoesNotExist:
                continue
    return filter_kwargs


def has_field(cls, field):
    try:
        cls._meta.get_field(field)
        return True
    except FieldDoesNotExist:
        return False


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only and has_field(self.model, 'deleted_at'):
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def exclude(self, *args, **kwargs):
        if self.alive_only and has_field(self.model, 'deleted_at'):
            delete_filters_kwargs = _get_delete_filters_kwargs(self.model, *args, **kwargs)
            return super(SoftDeletionManager, self).exclude(*args, **kwargs).filter(**delete_filters_kwargs)
        return super(SoftDeletionManager, self).exclude(*args, **kwargs)

    def filter(self, *args, **kwargs):
        if self.alive_only and has_field(self.model, 'deleted_at'):
            delete_filters_kwargs = _get_delete_filters_kwargs(self.model, *args, **kwargs)
            kwargs.update(delete_filters_kwargs)
            return super(SoftDeletionManager, self).filter(*args, **kwargs)
        return super(SoftDeletionManager, self).filter(*args, **kwargs)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()