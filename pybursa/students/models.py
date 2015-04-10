from django.db import models
from courses.models import Courses

class Students(models.Model):
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    # second_name = models.CharField(max_length=150)
    birdth_date = models.DateField()
    adress = models.CharField(max_length=300)
    email = models.EmailField()
    skype = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    # prakt_count = models.DecimalField(max_digits=2, decimal_places=0)
    # kontr_count = models.DecimalField(max_digits=2, decimal_places=0)
    # average_score = models.DecimalField(max_digits=2, decimal_places=0)
    # rank = models.DecimalField(max_digits=2, decimal_places=0)
    course = models.ManyToManyField(Courses)
    
    def __unicode__(self):
        return self.first_name
