from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), unique=True, on_delete=models.CASCADE, primary_key=True)

    username = models.CharField(default="匿名ユーザー", max_length=30)

    zipcode = models.CharField(default="", max_length=8)
    # 000-0000, 0000000

    prefecture = models.CharField(default="", max_length=6)

    city = models.CharField(defalut="", max_length=100)

    address = models.CharField(default="", max_length=200)
