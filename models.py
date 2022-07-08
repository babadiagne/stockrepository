from django.db import models

# Create your models here.
class Article(models.Model):
  titre=models.CharField(max_length=100)
  auteur=models.CharField(max_length=100)
  contenu=models.TextField(null=True)
  date=models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="Date de parution")
  categorie=models.ForeignKey('Categorie',on_delete=models.CASCADE)
  client=models.ForeignKey('Client',on_delete=models.CASCADE)


  def __str__(self):
    return self.titre

class Categorie(models.Model):
  nom=models.CharField(max_length=100)

  def __str__(self):
    return self.nom

class Client(models.Model):
  pnom=models.CharField(max_length=100)

  def __str__(self):
    return self.pnom

#member:malick diagne
#member:hamath
#member:general
#member:fama
#member:moussa
