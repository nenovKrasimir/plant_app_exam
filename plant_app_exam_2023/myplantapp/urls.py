from django.urls import path, include

from plant_app_exam_2023.myplantapp import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('create_profile/', views.create_profile, name='create-profile'),
    path('create_plant/', views.create_plant, name='create-plant'),
    path('catalogue/', views.show_catalogue, name='show-catalogue')
]