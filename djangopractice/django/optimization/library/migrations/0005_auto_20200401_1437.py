# Generated by Django 3.0 on 2020-04-01 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20200401_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='vegetarian',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('best_pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='championed_by', to='library.Pizza')),
                ('pizzas', models.ManyToManyField(related_name='restaurants', to='library.Pizza')),
            ],
        ),
    ]
