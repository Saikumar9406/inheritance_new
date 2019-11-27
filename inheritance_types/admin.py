from django.contrib import admin
from .models import student,employee,product,proxy
# Register your models here.
admin.site.register(student)
admin.site.register(employee)
admin.site.register(product)
admin.site.register(proxy)