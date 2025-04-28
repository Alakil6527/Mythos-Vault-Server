import random
import string

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, User

def generate_random_username():
    
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"mythos_{random_string}"

@receiver(post_save, sender=User)
# sender and **kwargs for future work sending email notification
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        username = generate_random_username()

        while UserProfile.objects.filter(username=username).exists():
            username = generate_random_username()

        UserProfile.objects.create(user=instance, username=username)
