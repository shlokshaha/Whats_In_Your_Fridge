from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
