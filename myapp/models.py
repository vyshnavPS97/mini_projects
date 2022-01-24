from django.db import models

# Create your models here.
class client(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_email = models.EmailField(max_length=20)
    cli_name = models.CharField(max_length=20)
    cli_contact = models.CharField(max_length=20)
    cli_password = models.CharField(max_length=20)

class place_order(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=20)
    item_count = models.CharField(max_length=20)
    item_location = models.CharField(max_length=20)
    item_contact = models.CharField(max_length=20)

class payment_details(models.Model):
    pay_id = models.AutoField(primary_key=True)
    card_number = models.CharField(max_length=30)
    expiry_month = models.CharField(max_length=10)
    expiry_year = models.CharField(max_length=10)
    cvv = models.CharField(max_length=3)

class juice(models.Model):
    item_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    price = models.IntegerField(max_length=20)
