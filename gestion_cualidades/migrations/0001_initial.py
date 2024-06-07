# Generated by Django 5.0.6 on 2024-06-07 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_miembros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cualidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Distribucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RelacionCualidadEntrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cualidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_cualidades.cualidades')),
                ('entrenador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_miembros.entrenador')),
            ],
        ),
        migrations.AddField(
            model_name='cualidades',
            name='entrenador',
            field=models.ManyToManyField(through='gestion_cualidades.RelacionCualidadEntrenador', to='gestion_miembros.entrenador'),
        ),
        migrations.CreateModel(
            name='RelacionDistribucionCualidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cualidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_cualidades.cualidades')),
                ('distribucion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_cualidades.distribucion')),
            ],
        ),
        migrations.AddField(
            model_name='distribucion',
            name='cualidad',
            field=models.ManyToManyField(through='gestion_cualidades.RelacionDistribucionCualidades', to='gestion_cualidades.cualidades'),
        ),
        migrations.CreateModel(
            name='RelacionGrupoEtarioCualidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cualidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_cualidades.cualidades')),
                ('grupo_etario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion_miembros.grupoetario')),
            ],
        ),
        migrations.AddField(
            model_name='cualidades',
            name='grupo_etario',
            field=models.ManyToManyField(through='gestion_cualidades.RelacionGrupoEtarioCualidad', to='gestion_miembros.grupoetario'),
        ),
    ]