from django.urls import  path
from .views import EmpView,DepView

urlpatterns = [
    path('employees/',EmpView.as_view()),
    path('employees/<int:pk>/',EmpView.as_view()),
    path('department/',DepView.as_view()),
    path('department/<int:pk>/',DepView.as_view())
]