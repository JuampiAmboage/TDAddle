from django.db import models
from django.utils import timezone

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Complexity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Algorithm(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    code = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    complexity = models.ForeignKey(Complexity, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.type.name} - {self.name}"

class AlgorithmOfTheDay(models.Model):
    date = models.DateField(default=timezone.now)
    algorithm = models.ForeignKey('Algorithm', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.algorithm.name}"