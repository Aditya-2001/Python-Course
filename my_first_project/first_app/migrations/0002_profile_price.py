# Generated by Django 3.0.8 on 2020-07-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Price',
            field=models.FloatField(default=1000),
            preserve_default=False,
        ),
    ]
