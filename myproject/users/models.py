from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="姓名")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="头像")

    def __str__(self):
        return self.name
