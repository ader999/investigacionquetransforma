# Generated by Django 4.2.3 on 2023-09-06 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image_alter_post_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_de_publicacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]