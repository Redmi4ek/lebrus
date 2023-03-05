from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=75, null=False)
    surname = models.CharField(max_length=75, null=False)
    year_of_study = models.IntegerField(null=False)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)
# Create your models here.
