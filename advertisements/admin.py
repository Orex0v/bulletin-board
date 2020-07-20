from django.contrib import admin

from .models import Ad, Category, City, EmailMessage

admin.site.register(Category)
admin.site.register(City)
admin.site.register(EmailMessage)
admin.site.register(Ad)
print('x')
