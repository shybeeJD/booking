# Generated by Django 3.2.8 on 2021-11-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='typeId',
            field=models.IntegerField(max_length=100),
        ),
    ]
