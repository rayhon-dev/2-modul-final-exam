from django.urls import path
from . import views


app_name = 'subjects'

urlpatterns = [
    path('subject_list/', views.SubjectListView.as_view(), name='list'),
    path('create/', views.SubjectCreateView.as_view(), name='add'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.SubjectDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.SubjectDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.SubjectUpdateView.as_view(), name='update'),
]