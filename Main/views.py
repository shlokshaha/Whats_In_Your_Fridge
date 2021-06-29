from django.shortcuts import render


def home(request):
    return render(request, 'Main/home.html', {'title': 'Home'})


def instructions(request):
    return render(request, 'Main/instructions.html', {'title': 'Instructions'})
