# Generated by Django 2.2.4 on 2019-09-02 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190902_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
    ]