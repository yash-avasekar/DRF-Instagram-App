import uuid
from django.db import models
from Profile.models import Profile


# Create your models here.


# Posts Model
class Posts(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_picture = models.ImageField(
        upload_to="media/posts/", null=True, blank=True
    )
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.description
