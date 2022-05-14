from django.urls import path
from .views import FeedbackCreateListView, FeedbackDeleteView


urlpatterns = [
    path('feedback/', FeedbackCreateListView.as_view()),
    path('feedback/delete/<int:pk>/', FeedbackDeleteView.as_view()),
]