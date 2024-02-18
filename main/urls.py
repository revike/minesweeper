from django.urls import path

from main.views import NewGameAPIView, TurnGameAPIView

app_name = 'main'

urlpatterns = [
    path('new', NewGameAPIView.as_view(), name='new_game'),
    path('turn', TurnGameAPIView.as_view(), name='turn_game'),
]
