from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('<uuid:user_uuid>/', views.profile, name='profil'),
    path('edit-profile/', views.edit_profile, name='edit_profile' ),
    path('follow/<uuid:follow_uuid>',views.follow, name='follow' ),
    path('follow-cancel/<uuid:follow_cancel_uuid>',views.follow_cancel, name='follow-cancel' ),
    path('<uuid:user_uuid>/follower/', views.follower_view, name='follower_view'),
    path('follback/<int:follower_id>', views.follback, name='follback'),
    path('delete_follower/<int:delete_id>', views.delete_follower, name='delete_follower'),
    path('<uuid:user_uuid>/following/', views.following_view, name='following_view'),
    path('follwing_cancel/<int:following_id>', views.following_cancel, name='following_cancel'),
    path('delete_post/<uuid:delete_post_uuid>', views.delete_post, name='delete_post')
]
