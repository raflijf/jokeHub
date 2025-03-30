from django.urls import path
from . import views

app_name = 'hubspace'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create, name='create'),
    path('add-new-category/', views.addNewCategory, name='new_category'),
    path('reaction/<str:reaction_type>/<int:post_id>/', views.reaction, name='reaction'),
    path('delete-reaction/<str:reaction_type>/<int:post_id>', views.deltete_reaction, name='delete_reaction'),
    path('comment/<uuid:post_uuid>', views.comment, name="comment"),
    path('delete-comment/<int:id_comment>/', views.delete_comment, name='delete_comment'),
    path('search/', views.search, name='search'),
]
