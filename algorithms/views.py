from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from .models import AlgorithmOfTheDay, Algorithm, Type, Name, Complexity
from .serializers import AlgorithmSerializer, TypeSerializer, NameSerializer, ComplexitySerializer
import random

@api_view(['GET'])
def get_algorithm_of_the_day(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

    today = timezone.now().date()
    algorithm_of_the_day, created = AlgorithmOfTheDay.objects.get_or_create(
        date=today,
        defaults={'algorithm': random.choice(Algorithm.objects.all())}
    )

    algorithm_serializer = AlgorithmSerializer(algorithm_of_the_day.algorithm)
    types_serializer = TypeSerializer(Type.objects.all(), many=True)
    names_serializer = NameSerializer(Name.objects.all(), many=True)
    complexities_serializer = ComplexitySerializer(Complexity.objects.all(), many=True)

    response_data = {
        'algorithm-of-the-day': algorithm_serializer.data,
        'dropdown-types': types_serializer.data,
        'dropdown-names': names_serializer.data,
        'dropdown-complexities': complexities_serializer.data,
    }

    return JsonResponse(response_data, safe=False)