from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    title = models.CharField(default='', max_length=30)

    text = models.TextField(default='')

    author = models.CharField(default='', max_length=30)

    created_at = models.DateField(auto_now_add=True)

    updated_at = models.DateField(auto_now=True)

    count = models.IntegerField(default=0)


class Comment(models.Model):
    comment = models.TextField(default="", max_length=500)

    created_at = models.DateField(auto_now_add=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  #

    # OneToOne = 1 対 1
    # ForeignKey = 1 対 多
    # ManyToMany = 多 対 多
    # on_delete --> もしユーザーが削除された場合の処理、CASCADEの場合は対象のコメントも削除する

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
