from django.urls import path

from .views import weekdays, weekdays_uz, weekdays_ru, weekdays_eng

urlpatterns = [
    path('', weekdays, name='weekdays_table'),
    path('weekdays/uz', weekdays_uz, name='weekdays_uz'),
    path('weekdays/ru', weekdays_ru, name='weekdays_ru'),
    path('weekdays/eng', weekdays_eng, name='weekdays_eng'),
]