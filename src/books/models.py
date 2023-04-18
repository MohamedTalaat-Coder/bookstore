from django.db import models
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    genre = models.CharField(max_length=25)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Reviews(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    date = models.DateField(auto_now_add=True)


class Payments(models.Model):
    card_number = models.IntegerField()
    expiry_date = models.DateField()
    cvv = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class BookStore(models.Model):
    store_name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    phone_number = models.IntegerField()
    email = models.EmailField()
    social_media_link = models.URLField()
    books = models.ManyToManyField(Books)


class Orders(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payments, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=40)
    watchlist = models.ManyToManyField(Watchlist)
    date = models.DateField(auto_now_add=True)


class Coupons(models.Model):
    coupon_code = models.CharField(max_length=40)
    discount = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Discount(models.Model):
    code = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    books = models.ManyToManyField('Books')
