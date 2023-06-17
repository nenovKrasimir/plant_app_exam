from django.shortcuts import render, redirect
from .forms import CreateProfileForm, CreatePlantForm
from .models import Profile, Plant


# Create your views here.

def home_page(request):
    profile = Profile.objects.first()
    return render(request=request, template_name='home-page.html', context={"profile": profile})


def create_profile(request):
    form = CreateProfileForm
    profile = Profile.objects.first()
    context = {'form': form, 'profile': profile}

    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    return render(request=request, template_name='create-profile.html', context=context)


def create_plant(request):
    form = CreatePlantForm
    profile = Profile.objects.first()
    plant = Plant.objects.first()
    context = {'form': form, 'profile': profile, 'plant': plant}

    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-catalogue')

    return render(request=request, template_name='create-plant.html', context=context)


def show_catalogue(request):
    plants = Plant.objects.all()
    return render(request=request, template_name='catalogue.html', context={'plants': plants})