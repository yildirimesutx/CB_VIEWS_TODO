from django.urls import path
from .views import Home, TodoList, TodoCreate,TodoUpdate, TodoDelete 


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("list/", TodoList.as_view(), name="list"),
    path("add/", TodoCreate.as_view(), name= "add"),
    path("update/<int:pk>/", TodoUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", TodoDelete.as_view(), name="delete")


]
