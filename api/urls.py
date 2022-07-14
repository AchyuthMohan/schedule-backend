from django.urls import path
from .views import todo_list,todo_detail
urlpatterns = [
    path('todos/', todo_list),
    path('todo_detail/<int:pk>/',todo_detail),
]
