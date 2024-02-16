import random

from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase

from main import views
from main.models import Game
from main.serializers import NewGameSerializer
from settings.settings import MIN_WIDTH, MAX_WIDTH, MIN_HEIGHT, MAX_HEIGHT


class TestMain(APITestCase):
    """Test for Main application"""

    def setUp(self):
        super().setUp()
        self.data_success = {
            'width': 10,
            'height': 10,
            'mines_count': 10
        }
        max_count = MAX_WIDTH * MAX_HEIGHT
        self.data_errors = [{
            'width': random.randint(MIN_WIDTH, MAX_WIDTH) if i == 0 else random.randint(MIN_WIDTH, MAX_WIDTH + 100),
            'height': random.randint(MIN_HEIGHT, MAX_HEIGHT) if i == 1 else random.randint(MIN_HEIGHT,
                                                                                           MAX_HEIGHT + 100),
            'mines_count': random.randint(1, max_count - 1) if i == 2 else random.randint(max_count, max_count + 100)
        } for i in range(3)]
        self.game = Game.objects.create(**self.data_success)

    def test_new_game(self):
        """Test new game"""
        url, view = reverse('main:new_game'), views.NewGameAPIView
        for data_error in self.data_errors:
            response = self.client.post(path=url, data=data_error)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.post(path=url, data=self.data_success)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        game_id = response.data.get('game_id')
        game = Game.objects.get(game_id=game_id)
        self.assertEqual(resolve(url).func.view_class, view)
        self.assertEqual(self.get_serialized_data(game, view.serializer_class), response.data)

    def test_turn(self):
        """Test turn"""
        data = {
            'game_id': self.game.game_id,
            'col': self.game.height,
            'row': self.game.width
        }
        url, view = reverse('main:turn_game'), views.TurnGameAPIView
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data['col'], data['row'] = data['col'] - 1, data['row'] - 1
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(resolve(url).func.view_class, view)
        game = Game.objects.get(game_id=self.game.game_id)
        self.assertEqual(self.get_serialized_data(game, NewGameSerializer), response.data)

    @staticmethod
    def get_serialized_data(instance, serializer_class):
        """Serialized data return method"""
        return serializer_class(instance).data
