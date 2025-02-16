from django.urls import path
from students import views


app_name = 'students'

urlpatterns = [
    path('student_list/', views.StudentListView.as_view(), name='list'),
    path('create/', views.StudentCreateView.as_view(), name='add'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.StudentDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update'),
]