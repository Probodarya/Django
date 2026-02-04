from django.contrib import admin
from .models import Student, Product, marks



# Register your models here.
admin.site.register(Student)
admin.site.register(marks)
admin.site.register(Product)