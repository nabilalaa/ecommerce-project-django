# Generated by Django 3.2.5 on 2021-07-30 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_alter_register_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.register'),
        ),
    ]
