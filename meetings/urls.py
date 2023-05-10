from django.urls import path

from . import views

urlpatterns = [
    path('meeting/<int:id>', views.meeting_detail, name = "meeting_detail"),
    path('rooms',views.room_list, name = "room_list"),
    path('new', views.new, name = "new"),
]