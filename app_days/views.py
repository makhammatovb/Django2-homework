from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


links = "<ul>"
links += "<li><a href='/'><button>Main</button></a></li>"
links += "<li><a href='/weekdays/uz'><button>Hafta kunlari</button></a></li>"
links += "<li><a href='/weekdays/ru'><button>Дни недели</button></a></li>"
links += "<li><a href='/weekdays/eng'><button>Weekdays</button></a></li>"
links += "</ul>"

def weekdays(request):
    weekdays = {
        'English': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'Uzbek': ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba'],
        'Russian': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    }

    html = "<h1>Weekdays in 3 Languages</h1>"
    html += "<table style='border-collapse: collapse;'>"
    html += "<tr><th style='border: 1px solid black; padding: 8px;'>English</th><th style='border: 1px solid black; padding: 8px;'>Uzbek</th><th style='border: 1px solid black; padding: 8px;'>Russian</th></tr>"

    for i in range(7):
        html += "<tr>"
        for language in ['English', 'Uzbek', 'Russian']:
            html += f"<td style='border: 1px solid black; padding: 8px;'>{weekdays[language][i]}</td>"
        html += "</tr>"

    html += "</table>"
    html += links
    return HttpResponse(html)

def weekdays_uz(request):
    kunlar = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']

    html = "<h1>Hafta Kunlari</h1>"
    html += "<table style='border-collapse: collapse;'>"
    html += "<tr><th style='border: 1px solid black; padding: 8px;'>Kun</th></tr>"

    for kun in kunlar:
        html += f"<tr><td style='border: 1px solid black; padding: 8px;'>{kun}</td></tr>"

    html += "</table>"
    html += links
    return HttpResponse(html)

def weekdays_ru(request):
    дни = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    html = "<h1>Дни недели</h1>"
    html += "<table style='border-collapse: collapse;'>"
    html += "<tr><th style='border: 1px solid black; padding: 8px;'>День</th></tr>"

    for день in дни:
        html += f"<tr><td style='border: 1px solid black; padding: 8px;'>{день}</td></tr>"

    html += "</table>"
    html += links
    return HttpResponse(html)

def weekdays_eng(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    html = "<h1>Weekdays</h1>"
    html += "<table style='border-collapse: collapse;'>"
    html += "<tr><th style='border: 1px solid black; padding: 8px;'>Weekday</th></tr>"

    for day in days:
        html += f"<tr><td style='border: 1px solid black; padding: 8px;'>{day}</td></tr>"

    html += "</table>"
    html += links
    return HttpResponse(html)
