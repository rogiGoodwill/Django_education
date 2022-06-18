from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_of_records),
    path('people', views.people_represent),
    path('people_detail', views.people_represent_detail),
    path('<str:record_val>', views.show_record, name='record-name'),

]