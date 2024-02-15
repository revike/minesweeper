from django.urls import path

from main.views import NewGameAPIView

app_name = 'main'

urlpatterns = [
    path('api/new', NewGameAPIView.as_view(), name='new_game'),
]
