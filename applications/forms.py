from django import forms

from applications.models import Credit


class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['price', 'purpose', 'city']

    def save(self, user, commit=True):
        credit = super().save(commit=False)
        credit.user = user
        return super(CreditForm, self).save()


class ChangeStatusForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['status']

        widgets = {
            'status': forms.Select(choices=Credit.Status.choices)
        }
