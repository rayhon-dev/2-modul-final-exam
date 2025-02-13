from django.urls import path
from . import views


app_name = 'groups'

urlpatterns = [
    path('group_list/', views.GroupListView.as_view(), name='list'),
    path('create/', views.GroupCreateView.as_view(), name='add'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.GroupDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.GroupDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.GroupUpdateView.as_view(), name='update'),
]