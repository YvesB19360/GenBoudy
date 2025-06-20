from django.db import models

class Famille(models.Model):
    nom = models.fields.CharField(max_length=100)
    prenom = models.fields.CharField(max_length=100)
    dateNaissance = models.fields.CharField(max_length = 20 , null = True)
    dateDeces = models.fields.CharField(max_length = 20 , null = True)
    villeNaissance = models.fields.CharField(max_length = 50 , null = True)
    def __str__(self):
        return f'{self.nom}'
    
class Cousin(models.Model):
    nom = models.fields.CharField(max_length=100)
    prenom = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.nom}'
    
class Melimelo(models.Model):
    nom = models.fields.CharField(max_length=100)
    prenom = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.nom}'