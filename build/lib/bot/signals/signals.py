from django.db.models.signals import post_save
from django.dispatch import receiver
from bot.models.competition import Competition


@receiver(post_save, sender=Competition)
def my_model_post_save(sender, instance, **kwargs):
    print(f"Signal: {instance.name} saqlandi!")
