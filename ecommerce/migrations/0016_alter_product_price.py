# Generated by Django 3.2.5 on 2021-07-31 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_auto_20210731_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(max_length=8, null=True),
        ),
    ]
