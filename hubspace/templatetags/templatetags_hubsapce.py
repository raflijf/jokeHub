from django import template
from django.utils.timezone import now
from datetime import timedelta
from hubspace.models import Reaction, Post
from userProfile.models import Follow
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

register = template.Library()

@register.filter
def time_ago(value) : 
    elapsed_time = now() - value

    if elapsed_time < timedelta(minutes=1) :
        return 'Baru saja'
    elif elapsed_time < timedelta(hours=1) :
        return f'{elapsed_time.seconds // 60} Menit yang lalu'
    elif elapsed_time < timedelta(days=1) :
        return f'{elapsed_time.seconds // 3600} Jam yang lalu'
    elif elapsed_time < timedelta(days=8) : 
        return f'{elapsed_time.days} Hari yang lalu'
    else :
        return value.strftime('%y-%m-%d')
    

@register.filter
def count_reaction(id, type = 'like') :
    post = Post.objects.get(id = id)
    count = Reaction.objects.filter(post = post, type = type).count()
    return count

@register.filter
def count_comment(id) :
    return Post.objects.get(id = id).comment.count()

User = get_user_model()
@register.filter
def count_follow(id, type = 'followers') :
    user = get_object_or_404(User, id = id)
    if type == 'followers' :
        return user.follower.all().count()
    elif type == 'followings' :
        return user.following.all().count()     

@register.filter
def is_follow(id, my_id) :
    user = get_object_or_404(User, id = id)
    return  Follow.objects.filter(follower=my_id, following=user).exists()