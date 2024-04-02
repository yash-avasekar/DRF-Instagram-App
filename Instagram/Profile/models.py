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
        profile_picture (ImageField): The profile picture of the user.
        username (str): The unique username of the user.
        name (str): The name of the user.
        bio (str): A short biography or description of the user.
        website (str): The website URL of the user.
        created_at (DateTimeField): The date and time when the profile was created.
        updated_at (DateTimeField): The date and time when the profile was last updated.
        id (UUIDField): The universally unique identifier for the profile.

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
    website = models.URLField(null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    def __str__(self):
        """
        Returns a string representation of the profile.

        Returns:
            str: The username of the profile.
        """

        return self.username


class Relation(models.Model):
    """
    Represents a relationship between two profiles, indicating one profile follows another.

    Attributes:
        following (ForeignKey): The profile being followed.
        follower (ForeignKey): The profile following another.

    Meta:
        unique_together (list of str): Ensures each combination of following and follower is unique.

    Methods:
        __str__(self): Returns a string representation of the relation.
    """

    following = models.ForeignKey(Profile, models.CASCADE, related_name="follower")
    follower = models.ForeignKey(Profile, models.CASCADE, related_name="following")
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    class Meta:
        unique_together = ["following", "follower"]

    def __str__(self):
        """
        Returns a string representation of the relation.

        Returns:
            str: A string indicating the follower is following the following.
        """
        return f"{self.follower} is following {self.following}"
