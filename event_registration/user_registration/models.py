from django.db import models
from django.forms import ModelForm

class User(models.Model):
    soeid = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    status = models.CharField(max_length=10)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, to_field='short_name')
    registered_date = models.DateTimeField()

class Role(models.Model):
    short_name = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=100)

class Config(models.Model):
    event_name = models.CharField(max_length=200)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    registration_cap = models.IntegerField()

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['soeid', 'name', 'role', 'email']