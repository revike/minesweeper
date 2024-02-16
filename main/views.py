from uuid import UUID

from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.response import Response

from main.models import Game
from main.schemas import response
from main.serializers import NewGameSerializer, TurnSerializer
from main.services import check_uuid, get_game_data


class NewGameAPIView(generics.CreateAPIView):
    """New Game API View"""
    serializer_class = NewGameSerializer

    @extend_schema(summary='New game', description='Начало новой игры', responses=response)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response


class TurnGameAPIView(generics.CreateAPIView):
    """Turn API View"""
    serializer_class = TurnSerializer

    @extend_schema(summary='Turn game', description='Ход пользователя', responses=response)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        response_data = {'error': 'некорректный формат идентификатора'}
        response_status = status.HTTP_400_BAD_REQUEST
        game_id = data.get('game_id')
        if check_uuid(game_id):
            game = Game.objects.filter(game_id=game_id).first()
            response_data['error'] = f'игра с идентификатором {game_id} не была создана или устарела (неактуальна)'
            if game:
                col, row = data.get('col'), data.get('row')
                response_data['error'] = 'ошибка разбора входных данных'
                if isinstance(col, int) and isinstance(row, int):
                    response_data['error'] = f'ряд должен быть неотрицательным и менее высоты {game.height}'
                    if 0 <= row < game.height:
                        response_data['error'] = f'колонка должна быть неотрицательной и менее ширины {game.width}'
                        if 0 <= col <= game.width:
                            game_obj = get_game_data(game, col, row)
                            response_data = NewGameSerializer(game_obj).data
                            response_status = status.HTTP_200_OK
        return Response(response_data, response_status)
