import uuid

from django.db import models
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

from main.services import create_field, create_bomb_field
from settings.settings import MIN_WIDTH, MAX_WIDTH, MIN_HEIGHT, MAX_HEIGHT


class Game(models.Model):
    """Game Model"""
    game_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='game_id')
    width = models.IntegerField(verbose_name='width', default=10)
    height = models.IntegerField(verbose_name='height', default=10)
    mines_count = models.IntegerField(verbose_name='mines_count', default=5)
    completed = models.BooleanField(verbose_name='completed', default=False)

    class Meta:
        verbose_name = 'game'
        verbose_name_plural = 'games'

    def __str__(self):
        return f'{self.game_id}'

    def save(self, *args, **kwargs):
        if self.width < 2 or self.width > 30:
            raise ValidationError(f'ширина поля должна быть не менее {MIN_WIDTH} и не более {MAX_WIDTH}')
        if self.height < 2 or self.height > 30:
            raise ValidationError(f'высота поля должна быть не менее {MIN_HEIGHT} и не более {MAX_HEIGHT}')
        max_mines_count = self.width * self.height
        if self.mines_count >= max_mines_count or self.mines_count < 1:
            raise ValidationError(f'количество мин должно быть не менее 1 и не более {max_mines_count - 1}')
        super().save(*args, **kwargs)


class GameField(models.Model):
    """Game Field Model"""
    game_field = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='game', verbose_name='game')
    field = models.JSONField(verbose_name='field', null=True)
    field_bomb = models.JSONField(verbose_name='bomb field', null=True)

    class Meta:
        verbose_name = 'game field'
        verbose_name_plural = 'game fields'

    def __str__(self):
        return f'{self.game_field}'

    @staticmethod
    @receiver(models.signals.post_save, sender=Game)
    def create_user_profile(sender, instance, created, **kwargs):
        if created and sender == Game and kwargs:
            game_field = GameField.objects.create(game_field=instance)
            width, height, mines_count = instance.width, instance.height, instance.mines_count
            game_field.field = create_field(width, height)
            game_field.field_bomb = create_bomb_field(width, height, game_field.field, mines_count)
            game_field.save()
