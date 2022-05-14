from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from rest_framework import generics

from .serializers import FeedbackSerializers
from .models import Feedback

import telegram # this is from python-telegram-bot package
import requests


class FeedbackCreateListView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializers
    queryset = Feedback.objects.all()

    def post_event_on_telegram(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        print(serializer)
        return super().create(request)
    

class FeedbackDeleteView(generics.DestroyAPIView):
    serializer_class = FeedbackSerializers()
    queryset = Feedback.objects.all()
