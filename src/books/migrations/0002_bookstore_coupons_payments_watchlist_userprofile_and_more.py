# Generated by Django 4.2 on 2023-04-18 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('social_media_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('coupon_code', models.CharField(max_length=40)),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('card_number', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('cvv', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('zip_code', models.IntegerField()),
                ('country', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('watchlist', models.ManyToManyField(to='books.watchlist')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.payments')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('books', models.ManyToManyField(to='books.books')),
            ],
        ),
    ]
