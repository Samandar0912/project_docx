from django.db import models
from users.models import CustomUser
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=150)
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categorys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

class CategoryScience(models.Model):
    name = models.CharField( max_length=100)
    class Meta:
        verbose_name = "category Science"
        verbose_name_plural = "category Science"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

class Product(models.Model):
    Author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    categoryScience = models.ForeignKey("CategoryScience", on_delete=models.CASCADE)
    name = models.CharField( max_length=150, verbose_name='Mavzu')
    price = models.CharField( max_length=50, verbose_name='narxi')
    created = models.DateTimeField( auto_now_add=False, verbose_name='yuklangan sana')
    file = models.FileField( upload_to='Files/' )
    

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Article_detail", kwargs={"pk": self.pk})