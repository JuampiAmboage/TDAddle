from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Algorithm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.type.name} - {self.name}"
