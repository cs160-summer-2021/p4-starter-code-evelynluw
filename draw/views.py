# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html', {
        'size': request.GET.get('size', 'small')
    })

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name': room_name
    })

def recipe_small(request):
    return render(request, 'recipe/recipe_small.html')

def recipe_large(request):
    return render(request, 'recipe/recipe_large.html')
