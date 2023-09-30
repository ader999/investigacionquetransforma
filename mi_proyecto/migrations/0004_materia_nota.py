# Generated by Django 4.2.3 on 2023-09-02 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mi_proyecto', '0003_estudiante_carnet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estudiante_carnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_proyecto.estudiante')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_proyecto.materia')),
            ],
        ),
    ]