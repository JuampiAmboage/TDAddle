# Generated by Django 5.1.3 on 2024-11-17 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algorithms', '0002_complexity_name_alter_algorithm_type_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DailyRegistration',
            new_name='AlgorithmOfTheDay',
        ),
    ]
