from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(("Tên đăng nhập"), max_length=50)
    password = models.CharField(("Mật khẩu"), max_length=50)  
class Information(models.Model):
    name = models.CharField(("Họ tên"), max_length=50)
    address = models.CharField(("Địa chỉ"), max_length=50)
    phoneNumber = models.PhoneNumberField(("Số điện thoại"))
class Item:
    typeItem = models.CharField(("Loại đồ"), max_length=50)
    catalog = models.CharField(("Danh sách kiểu đồ"), max_length=50)
    time = models.TimeField(("Thời gian"), auto_now=False, auto_now_add=False)
    address = models.CharField(("Địa điểm"), max_length=50)
    content = models.CharField(("Nội dung"), max_length=500)
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    status = models.CharField(("Tình trạng"), max_length=50)

    