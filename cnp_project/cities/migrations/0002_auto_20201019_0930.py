# Generated by Django 3.1.2 on 2020-10-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='population',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
