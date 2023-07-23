from django.db import models
import datetime
class User(models.Model):
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    mail = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=25, blank=False)
    subscr_type = models.CharField(max_length=25, blank=False)
    birthday = models.DateField(blank=False)
    drive_licence_id = models.CharField(max_length=25, blank=False)

class Admin(User):
    age = models.IntegerField(default=15)

