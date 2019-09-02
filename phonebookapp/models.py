from django.db import models


class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)


class Telefon(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=50)


class Email(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False, on_delete=models.CASCADE)
    email = models.EmailField()
