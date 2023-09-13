from django.db import models

# Create your models here.

# model for work experince pip
class WorkExperience(models.Model):
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    loaction=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    description=models.TextField()

    def __str__(self):
        return self.title