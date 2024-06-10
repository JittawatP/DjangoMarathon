from django.urls import path
from .views import Homepage,About,Services,Products,Contact

urlpatterns = [
    path('', Homepage, name='home' ),       #หน้าแรกเวลาเข้าไปโดยไม่ได้ระบุหน้าเช่น   www.book.com
    path('about', About, name='about'), 
    path('services', Services, name='services'),  
    path('products',Products, name='products'),
    path('contact',Contact, name='contact'),
    path('home', Homepage, name='home' ),   

]
