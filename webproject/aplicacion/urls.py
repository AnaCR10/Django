from django.urls import path
from aplicacion import views

urlpatterns = [
   # path('',views.index, name='index'),
    path('',views.index, name='index'),
    path('viernes/',views.metodoViernes, name='viernes'),
    
]

