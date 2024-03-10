from django.urls import path

from .views import weekdays, weekdays_uz, weekdays_ru, weekdays_eng

urlpatterns = [
    path('', weekdays, name='weekdays_table'),
    path('weekdays/uz', weekdays_uz, name='hafta kunklari'),
    path('weekdays/ru', weekdays_ru, name='дни недели'),
    path('weekdays/eng', weekdays_eng, name='weekdays')
]