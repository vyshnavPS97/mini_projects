# Generated by Django 3.2.8 on 2021-10-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_payment_details_cvv'),
    ]

    operations = [
        migrations.CreateModel(
            name='juice',
            fields=[
                ('item_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('price', models.IntegerField(max_length=20)),
            ],
        ),
    ]