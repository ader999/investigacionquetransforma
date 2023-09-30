# Generated by Django 4.2.3 on 2023-09-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('Educacion', 'Educación, Humanidades y Artes'), ('Ciencia_Sociales', 'Ciencias Sociales, Económicas, Administrativas y Derecho')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]
