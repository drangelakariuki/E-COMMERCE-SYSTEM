# Generated by Django 4.0.3 on 2022-03-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kui', '0002_rename_product_type_collection_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(blank=True, to='kui.promotion'),
        ),
    ]
