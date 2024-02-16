from rest_framework import serializers

from main.models import Game


class NewGameDummySerializer(serializers.Serializer):
    """New Game Dummy Serializer"""
    error = serializers.StringRelatedField(default='Произошла непредвиденная ошибка')


class NewGameSerializer(serializers.ModelSerializer):
    """New Game Serializer"""
    completed = serializers.BooleanField(read_only=True)
    width = serializers.IntegerField(default=10)
    height = serializers.IntegerField(default=10)
    mines_count = serializers.IntegerField(default=10)
    field = serializers.JSONField(read_only=True, default=[[' ']])

    class Meta:
        model = Game
        fields = ['game_id', 'width', 'height', 'mines_count', 'field', 'completed']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['field'] = instance.game.field
        return representation


class TurnSerializer(serializers.Serializer):
    """Turn Serializers"""
    game_id = serializers.UUIDField(required=True)
    col = serializers.IntegerField(required=True)
    row = serializers.IntegerField(required=True)
