# Generated by Django 3.0 on 2020-05-04 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sagar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
    ]