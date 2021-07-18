from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class DayPlans(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    date = models.DateField('Date') #max_length, min_length, default
    plan = models.TextField('Text', max_length=2048)

    def __str__(self):
        return self.plan

    def get_absolute_url(self):
        return '/myplans'

    class Meta:
        verbose_name = 'День и план'
        verbose_name_plural = 'Дни и планы'

class Letters(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    letter = models.TextField('Text', max_length=2048)

    def __str__(self):
        return f'{self.letter}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'

class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.BooleanField('theme', default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(author=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()