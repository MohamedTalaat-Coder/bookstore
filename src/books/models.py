from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    genre = models.CharField(max_length=25)
    price = models.IntegerField()
    rating = models.IntegerField()
    reviews = models.TextField()
    buy_option = (
    ("1", "Cash"),
    ("2", "Bank Card"),
    ("3", "PayPal")
    )
    date = models.DateField(auto_created=True)
