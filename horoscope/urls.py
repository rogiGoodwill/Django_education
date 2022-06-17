from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type', views.list_zodiac),
    path('type/<str:element>', views.type_zodiacs, name='type-name'),
    path('<int:sign_zodiac>', views.zodiacs_by_num),
    path('<str:sign_zodiac>', views.zodiacs, name='horoscope-name'),


]
