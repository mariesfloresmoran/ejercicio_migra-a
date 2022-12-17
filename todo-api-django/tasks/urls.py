"""from rest_framework.routers import DefaultRouter
from .views import TaskView

#vamos a instaciar para luego poder crear las rutas 
router = DefaultRouter()

router.register("todo", TaskView, basename="todo") #esto es para poder crear las rutas"""
from django.urls import path, re_path, include
from .views import TodoView, TodoViewDetail
from versioned_todo.v3.router import api_urlpatterns as api_v3
#from versioned_todo.v4.router import api_urlpatterns as api_v4

urlpatterns = [
    path("todo/", TodoView.as_view(), name="todo"),
    path("todo/<id>/", TodoViewDetail.as_view(), name="todo-detail"),
    re_path(r'^api/v3/', include(api_v3)),
    #re_path(r'^api/v4/', include(api_v4)),
]