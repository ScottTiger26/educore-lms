from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICE = (
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    )   

    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default="student")
    

    def __str__(self):
        return self.username
