import uuid

from django.db import models


# Create your models here.
class Users(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    referal_adress = models.CharField(max_length=150)
    user_img = models.ImageField(default=None)
    user_skin = models.ImageField(default=None)
    user_somus = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.user_name)


class Posts(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=150)
    post_img = models.ImageField()
    post_text = models.TextField()
    post_date = models.DateField()

    def __str__(self) -> str:
        return str(self.post_title)


class PostLike(models.Model):
    like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class Comments(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateField()


class CommentLike(models.Model):
    like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
