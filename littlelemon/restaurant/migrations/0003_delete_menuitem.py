# Generated by Django 4.2.6 on 2023-10-26 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menuitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
