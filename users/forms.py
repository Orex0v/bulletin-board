from allauth.account.forms import SignupForm
from allauth.account.forms import forms
from django.db import IntegrityError


class MyCustomSignupForm(SignupForm):
    """Форма регистрации"""
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['phone'] = forms.CharField(required=True)
        self.fields['image'] = forms.FileField(required=False)



    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.phone = self.cleaned_data['phone']
        if self.cleaned_data['image']:
            user.image = self.cleaned_data['image']
        user.save()
        return user