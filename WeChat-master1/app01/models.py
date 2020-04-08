from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=32,verbose_name="用户名")
    pwd = models.CharField(max_length=64,verbose_name="密码")
    wx_id = models.CharField(max_length=32,null=True,blank=True,verbose_name="微信号")
