from django.urls import path
from . import views

urlpatterns = [
    path('<int:day>', views.my_schedule_num),
    path('<day>', views.my_schedule, name='day-name'),
]
