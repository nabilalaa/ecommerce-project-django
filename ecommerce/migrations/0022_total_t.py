# Generated by Django 3.2.5 on 2021-08-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_auto_20210802_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='total',
            name='t',
            field=models.FloatField(default=0, null=True),
        ),
    ]