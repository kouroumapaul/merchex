# Generated by Django 4.0.1 on 2022-01-29 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_listing_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='year_formed',
            field=models.IntegerField(),
        ),
    ]