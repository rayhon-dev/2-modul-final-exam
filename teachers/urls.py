from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('teachers_list/', views.TeacherListView.as_view(), name='list'),
    path('create/', views.TeacherCreateView.as_view(), name='add'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.TeacherDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.TeacherUpdateView.as_view(), name='update'),
]