from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Доп. поля пользователя"""
    phone = models.CharField('Номер телефона', max_length=12, null=False, unique=False)
    image = models.ImageField('Аватар',
                              upload_to='images/users/',
                              null=True,
                              default='images/users/user.png'
                              )

