from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.StringRelatedField()  # Display recipient username

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'title', 'message', 'is_read', 'created_at']

class CreateNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['recipient', 'title', 'message']
