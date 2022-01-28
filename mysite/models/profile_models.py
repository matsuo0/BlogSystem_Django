from django.db import models


class Profile(models.Model):
    username = models.CharField(default="匿名ユーザー", max_length=30)

    zipcode = models.CharField(default="", max_length=8)
    # 000-0000, 0000000

    prefecture = models.CharField(default="", max_length=6)

    city = models.CharField(defalut="", max_length=100)

    address = models.CharField(default="", max_length=200)