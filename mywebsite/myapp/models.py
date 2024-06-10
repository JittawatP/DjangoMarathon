from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,default=10)
    image = models.ImageField(upload_to='product_images/', null=True, blank= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
class Staff(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.tel}, {self.email})'


class ContactUs(models.Model):
    name = models.CharField(max_length=200,verbose_name='ชื่อผู้ถาม (name)')
    title = models.CharField(max_length=200,verbose_name='ชื่อปัญหา (title)')
    detail = models.TextField(null=True,blank=True,verbose_name='รายละเอียดปัญหา (detail)')
    email = models.CharField(max_length=200,verbose_name='อีเมลผู้ติดต่อ (email)')
    done = models.BooleanField(default=False,verbose_name='แก้ปัญหาจบแล้วยัง? (done)')
    summary = models.TextField(null=True,blank=True,verbose_name='สรุปว่าปัญหานี้แก้อย่างไร (summary)')

    def __str__(self):
        return f'{self.name} ({self.title}, {self.detail},{self.email},{self.done},{self.summary})'

