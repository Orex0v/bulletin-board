from django import forms

from .models import Ad, EmailMessage


class AddPost(forms.ModelForm):
    """Форма добавления новой записи"""

    class Meta:
        model = Ad
        fields = ('title', 'description', 'image', 'category', 'city', 'price')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.Meta.fields:
    #         self.fields[field].widget.attrs.update({
    #             'class': 'form-control input-md'
    #         })




class SendMailForm(forms.ModelForm):
    """Форма для отправки сообщений на почту"""
    class Meta:
        model = EmailMessage
        fields = ('email', 'message')

    def send_mail(self):
        pass


