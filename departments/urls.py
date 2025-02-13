from django.urls import path
from . import views


app_name = 'departments'

urlpatterns = [
    path('department_list/', views.DepartmentListView.as_view(), name='list'),
    path('create/', views.DepartmentCreateView.as_view(), name='add'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.DepartmentDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.DepartmentDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', views.DepartmentUpdateView.as_view(), name='update'),
]