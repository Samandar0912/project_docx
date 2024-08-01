from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.username
    
class Saved(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser,  on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return 'coment of ' + str(self.author.username)