from django.shortcuts import render, redirect
from .forms import CreateProfileForm, CreatePlantForm, EditProfileForm, EditPlantForm
from .models import Profile, Plant


# Create your views here.

def home_page(request):
    profile = Profile.objects.first()
    return render(request=request, template_name='home-page.html', context={"profile": profile})


def create_profile(request):
    form = CreateProfileForm()

    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {'form': form}
    return render(request=request, template_name='create-profile.html', context=context)


def details_profile(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    context = {'profile': profile, 'plants': plants}
    return render(request=request, template_name='profile-details.html', context=context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {'profile': profile, 'form': form}
    return render(request=request, template_name='edit-profile.html', context=context)


def delete_profile(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    if request.method == "POST":
        profile.delete()
        plants.delete()
        return redirect('home-page')

    return render(request=request, template_name='delete-profile.html', context={'profile': profile})


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


def details_plant(request, pk):
    plant = Plant.objects.get(id=pk)
    profile = Profile.objects.first()
    context = {'plant': plant, 'profile': profile}
    return render(request=request, template_name='plant-details.html', context=context)


def edit_plant(request, pk):
    plant = Plant.objects.get(id=pk)
    form = EditPlantForm(instance=plant)

    if request.method == "POST":
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('show-catalogue')

    return render(request=request, template_name='edit-plant.html', context={'form': form})


def show_catalogue(request):
    plants = Plant.objects.all()
    profile = Profile.objects.first()
    return render(request=request, template_name='catalogue.html', context={'plants': plants, 'profile': profile})
