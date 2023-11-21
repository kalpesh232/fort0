from django.db import models

# Create your models here.


class Users(models.Model):
    UserName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=25)
    Flag = models.CharField(max_length=10)
    Password = models.CharField(max_length=50, default='123')  # Add this line

    def __str__(self) -> str:
        return self.UserName

