from rest_framework import status

from main.serializers import NewGameSerializer, NewGameDummySerializer

response = {
    status.HTTP_200_OK: NewGameSerializer,
    status.HTTP_400_BAD_REQUEST: NewGameDummySerializer,
}
