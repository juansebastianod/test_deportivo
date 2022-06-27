# Generated by Django 4.0.3 on 2022-06-02 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deportista',
            fields=[
                ('codigoDeportista', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(max_length=30, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=30, verbose_name='Apellido Materno')),
                ('edad', models.PositiveSmallIntegerField()),
                ('altura', models.PositiveSmallIntegerField()),
                ('email', models.CharField(max_length=30, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Deportista',
                'verbose_name_plural': 'Deportistas',
                'db_table': 'deportista',
            },
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('codigoEntrenador', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(max_length=30, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=30, verbose_name='Apellido Materno')),
                ('edad', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Entrenador',
                'verbose_name_plural': 'Entrenadores',
                'db_table': 'entrenador',
            },
        ),
        migrations.CreateModel(
            name='Test_Tiros_De_Tres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partidos', models.PositiveSmallIntegerField()),
                ('tiros_tres', models.PositiveSmallIntegerField()),
                ('tiros_fallidos', models.PositiveSmallIntegerField()),
                ('porcentaje_tiro_de_tres', models.PositiveSmallIntegerField()),
                ('codigoDeportista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrenador.deportista')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Tiros_De_Dos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partidos', models.PositiveSmallIntegerField()),
                ('tiros_dentro', models.PositiveSmallIntegerField()),
                ('tiros_fallidos', models.PositiveSmallIntegerField()),
                ('porcentaje_tiro_de_dos', models.PositiveSmallIntegerField()),
                ('codigoDeportista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrenador.deportista')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Puntos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partidos', models.PositiveSmallIntegerField()),
                ('puntos', models.PositiveSmallIntegerField()),
                ('puntos_por_partidos', models.PositiveSmallIntegerField()),
                ('codigoDeportista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrenador.deportista')),
            ],
        ),
        migrations.CreateModel(
            name='Salto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Salto', models.PositiveSmallIntegerField()),
                ('codigoDeportista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrenador.deportista')),
            ],
        ),
        migrations.CreateModel(
            name='Robos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partidos', models.PositiveSmallIntegerField()),
                ('robos', models.PositiveSmallIntegerField()),
                ('robos_por_partido', models.PositiveSmallIntegerField()),
                ('codigoDeportista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrenador.deportista')),
            ],
        ),
        migrations.AddField(
            model_name='deportista',
            name='codigoEntrenador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Entrenador.entrenador'),
        ),
    ]
