from django.urls import path
from .views import Homepage

urlpatterns = [
    path('', Homepage ),    #หน้าแรกเวลาเข้าไปโดยไม่ได้ระบุหน้าเช่น   www.book.com
]
