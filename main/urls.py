from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('<int:id>', detail, name="detail"),
    path('buy/new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<int:id>', edit,name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>',delete,name="delete"),
    path('<str:post_id>/create_comment', create_comment, name="create_comment"),
    path('<str:comment_id>/edit_comment', edit_comment, name="edit_comment"),
    path('<str:comment_id>/update_comment', update_comment, name="update_comment"),
    path('<str:comment_id>/delete_comment', delete_comment, name="delete_comment"),
]
