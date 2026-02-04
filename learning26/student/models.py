from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
   

    class Meta:
        db_table = 'student'

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = 'product'

class marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    email=models.EmailField(null=True)

    class Meta:
        db_table = 'marks'