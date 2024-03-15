from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy
from django.views.generic import CreateView

from auth.forms import CustomAuthenticationForm, CustomUserCreationForm

app_name = 'custom_auth'

urlpatterns = [
    path('sign-in/', LoginView.as_view(template_name='auth/sign-in.html', next_page=reverse_lazy('main:home'),
                                       form_class=CustomAuthenticationForm, extra_context={'sign_in_active': 'active'}),
         name='sign-in'),
    path('sign-up/', CreateView.as_view(template_name='auth/sign-up.html', success_url=reverse_lazy('auth:sign-in'),
                                        form_class=CustomUserCreationForm, extra_context={'sign_up_active': 'active'},
                                        model=User), name='sign-up'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('auth:sign-in')), name='logout'),
]
