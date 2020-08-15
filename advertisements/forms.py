from django import forms

from .models import Ad


class AddPost(forms.ModelForm):
    """Форма добавления новой записи"""

    class Meta:
        model = Ad
        fields = ('title', 'description', 'image', 'category', 'city', 'price', 'status')

