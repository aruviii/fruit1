# Generated by Django 3.2.5 on 2021-07-29 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_products_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pic',
            field=models.SlugField(),
        ),
    ]