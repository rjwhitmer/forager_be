# Generated by Django 3.0.9 on 2020-08-18 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forager', '0006_delete_userplants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
