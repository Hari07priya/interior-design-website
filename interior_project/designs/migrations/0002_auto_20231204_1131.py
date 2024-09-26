# Generated by Django 3.2.9 on 2023-12-04 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='design',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='design',
            name='image',
            field=models.ImageField(upload_to='static/design_images/'),
        ),
        migrations.AlterField(
            model_name='design',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designs.design')),
            ],
        ),
    ]