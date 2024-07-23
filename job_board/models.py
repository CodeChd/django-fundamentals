from django.db import models

# Create your models here.
class JobPosting(models.Model):
    #  by default models already have id that starts at 1 and autoincrement
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

    # model manager - objects from python we can use to interact with the database, basically its ORM methods

