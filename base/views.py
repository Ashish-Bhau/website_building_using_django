from django.shortcuts import render


# Create your views here.
rooms = [
    {"id":1,"name":"My First Blog"},
    {"id":2,"name":"My Second Blog"},
    {"id":3,"name":"My third Blog"},
]


def home(request):
    return render(request,'home.html',{'rooms':rooms})

def room(request):
    return render(request,'room.html')