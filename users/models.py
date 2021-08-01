from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.is_active = False
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    status = models.CharField(max_length=10, default="Draft", editable=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = 'Profilo'
        verbose_name_plural = 'Profili'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # instance.is_active = False
        profile = Profile.objects.create(user=instance)
    instance.profile.save()