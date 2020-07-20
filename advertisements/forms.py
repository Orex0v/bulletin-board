from django import forms

from .models import Ad, EmailMessage


class AddPost(forms.ModelForm):
    """Форма добавления новой записи"""

    class Meta:
        model = Ad
        fields = ('title', 'description', 'image', 'category', 'city', 'price')


class SendMailForm(forms.ModelForm):
    """Форма для отправки сообщений на почту"""

    class Meta:
        model = EmailMessage
        fields = ('email', 'message')
