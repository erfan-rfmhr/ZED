import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel

User = get_user_model()


class Topic(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=32, verbose_name=_('topic name'))

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")
        db_table = "Topic"

    def __str__(self):
        return self.name


class Post(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(verbose_name=_('post content'))
    image = models.ImageField(verbose_name=_('post image'), upload_to="post_photos/", blank=True, null=True)
    like_count = models.IntegerField(verbose_name=_('post like count'), default=0)
    comment_count = models.IntegerField(verbose_name=_('post comment count'), default=0)
    author = models.ForeignKey(
        User,
        verbose_name=_('post author'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    topic = models.ForeignKey(
        Topic,
        verbose_name=_('post topic'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        db_table = "Post"

    def __str__(self):
        content = str(self.content).split()[:5]
        content = ' '.join(content)
        return f'{self.author} | {content}'


class Comment(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField(verbose_name=_('comment content'))
    like_count = models.IntegerField(verbose_name=_('comment like count'), default=0)
    commenter = models.ForeignKey(
        User,
        verbose_name=_('commenter'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    post = models.ForeignKey(
        Post,
        verbose_name=_('comment post'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        db_table = "Comment"

    def __str__(self):
        content = str(self.content).split()[:5]
        content = ' '.join(content)
        return f'{self.commenter} | {content}'


class Repost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(
        Post,
        verbose_name=_('reposted post'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    reposter = models.ForeignKey(
        User,
        verbose_name=_('reposter'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Repost")
        verbose_name_plural = _("Reposts")
        db_table = "Repost"

    def __str__(self):
        return f'{self.reposter} -> {self.post}'
