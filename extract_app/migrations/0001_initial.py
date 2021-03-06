# Generated by Django 2.0.5 on 2018-05-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List_prepations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_recept', models.IntegerField()),
                ('id_pripations', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patiens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('adress', models.CharField(max_length=100)),
                ('polis', models.CharField(max_length=16)),
                ('exmotion', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Prepations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('type_prepations', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recepts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_patiens', models.IntegerField()),
                ('id_staff', models.IntegerField()),
                ('date_issue', models.CharField(max_length=8)),
            ],
        ),
    ]
