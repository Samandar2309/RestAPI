from django.urls import path
from .views import TodoList, TodoCreate, TodoRetrieve, TodoUpdate, TodoDelete
urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('/create/', TodoCreate.as_view(), name='todo-create'),
    path('/<int:pk>/', TodoRetrieve.as_view(), name='todo-retrieve'),
    path('/<int:pk>/update/', TodoUpdate.as_view(), name='todo-update'),
    path('/<int:pk>/delete/', TodoDelete.as_view(), name='todo-delete'),
]