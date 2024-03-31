import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Profile
class Profile(models.Model):
    """
    Model representing a user profile.

    Attributes:
        user (User): The user associated with this profile.
        profile_picture (Image): The profile picture of the user.
        username (str): The username of the user. It must be unique.
        name (str): The name of the user.
        bio (str): A short biography or description of the user.
        website (str): The website URL of the user.
        created_at (DateTime): The date and time when the profile was created.
        updated_at (DateTime): The date and time when the profile was last updated.
        id (UUID): The primary key and universally unique identifier for the profile.

    Methods:
        __str__(): Returns a string representation of the profile.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    profile_picture = models.ImageField(
        upload_to="media/profile_images/", null=True, blank=True
    )
    username = models.CharField(null=False, blank=False, unique=True, max_length=50)
    name = models.CharField(null=True, blank=True, max_length=100)
    bio = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    def __str__(self):
        """
        String representation of the model instance.
        """

        return self.username


# Following Model
class Following(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    following = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="following_profile"
    )


# Follower Model
class Follower(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
    follower = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="follower_profile"
    )
