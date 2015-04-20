from django.db import models
from django.contrib.auth.models import User

class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255)

    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def __unicode__(self):
        return self.full_name()

    class Meta:
            verbose_name_plural = "coaches"
