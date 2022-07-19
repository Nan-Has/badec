from django.contrib import admin


from .models import Departement, Employe,Gestionnaire, Consultant,Categorie_salle, Projet
from .models import Salle, disponibilite_salle, Client, Payement, Reservation

# Register your models here.


@admin.register(Departement, Employe,Gestionnaire, Projet, Consultant,Categorie_salle,Salle, disponibilite_salle, Client, Payement, Reservation)

class GenericAdmin(admin.ModelAdmin):
    pass