# Generated by Django 4.2 on 2023-07-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('id_colaborador', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('departamento', models.TextField(max_length=255)),
            ],
        ),
    ]
