from django.contrib import admin
from .models import Student, Product, marks, StudentProfile, Category, Service, customer, bankdetails, productdetail, order,buyer,feedback



# Register your models here.
admin.site.register(Student)
admin.site.register(customer)
admin.site.register(bankdetails)
admin.site.register(marks)
admin.site.register(Product)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(productdetail)
admin.site.register(order)  
admin.site.register(buyer)
admin.site.register(feedback)

