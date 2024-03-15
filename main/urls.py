from django.urls import path

from main.views import home, contact

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('about_us/', contact, name='contact'),
]
