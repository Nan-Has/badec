from django.db import models

# Create your models here.
sex_choice = (
    ('Homme', 'Homme'),
    ('Femme', 'Femme')
)


class Departement(models.Model):
    id = models.CharField(primary_key='True', max_length=10)
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.nom

class Employe(models.Model):
    dept = models.ForeignKey(Departement, on_delete=models.CASCADE)
    id = models.CharField(primary_key='True', max_length=10)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Homme')
    date_naissance = models.DateField(default='1990-01-01')
    tel = models.IntegerField(default=0)
    email = models.EmailField(max_length=200)
    date_embauche = models.DateField(default='2022-01-01')
    salaire_mensuel = models.FloatField(default=0)


    def __str__(self):
        return self.nom

class Gestionnaire(models.Model):
    dept = models.ForeignKey(Departement, on_delete=models.CASCADE)
    emp = models.ForeignKey(Employe, on_delete=models.CASCADE)

class Consultant(models.Model):
    dept = models.ForeignKey(Departement,default='Consultance', on_delete=models.CASCADE)
    id = models.CharField(primary_key='True', max_length=10)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Homme')
    date_naissance = models.DateField(default='1990-01-01')
    tel = models.IntegerField(default=0)
    email = models.EmailField(max_length=200)
    profil = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.nom

class Categorie_salle(models.Model):
    id = models.CharField(primary_key='True', max_length=10)
    nom = models.CharField(max_length=200)
    capacite_max = models.FloatField(default=0)

    def __str__(self):
        return self.nom

class Salle(models.Model):
    id = models.CharField(primary_key='True', max_length=10)
    numero_salle = models.IntegerField(default=0)
    nom = models.CharField(max_length=200, default='Salle 25')
    categorie = models.ForeignKey(Categorie_salle, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class disponibilite_salle(models.Model):
    id = models.CharField(primary_key='True', max_length=10)
    date_disponibilite = models.DateField(default='2022-01-01')
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Client(models.Model):
    id = models.CharField(primary_key='True', max_length=10)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    sex = models.CharField(max_length=50, choices=sex_choice, default='Homme')
    tel = models.IntegerField(default=0)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.nom


class Payement(models.Model):
    id = models.CharField(primary_key='True', max_length=10)
    methode_payement = models.CharField(max_length=20)
    montant = models.FloatField()
    date_payement = models.DateField(default='2022-01-01')

    def __str__(self):
        return self.methode_payement


class Reservation(models.Model):
    id = models.CharField(primary_key='True', max_length=10)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField(default='2022-01-01')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payement, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Projet(models.Model):
    id = models.CharField(primary_key='True', max_length=10)
    dept = models.ForeignKey(Departement,default='0', on_delete=models.CASCADE)
    projet_num = models.IntegerField(default=0)
    nom = models.CharField(max_length=200)
    date_debut = models.DateField(default='')
    date_fin = models.DateField(default='2022-01-01')
    description = models.CharField(max_length=5000)

    def __str__(self):
        return self.nom
    


