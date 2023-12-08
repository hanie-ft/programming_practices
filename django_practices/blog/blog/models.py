from gettext import translation
from django.db import models
from django.utils import timezone

# TODO write all of your code here...


class BaseModel(models.Model):
    date_created = models.DateTimeField(db_index=True, default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class BlogPost(BaseModel):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.title}] - [date: {self.date_created}] \
            -[author: {self.author}]: {self.body}"

    def copy(self) -> int:
        new_blog = BlogPost.objects.get(id=self.id)
        new_blog.pk = None
        new_blog._state.adding = True
        new_blog.date_created = timezone.now()
        new_blog.save()

        # copy comments
        comments = self.comment_set.all()
        for comment in comments:
            comment.blog_post = new_blog
            comment.pk = None
            comment._state.adding = True
            comment.save()

        return new_blog.id


class Comment(BaseModel):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f" [id: {self.pk}] {self.text} {self.blog_post}"
