# Generated by Django 3.2.5 on 2021-07-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]