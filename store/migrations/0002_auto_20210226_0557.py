# Generated by Django 3.0.4 on 2021-02-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]