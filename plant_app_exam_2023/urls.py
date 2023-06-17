from django.contrib import admin
from django.urls import path, include
import plant_app_exam_2023.myplantapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(plant_app_exam_2023.myplantapp.urls))
]
