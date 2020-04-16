from django.shortcuts import render
from . import models 
#from models import Board

# Create your views here.

def home(request):
    boards = models.Board.objects.get(id=1)
    boards.name = "New Name"
    boards.save()
    return render(request, "home_001.html", {"boards": [boards]})
