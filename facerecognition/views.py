from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def index (request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() #creating the note object
        else:
            print(form.errors)  # Print form errors to console for debugging
        return render(request, 'home.html', {'photos': photos})
    else:
        form = PhotoForm()
    return render(request, 'home.html', {'photos': photos})

