from django.urls import path

from main.views import NewGameAPIView, TurnGameAPIView

app_name = 'main'

urlpatterns = [
    path('api/new', NewGameAPIView.as_view(), name='new_game'),
    path('api/turn', TurnGameAPIView.as_view(), name='turn_game'),
]
