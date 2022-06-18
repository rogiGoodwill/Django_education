from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here.

class Zodiac:
    def __init__(self, zodiac_name, description, zodiac_type):
        self.zodiac_name = zodiac_name
        self.zodiac_description = description
        self.zodiac_type = zodiac_type


elements = ['fire', 'earth', 'air', 'water']

aries = Zodiac('aries', 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).', elements[0])
taurus = Zodiac('taurus', 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).', elements[1])
gemini = Zodiac('gemini', 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).', elements[2])
cancer = Zodiac('cancer', 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).', elements[3])
leo = Zodiac('leo', 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).', elements[0])
virgo = Zodiac('virgo', 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).', elements[1])
libra = Zodiac('libra', 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).', elements[2])
scorpio = Zodiac('scorpio', 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).', elements[3])
sagittarius = Zodiac('sagittarius', 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
                     elements[0])
capricorn = Zodiac('capricorn', 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
                   elements[1])
aquarius = Zodiac('aquarius', 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
                  elements[2])
pisces = Zodiac('pisces', 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).', elements[3])

signs = [aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces]


# signs = {
#     'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
#     'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
#     'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
#     'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
#     'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
#     'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
#     'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
#     'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
#     'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
#     'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
#     'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
#     'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
# }


def index(request):
    # li_path = ''
    # for sign in signs:
    #     href_path = reverse('horoscope-name', args=[sign.zodiac_name])
    #     li_path += f'<li><a href={href_path}>{sign.zodiac_name.title()}</a></li>'
    # # zodiac_list = f'<ol>{li_path}</ol>'
    # return HttpResponse(zodiac_list)
    data = {
        'signs': signs,
    }
    return render(request, 'horoscope/index.html', context=data)


def zodiacs(request, sign_zodiac: str):
    data = {'sign': sign_zodiac}
    for sign in signs:
        if sign_zodiac == sign.zodiac_name:
            data['zodiac_description'] = sign.zodiac_description
    return render(request, 'horoscope/info_zodiac.html', context=data)


def zodiacs_by_num(request, sign_zodiac):
    if sign_zodiac in range(1, len(signs) + 1):
        return HttpResponseRedirect(reverse('horoscope-name', args={signs[sign_zodiac - 1].zodiac_name}))
    return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')


def list_zodiac(request):
    li = ''
    for t_zodiac in elements:
        li += f'<li><a href={reverse("type-name", args=[t_zodiac])}>{t_zodiac.title()}</a></li>'
    link_path = f'<ul>{li}</ul>'
    return HttpResponse(link_path)


def type_zodiacs(request, element):
    li = ''
    if element in elements:
        for sign in signs:
            if element == sign.zodiac_type:
                href_path = reverse('horoscope-name', args=[sign.zodiac_name])
                li += f'<li><a href={href_path}>{sign.zodiac_name.title()}</a></li>'
        zodiac_list = f'<ul>{li}</ul>'
        return HttpResponse(zodiac_list)
    return HttpResponseNotFound(f'Не существующая стихия - {element}')


def fake(request):
    return render(request, 'horoscope/fake.html')
