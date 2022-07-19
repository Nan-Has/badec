# Generated by Django 3.1.6 on 2022-07-07 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie_salle',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('capacite_max', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.CharField(max_length=50, primary_key='True', serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='Homme', max_length=50)),
                ('tel', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.CharField(max_length=50, primary_key='True', serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='Homme', max_length=50)),
                ('date_naissance', models.DateField(default='1990-01-01')),
                ('tel', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=200)),
                ('profil', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.CharField(max_length=50, primary_key='True', serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('Homme', 'Homme'), ('Femme', 'Femme')], default='Homme', max_length=50)),
                ('date_naissance', models.DateField(default='1990-01-01')),
                ('tel', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=200)),
                ('date_embauche', models.DateField(default='2022-01-01')),
                ('salaire_mensuel', models.FloatField(default=0)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badec_app.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('methode_payement', models.CharField(max_length=20)),
                ('montant', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('numero_salle', models.IntegerField(default=0)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badec_app.categorie_salle')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badec_app.client')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badec_app.payement')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badec_app.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Gestionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badec_app.departement')),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badec_app.employe')),
            ],
        ),
        migrations.CreateModel(
            name='disponibilite_salle',
            fields=[
                ('id', models.CharField(max_length=100, primary_key='True', serialize=False)),
                ('date_disponibilite', models.FloatField(default=0)),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badec_app.salle')),
            ],
        ),
    ]