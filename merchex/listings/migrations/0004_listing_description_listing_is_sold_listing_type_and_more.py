# Generated by Django 4.0.1 on 2022-01-29 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_brand_active_brand_biography_brand_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('Records', 'Records'), ('Clothing', 'Clothing'), ('Poster', 'Poster'), ('Miscellaneous', 'Miscellaneous')], default='Record', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900)]),
        ),
    ]
