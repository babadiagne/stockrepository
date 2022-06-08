from django.db import models

# Create your models here.
class Class1 (models.Model):
  auteurs = models.CharField (max_length = 30)
  categorie = models.ForeignKey ('Class2' , on_delete=models.CASCADE)
#first class
  def __str__ (self):
    return self.auteurs

#second class
class Class2 (models.Model):
  noms = models.CharField (max_length = 30)

  def __str__ (self):
    return self.noms

