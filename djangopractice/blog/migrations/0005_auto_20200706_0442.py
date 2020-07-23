# Generated by Django 2.0.2 on 2020-07-03 11:41

from django.db import migrations


def load_data(apps, schema_editor):
    Blog = apps.get_model('blog', 'Blog')
    Blog.objects.create(
        name='blog2',
        tagline='tagline2'
    )
    Blog.objects.create(
        name='blog3',
        tagline='tagline3'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_entrydetails'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]