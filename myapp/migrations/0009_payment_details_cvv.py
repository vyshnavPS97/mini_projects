# Generated by Django 3.2.8 on 2021-10-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_payment_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_details',
            name='cvv',
            field=models.CharField(default=121, max_length=3),
            preserve_default=False,
        ),
    ]