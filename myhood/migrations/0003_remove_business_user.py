# Generated by Django 3.2.5 on 2021-07-24 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0002_auto_20210724_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
    ]
