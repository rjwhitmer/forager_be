# Generated by Django 3.0.9 on 2020-08-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forager', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
