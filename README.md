==================
# Django Relative SoftDeletion
==================

Django Relative SoftDeletion is a custom made Django plugin which allows you to Soft Delete database values, which means while deleting any data, it will flag the data as deleted but will not remove the data completely from database. And at the time of fetching data from database, you will automatically get filtered result (excluding deleted values).

Another important implementation in this plugin is that it will also filter deleted values while filtering on reverse relationships. It means while filtering (reverse lookups also) in Foreign fields, it will not consider the deleted data as those values will already be excluded.


### Installing

Activate your environment and install the plugin using the command given below:

```
pip install git+https://github.com/DesignString/django-relative-soft-deletion.git
```


## Usage

Import the `SoftDeletionModel` from `django_soft_deletion.models` and inherit in your Model classes:

For example, 
```
from django_soft_deletion.models import SoftDeletionModel

class Employee(SoftDeletionModel):
	pass
```

## Functions

`Model.objects()...`: Return result excluding deleted values

`Model.all_objects()...`: Return result including deleted values

`delete()`: Soft delete the item

`hard_delete()`: Permanent delete the item
