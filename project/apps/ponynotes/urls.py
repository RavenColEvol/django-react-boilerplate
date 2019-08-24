from django.urls import path
from . import views
urlpatterns = [
    path('api/note/', views.NoteView.as_view() ),
]