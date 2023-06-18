from django import forms

from .models import Plant, Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreatePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class EditPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class DeletePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
