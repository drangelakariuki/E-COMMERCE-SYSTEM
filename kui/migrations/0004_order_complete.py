# Generated by Django 4.0.3 on 2022-03-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kui', '0003_alter_product_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
