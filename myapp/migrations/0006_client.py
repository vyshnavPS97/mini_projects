# Generated by Django 3.2.8 on 2021-10-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0005_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_email', models.EmailField(max_length=20)),
                ('cli_name', models.CharField(max_length=20)),
                ('cli_contact', models.CharField(max_length=20)),
                ('cli_password', models.CharField(max_length=20)),
            ],
        ),
    ]
