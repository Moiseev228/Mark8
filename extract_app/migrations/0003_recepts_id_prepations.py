# Generated by Django 2.0.5 on 2018-06-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extract_app', '0002_auto_20180515_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepts',
            name='id_prepations',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]