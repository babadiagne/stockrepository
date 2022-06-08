from django.db import models

# Create your models here.
class Class1 (models.Model):
  auteurs = models.CharField (max_length = 42)
  larelation = models.ForeignKey ('Class2' , on_delete=models.CASCADE)
#first class
  def __str__ (self):
    return self.auteurs

#second class
class Class2 (models.Model):
  noms = models.CharField (max_length = 45)

  def __str__ (self):
    return self.noms

