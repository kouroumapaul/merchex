# Generated by Django 4.0.1 on 2022-01-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_listing_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
