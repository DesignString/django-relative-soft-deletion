==================
Django Relative SoftDeletion
==================

Django Relative SoftDeletion is a custom made Django plugin which allows you to Soft Delete database values, which means while deleting any data, it will flag the data as deleted but will not remove the data completely from database. And at the time of fetching data from database, you will automatically get filtered result (excluding deleted values).

Another important implementation in this plugin is that it will also filter deleted values while filtering on reverse relationships. It means while filtering (reverse lookups also) in Foreign fields, it will not consider the deleted data as those values will already be excluded.