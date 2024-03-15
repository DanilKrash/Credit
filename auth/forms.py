from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in list(self.fields.values()):
            field.widget.attrs.update({'class': 'form-control'})


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in list(self.fields.values()):
            field.widget.attrs.update({'class': 'form-control'})
