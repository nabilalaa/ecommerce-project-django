# Generated by Django 3.2.5 on 2021-08-03 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_total_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='t',
            field=models.FloatField(null=True),
        ),
    ]