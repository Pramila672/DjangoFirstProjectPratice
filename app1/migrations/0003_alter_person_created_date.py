# Generated by Django 5.0.4 on 2024-04-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_person_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
