from django.db import models

# Create your models here.

# creating company model

class company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('Non IT','Non IT'),('Mobile phones','Mobile Phones')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
## Employee Model

class employee(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=50)
    adress=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    position=models.CharField(max_length=100)
    company=models.ForeignKey(company,on_delete=models.CASCADE)