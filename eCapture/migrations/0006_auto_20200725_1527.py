# Generated by Django 2.2.7 on 2020-07-25 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCapture', '0005_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtype',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]