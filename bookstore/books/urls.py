from django.urls import path 
from . import views
# Eğer books a bir request gelirse viewlerden indexi çalıştır ve ismide index olsun dedik.
urlpatterns = [
    path('',views.index,name="index")
]
