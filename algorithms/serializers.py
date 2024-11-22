from rest_framework import serializers
from .models import Algorithm, Type, Name, Complexity

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name']

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ['name']

class ComplexitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Complexity
        fields = ['name']

class AlgorithmSerializer(serializers.ModelSerializer):
    name = NameSerializer()
    type = TypeSerializer()
    complexity = ComplexitySerializer()

    class Meta:
        model = Algorithm
        fields = ['name', 'type', 'complexity',  'description', 'code']