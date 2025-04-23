from django.urls import path
from .views import MoodListView, MoodDetailView
from .views import MoodCreateView
from .views import MoodUpdateView
from .views import MoodDeleteView

urlpatterns = [
    path('', MoodListView.as_view(), name='mood_list'),
    path('<int:pk>/', MoodDetailView.as_view(), name='mood_detail'),
    path('new/', MoodCreateView.as_view(), name='mood_new'),
    path('<int:pk>/edit/', MoodUpdateView.as_view(), name='mood_edit'),
    path('<int:pk>/delete/', MoodDeleteView.as_view(), name='mood_delete'),

]