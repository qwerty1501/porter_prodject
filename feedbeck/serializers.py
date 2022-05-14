from rest_framework import serializers
from .models import Feedback
import requests

class FeedbackSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        feedback = Feedback.objects.create(
            name = validated_data['name'],
            phone = validated_data['phone'],
            poter = validated_data['poter'],
            movers = validated_data['movers'],
            dispersal = validated_data['dispersal'],
            trash = validated_data['trash'],
            description = validated_data['description']
        )
        feedback.save()
        return feedback
    
    def to_representation(self, instance):
        instance = super().to_representation(instance)
        for key,value in instance.items():
            if isinstance(value, bool):
                if value:
                    instance[key]='ДА'
                else:
                    instance[key]='НЕТ'
    
        data = {
            "text": f"Имя - {instance['name']},\n\
            Номер - {instance['phone']},\n\
            Портер - {instance['poter']},\n\
            Грузчики - {instance['movers']},\n\
            Разборка/сборка мебели - {instance['dispersal']},\n\
            Вызов мусора = {instance['trash']},\n\
            Описание - {instance['description']}",
            "chat_id": "-1001547008298"
        }
        r = requests.post('https://api.telegram.org/bot5315638799:AAFZgdZU3izLbWTNsl078A39FCp8SRrFKv4/sendMessage', json=data)

        return instance
    class Meta:
        model = Feedback
        fields = '__all__'
