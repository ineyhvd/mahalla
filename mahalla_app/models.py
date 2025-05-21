from django.db import models

class Viloyat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tuman(models.Model):
    name = models.CharField(max_length=100)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE, related_name='tumanlar')

    def __str__(self):
        return self.name

class Mahalla(models.Model):
    name = models.CharField(max_length=100)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE, related_name='mahallalar')
    population = models.PositiveIntegerField(default=0)
    houses = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name