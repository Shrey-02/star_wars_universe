from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    terrain = models.CharField(max_length=100)
    image = models.ImageField(upload_to='planet_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Resident(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    mass = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='residents')
    

    def __str__(self):
        return self.name
