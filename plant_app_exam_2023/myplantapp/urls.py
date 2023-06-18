from django.urls import path, include

from plant_app_exam_2023.myplantapp import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('profile/create/', views.create_profile, name='create-profile'),
    path('profile/details', views.details_profile, name='details-profile'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
    path('profile/delete', views.delete_profile, name='delete-profile'),
    path('create_plant/', views.create_plant, name='create-plant'),
    path('details_plant/<int:pk>', views.details_plant, name='details-plant'),
    path('edit/<int:pk>', views.edit_plant, name='edit-plant'),
    path('catalogue/', views.show_catalogue, name='show-catalogue')
]