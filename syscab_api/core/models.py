from django.contrib.auth import get_user_model
from django.db import models

types = (
    ("1", "Particulier"),
    ("2", "Personne morale"),
    ("3", "Institution"),
    )

class Client(models.Model):
    email = models.EmailField(max_length = 200),
    password = models.CharField(max_length = 200),
    tel = models.CharField(max_length = 200),
    pays = models.CharField(max_length = 200),
    type = models.CharField(
        max_length =  15,
        choices = types,
        default = "Particulier",
    )

class Particulier(models.Model):
    nom = models.CharField(max_length = 200),
    prenom = models.CharField(max_length = 200),
    date_de_naissance = models.DateField(),
    lieu_de_naissance = models.CharField(max_length = 200),
    profession = models.CharField(max_length = 200),
    domicile = models.CharField(max_length = 200),
    residence = models.CharField(max_length = 200),
    client = models.OneToOneField(Client, on_delete = models.CASCADE),

class Personne_morale(models.Model):
    raison_sociale = models.CharField(max_length = 200),
    forme_juridique = models.CharField(max_length = 200),
    ville = models.CharField(max_length = 200),
    quartier = models.CharField(max_length = 200),
    rue = models.CharField(max_length = 200),
    boite_postale = models.CharField(max_length = 200),
    autre = models.CharField(max_length = 200),
    client = models.OneToOneField(Client, on_delete = models.CASCADE),


class Institution(models.Model):
    institution = models.CharField(max_length = 200),
    de = models.CharField(max_length = 200),
    client = models.OneToOneField(Client, on_delete = models.CASCADE)

class Nature(models.Model):
    nature = models.CharField(max_length = 200)

Trimestre = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)

class Civile(models.Model):
    libelle = models.CharField(max_length = 200),
    audiance = models.DateField(),
    signification = models.DateField(),
    enregistrement = models.DateTimeField(auto_now_add = True),
    client = models.ManyToManyField(Client),
    reglement = models.CharField(max_length = 200),
    adversaires = models.ManyToManyField(client),
    parent = models.ForeignKey(Civile, on_delete = models.PROTECT),
    trimestre = models.CharField(
        max_length = 1,
        choices = Trimestre,
        default = "1"
    ),
    ref = models.CharField(max_length = 200),
    description = models.TextField(),
    acte = models.FileField()



