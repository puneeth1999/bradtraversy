# Generated by Django 3.1.6 on 2021-02-09 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='listing_id',
        ),
    ]
