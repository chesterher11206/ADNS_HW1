from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('message/<int:pk>/delete/', views.message_delete, name='message_delete')
]