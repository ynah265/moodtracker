from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('moods/', views.MoodListView.as_view(), name='mood_list'),
    path('moods/new/', views.MoodCreateView.as_view(), name='mood_new'),
    path('moods/<int:pk>/', views.MoodDetailView.as_view(), name='mood_detail'),
    path('moods/<int:pk>/edit/', views.MoodUpdateView.as_view(), name='mood_edit'),
    path('moods/<int:pk>/delete/', views.MoodDeleteView.as_view(), name='mood_delete'),
]
