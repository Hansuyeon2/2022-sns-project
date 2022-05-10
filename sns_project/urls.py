from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showmain, name="showmain"),
    path('show/', views.showintroduce, name="showintroduce"),
    path('<int:id>',views.detail, name="detail"),
    path('new/',views.new, name="new"),
    path('create/',views.create, name="create"),
]
