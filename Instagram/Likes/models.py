import uuid
from django.db import models

from Profile.models import Profile
from Posts.models import Posts

# Create your models here.


# Like Model
class Likes(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return f"{self.profile} liked {self.post}"
