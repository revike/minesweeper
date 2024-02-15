from drf_spectacular.utils import extend_schema
from rest_framework import generics, status

from main.schemas import response_new_game
from main.serializers import NewGameSerializer


class NewGameAPIView(generics.CreateAPIView):
    """New Game API View"""
    serializer_class = NewGameSerializer

    @extend_schema(summary='New game', description='Начало новой игры', responses=response_new_game)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response
