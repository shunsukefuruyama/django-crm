from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# for authentication, etc. one-to-one relationship with Agent class
# creating custom user class is highly recommended
# User = get_user_model()

class User(AbstractUser):
    pass

class Lead(models.Model):
    # SOURCE_CHOICES = (
    #     # (Name in DB, Display Name)
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter')
    # )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)
    
    # with double quotations, no need to move Agent class up in this doc
    # models.CASCADE ... If Agent class is deleted, Lead will also get deleted. null=True must be set.
    # models.SET_NULL ... null=True is required
    # models.SET_DEFAULT ... default value must be set
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        # refer to user table that is in one-to-one relationship
        return self.user.username