from django.db import models

class FastFood(models.Model):
    nom1=models.CharField(max_length=31)
    rasm1=models.CharField(max_length=255)
    admin1=models.CharField(max_length=31)
    sana1=models.DateTimeField(auto_now_add=True)

    nom2=models.CharField(max_length=31)
    rasm2=models.CharField(max_length=255)
    admin2=models.CharField(max_length=31)
    sana2=models.DateTimeField(auto_now_add=True) 

    nom3=models.CharField(max_length=31)
    rasm3=models.CharField(max_length=255)
    admin3=models.CharField(max_length=31)
    sana3=models.DateTimeField(auto_now_add=True)

    nom4=models.CharField(max_length=31)
    rasm4=models.CharField(max_length=255)
    admin4=models.CharField(max_length=31)
    sana4=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nom1

class MilliyTaom(models.Model):
    nom1=models.CharField(max_length=31)
    rasm1=models.CharField(max_length=255)
    admin1=models.CharField(max_length=31)
    sana1=models.DateTimeField(auto_now_add=True)

    nom2=models.CharField(max_length=31)
    rasm2=models.CharField(max_length=255)
    admin2=models.CharField(max_length=31)
    sana2=models.DateTimeField(auto_now_add=True) 

    nom3=models.CharField(max_length=31)
    rasm3=models.CharField(max_length=255)
    admin3=models.CharField(max_length=31)
    sana3=models.DateTimeField(auto_now_add=True)

    nom4=models.CharField(max_length=31)
    rasm4=models.CharField(max_length=255)
    admin4=models.CharField(max_length=31)
    sana4=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nom2

class Shirinlik(models.Model):
    nom1=models.CharField(max_length=31)
    rasm1=models.CharField(max_length=255)
    admin1=models.CharField(max_length=31)
    sana1=models.DateTimeField(auto_now_add=True)

    nom2=models.CharField(max_length=31)
    rasm2=models.CharField(max_length=255)
    admin2=models.CharField(max_length=31)
    sana2=models.DateTimeField(auto_now_add=True) 

    nom3=models.CharField(max_length=31)
    rasm3=models.CharField(max_length=255)
    admin3=models.CharField(max_length=31)
    sana3=models.DateTimeField(auto_now_add=True)

    nom4=models.CharField(max_length=31)
    rasm4=models.CharField(max_length=255)
    admin4=models.CharField(max_length=31)
    sana4=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nom3

class Ichimlik(models.Model):
    nom1=models.CharField(max_length=31)
    rasm1=models.CharField(max_length=255)
    admin1=models.CharField(max_length=31)
    sana1=models.DateTimeField(auto_now_add=True)

    nom2=models.CharField(max_length=31)
    rasm2=models.CharField(max_length=255)
    admin2=models.CharField(max_length=31)
    sana2=models.DateTimeField(auto_now_add=True) 

    nom3=models.CharField(max_length=31)
    rasm3=models.CharField(max_length=255)
    admin3=models.CharField(max_length=31)
    sana3=models.DateTimeField(auto_now_add=True)

    nom4=models.CharField(max_length=31)
    rasm4=models.CharField(max_length=255)
    admin4=models.CharField(max_length=31)
    sana4=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nom4