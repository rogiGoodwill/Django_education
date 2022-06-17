from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import pi


# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    #return HttpResponse(f"Площадь прямоугольника размером {width}х{height} равна {width * height}")
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width: int):
    #return HttpResponse(f"Площадь квадрата размером {width}х{width} равна {width ** 2}")
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius: int):
    #return HttpResponse(f"Площадь кругра радиуса {radius} равна {round(pi * radius ** 2, 1)}")
    return render(request, 'geometry/circle.html')


def redirect_rectangle_area(request, width, height):
    return HttpResponseRedirect(reverse('rectangle-name', args=[width, height]))


def redirect_square_area(request, width):
    return HttpResponseRedirect(reverse('square=name', args=[width]))


def redirect_circle_area(request, radius):
    return HttpResponseRedirect(reverse('circle-name', args=[radius]))
