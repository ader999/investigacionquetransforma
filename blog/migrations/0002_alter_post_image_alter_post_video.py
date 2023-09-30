# Generated by Django 4.2.3 on 2023-09-04 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
