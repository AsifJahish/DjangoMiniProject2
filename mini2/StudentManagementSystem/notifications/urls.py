from django.urls import path
from .views import NotificationListView, CreateNotificationView, MarkNotificationReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification_list'),
    path('create/', CreateNotificationView.as_view(), name='create_notification'),
    path('<int:notification_id>/mark-read/', MarkNotificationReadView.as_view(), name='mark_notification_read'),
]
