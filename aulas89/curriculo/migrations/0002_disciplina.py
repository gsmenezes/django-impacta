# Generated by Django 3.0.5 on 2020-04-26 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('etiqueta', models.SlugField(verbose_name='Etiqueta')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga Horaria')),
            ],
        ),
    ]
