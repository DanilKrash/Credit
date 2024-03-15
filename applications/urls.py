from django.urls import path

from applications.views import send_applic, whating_applic, all_applic, change_status

app_name = 'applications'

urlpatterns = [
    path('send_applic/', send_applic, name='send_applic'),
    path('whate_applic/', whating_applic, name='whate_applic'),
    path('all_applic/', all_applic, name='all_applic'),
    path('change_status/<int:applic_id>/', change_status, name='change_status'),
]
