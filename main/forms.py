from django import forms
from django.core.exceptions import ValidationError

from main.models import Game
from settings.settings import MIN_WIDTH, MIN_HEIGHT, MAX_WIDTH, MAX_HEIGHT


class GameAdminForm(forms.ModelForm):
    """Game Admin Form"""
    width = forms.IntegerField(min_value=MIN_WIDTH, max_value=MAX_WIDTH, initial=MIN_WIDTH, required=True)
    height = forms.IntegerField(min_value=MIN_HEIGHT, max_value=MAX_HEIGHT, initial=MIN_HEIGHT, required=True)
    mines_count = forms.IntegerField(min_value=3, initial=3, required=True)

    class Meta:
        model = Game
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        width, height, mines_count = data.get('width'), data.get('height'), data.get('mines_count')
        max_mines_count = width * height
        if width < 2 or width > 30:
            raise ValidationError(f'ширина поля должна быть не менее {MIN_WIDTH} и не более {MAX_WIDTH}')
        if height < 2 or height > 30:
            raise ValidationError(f'высота поля должна быть не менее {MIN_HEIGHT} и не более {MAX_HEIGHT}')
        if mines_count >= max_mines_count or mines_count < 1:
            raise ValidationError(f'количество мин должно быть не менее 1 и не более {max_mines_count - 1}')
        return data
