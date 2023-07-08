from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    status_choices = [
        ("متوفر", "متوفر"),
        ("مستعار", "مستعار"),
        ("مباع", "مباع")
    ]

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, null=True, blank=True)
    img = models.ImageField(upload_to="images", null=True, blank=True)
    author_img = models.ImageField(upload_to="images", null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_choices, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title