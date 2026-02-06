from django.db import models

# Create your models here.
class Student(models.Model):
    Studentname = models.CharField(max_length=100)
    Studentage = models.IntegerField()
    Studentemail = models.EmailField(unique=True)
   

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.Studentname 


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
class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    #studentPrilfe id --> pk create auto...
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.Studentname 
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    #after table creation adding new field
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName    

class customer(models.Model):
    customerName = models.CharField(max_length=100)
    customerEmail = models.EmailField(unique=True)
    customerPhone = models.CharField(max_length=10)
    customerAddress = models.CharField(max_length=200)

    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.customerName

class bankdetails(models.Model):
    customerId = models.OneToOneField(customer,on_delete=models.CASCADE)
    bankName = models.CharField(max_length=100)
    accountNumber = models.CharField(max_length=20)
    ifscCode = models.CharField(max_length=20)

    class Meta:
        db_table = "bankdetails"

    def __str__(self):
        return self.customerId.customerName

class buyer(models.Model):
    buyerName = models.CharField(max_length=100)
    buyerEmail = models.EmailField(unique=True)
    buyerPhone = models.CharField(max_length=10)
    buyerAddress = models.CharField(max_length=200)

    class Meta:
        db_table = "buyer"

    def __str__(self):
        return self.buyerName
class productdetail(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = 'productdetail'
    def __str__(self):
        return self.productName
class order(models.Model):
    orderDate = models.DateField()
    orderStatus = models.CharField(max_length=20)
    buyerId = models.ForeignKey(buyer,on_delete=models.CASCADE)
    productId = models.ForeignKey(productdetail,on_delete=models.CASCADE)

    class Meta:
        db_table = "order"

    def __str__(self):
        return f"Order {self.id} by {self.buyerId.buyerName}"

class feedback(models.Model):   
    feedbackText = models.TextField()
    feedbackRating = models.IntegerField()
    customerId = models.ForeignKey(order,on_delete=models.CASCADE)

    class Meta:
        db_table = "feedback"

    def __str__(self):
        return f"Feedback {self.id} for Order {self.customerId.id}"
