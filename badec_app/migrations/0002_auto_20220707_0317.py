# Generated by Django 3.1.6 on 2022-07-07 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badec_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilite_salle',
            name='date_disponibilite',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_fin',
            field=models.DateField(default='2022-01-01'),
        ),
    ]