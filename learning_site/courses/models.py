from django.db import models

# Create your models here.


class Course(models.Model):
    # auto_now_add=True sets the default of this field to now upon instantiation
    # this is why we needed to set our timezone in settings.py
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title