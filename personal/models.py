from django.db import models

PRIORITY_CHOICES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
]

class Question(models.Model):
    title = models.CharField(max_length=60)
    question = models.TextField(max_length=400)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "The Question"
        verbose_name_plural = "Peoples Questions"

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    area = models.FloatField()
    
    def __str__(self):
        return self.name


class Cattle(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    breed = models.CharField(max_length=50)
    number = models.IntegerField()
    weight = models.FloatField()
    age = models.IntegerField()
    is_pregnant = models.BooleanField()
    
    def __str__(self):
        return self.breed


class Pasture(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    area = models.FloatField()
    
    def __str__(self):
        return self.type


class ManureManagement(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    method = models.CharField(max_length=100)
    
    def __str__(self):
        return self.method


class EmissionFactor(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    
    def __str__(self):
        return self.name


class Emission(models.Model):
    cattle = models.ForeignKey(Cattle, on_delete=models.CASCADE)
    pasture = models.ForeignKey(Pasture, on_delete=models.CASCADE)
    manure_management = models.ForeignKey(ManureManagement, on_delete=models.CASCADE)
    emission_factor = models.ForeignKey(EmissionFactor, on_delete=models.CASCADE)
    emission = models.FloatField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cattle} - {self.date}"