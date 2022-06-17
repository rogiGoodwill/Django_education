from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

day_of_week = {
    'monday': 'Стать миллионером',
    'tuesday': 'Потратить миллион',
    'wednesday': 'Стать миллионером',
    'thursday': 'Потратить миллион',
    'friday': 'Стать миллионером',
    'saturday': 'Потратить миллион',
    'sunday': 'Стать миллионером',
}


def my_schedule(request, day):
    if day.lower() in day_of_week:
        return render(request, 'week_days/greeting.html')
        #return HttpResponse(day_of_week[day].lower())
    return HttpResponseNotFound(f'Не существующий день недели - {day}')


def my_schedule_num(request, day):
    if day in range(1, 8):
        return HttpResponseRedirect(reverse('day-name', args={list(day_of_week)[day - 1]}))
    return HttpResponse(f'Неверный номер дня - {day}')
