from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from dataclasses import dataclass


# Create your views here.


@dataclass
class RecordsList:
    record_name: str
    record_description: str


records = {
    'strong_beat': RecordsList('Мощный удар', """
    Норвежец Narve Laeret прославился тем, что 9 ноября 2006 г. в Осло на съемках телевизионной передачи
"Senkveld" телеканал TV2 в течение одной минуты сломал рукой 90 бетонных блоков.
    """),

    'hamburger': RecordsList('Гамбургер', """
    31 июля 2006г. в меню гриль-бара Bob's BBQ & Grill на пляже Паттайя в Таиланде был включен самый
большой гамбургер весом 35,6 кг.
    """),

    'hedgehog_man': RecordsList('Человек-ёж', """
    23 марта 2004 г. в городе Наньнин (Китай) в голову и лицо отважного китайца Вей Шенгчу было воткнуто
1790 игл для иглоукалывания.     
    """),
}


def list_of_records(request):
    li = ''
    for el in records:
        li += f'<li><a href={reverse("record-name", args=[el])}>{records[el].record_name}</a></li>'
    order_list = f'<ol>{li}</ol>'
    return HttpResponse(order_list)


def show_record(request, record_val):
    if record_val in records:
        data = {
            'record': records[record_val]
        }
        return render(request, 'guinness_records/record.html', context=data)
    return HttpResponse('Неверная ссылка на рекорд')


def people_represent(request):
    people = [
        'Жукова Анна Константиновна',
        'Юлия Степановна Потапова',
        'Гущин Аполлинарий Тимурович',
        'Дорофей Ярославович Третьяков',
        'Селезнева Анна Тарасовна',
        'Федотов Симон Харлампьевич',
        'Красильникова Вера Борисовна',
        'Бажен Тихонович Костин',
        'Веселова Анжелика Тимофеевна',
        'Щербаков Самсон Феодосьевич'
    ]
    data = {
        'people': people,
    }
    return render(request, 'guinness_records/people.html', context=data)


def people_represent_detail(request):
    people = [
        {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
        {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
        {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
        {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
        {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
        {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
        {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
        {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
        {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
        {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
    ]

    data = {
        'people': people,
    }
    return render(request, 'guinness_records/people_detail.html', context=data)
