from allauth.account.adapter import DefaultAccountAdapter
from users.models import CustomUser


class MyCoolAdapter(DefaultAccountAdapter):

    def clean_phone(self):
        print('Бля')
        if CustomUser.objects.filter(phone=self.cleaned_data["phone"]).exists():
            self.add_error("phone", forms.ValidationError("ERROR"))
        return self.cleaned_data["phone"]