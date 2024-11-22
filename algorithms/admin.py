from django.contrib import admin
from .models import Type, Name, Complexity, Algorithm, AlgorithmOfTheDay

admin.site.register(Type)
admin.site.register(Name)
admin.site.register(Complexity)
admin.site.register(AlgorithmOfTheDay)
admin.site.register(Algorithm)
