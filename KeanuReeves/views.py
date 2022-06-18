from django.shortcuts import render


# Create your views here.

def about_KeanuReeves(request):
    data = {
        'year_born': '1964 года',
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'KeanuReeves/about_Keanu.html', data)
