import uuid

from django.db import models


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    referal_adress = models.CharField(max_length=150)
    user_img = models.ImageField(default=None)
    user_skin = models.ImageField(default=None)
    user_somus = models.IntegerField(default=0)
    user_slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return str(self.user_name)


class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=150)
    post_img = models.ImageField()
    post_text = models.TextField()
    post_date = models.DateField()

    def __str__(self) -> str:
        return str(self.post_title)


class PostLike(models.Model):
    like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateField()


class CommentLike(models.Model):
    like_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)