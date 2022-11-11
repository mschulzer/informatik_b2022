from django.db import models
from django.forms import ModelForm
import uuid

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    email = models.EmailField()
    status = models.CharField(max_length = 50)


class StudentAdd(ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'email', 'status']
