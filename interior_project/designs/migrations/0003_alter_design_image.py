# Generated by Django 3.2.9 on 2023-12-04 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0002_auto_20231204_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='design_images/'),
        ),
    ]
