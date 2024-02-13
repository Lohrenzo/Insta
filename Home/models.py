from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # return str(self.name)
        return self.name

    def get_absolute_url(self):
        # return reverse('detail', args=str(self.id))
        return reverse("home")


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, upload_to="profile")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    pic = models.ImageField(null=True, upload_to="images")
    caption = models.TextField(max_length=500, blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name="blog_posts")
    favourites = models.ManyToManyField(
        User, related_name="favourite", default=None, blank=None
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.caption) + " by " + str(self.author)

    def get_absolute_url(self):
        # return reverse('detail', args=str(self.id))
        return reverse("home")


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE
    )
    username = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    # body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s -- comment by @%s" % (self.post.caption, self.username)
