from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .forms import userForm
from django.contrib import messages
from django.urls import reverse
from .models import Follow
from hubspace.models import Post
from django.http import HttpResponse
from hubspace.models import Reaction

# Create your views here.

User = get_user_model()

@login_required(login_url='landing:home')
def profile(request, user_uuid) : 
    user = get_object_or_404(User, uuid=user_uuid)  
    is_own_user = request.user.uuid == user_uuid
    followers = Follow.objects.filter(following = user)
    followings = Follow.objects.filter(follower = user)
    
    context = {
        'title' : 'profil',
        'viewed_user' : user, 
        'is_own_user' : is_own_user,
        'is_follow' : Follow.objects.filter(follower=request.user, following=user).exists(),
        'follower_count' : followers.count(), 
        'following_count' : followings.count(), 
        'followers' : followers, 
        'followings' : followings, 
        'posts_user' : User.objects.get(id = user.id).posts.all().order_by('-created_at'),
        'current_post' : User.objects.get(id = user.id).posts.all().count(),
        'data_likes' : [i.post.id  for i in Reaction.objects.filter(user = request.user, type = 'like')],
        'data_dislike' : [i.post.id for i in Reaction.objects.filter(user = request.user, type = 'dislike')],
    }

    return render(request, 'userProfile/profile.html', context)

def edit_profile(request) : 
    user_Form = userForm(request.POST or None, request.FILES or None , instance=request.user) 
    if request.method == 'POST' :
        if user_Form.is_valid() : 
            user_Form.save()
            messages.success(request, 'Profil berhasil diedit')
          
            return redirect('user_profile:edit_profile')
        else : 
            print('dak biso')
            print(user_Form.errors)
            
    context = {
        'title' : 'Edit profli',
        'form' : user_Form
    }
    
    return render(request, 'userProfile/edit_profile.html', context)

def follow(request, follow_uuid) : 
    following_user = get_object_or_404(User, uuid = follow_uuid)
    Follow(follower_id = request.user.id, following_id = following_user.id).save()

    return redirect(reverse('user_profile:profil', args=[follow_uuid]))

def follow_cancel(request, follow_cancel_uuid) : 
    following_user = get_object_or_404(User, uuid = follow_cancel_uuid)
    Follow.objects.get(follower_id = request.user.id, following_id = following_user.id).delete()

    return redirect(reverse('user_profile:profil', args=[follow_cancel_uuid]))
    
def follower_view(request, user_uuid) : 
    user = get_object_or_404(User, uuid = user_uuid )
    followers = Follow.objects.filter(following = user)
    followings = Follow.objects.filter(follower = user)
    context = {
        'title' : 'Pengikut',
        'viewed_user' : user,
        'followers' : followers,
        'is_own_user' : request.user == user,
        'followings_id' : set([ following.following.id for following in  followings])
    }

    return render(request, 'userProfile/follower.html', context)

def follback(request, follower_id) : 
    if request.method == 'POST' : 
        follback_user = get_object_or_404(User, id = follower_id)
        Follow(follower = request.user, following = follback_user).save()

    return HttpResponse(status = 204)

def delete_follower(request, delete_id) : 
    if request.method == 'POST' : 
        delete_user = get_object_or_404(User, id = delete_id)
        Follow.objects.get(follower = delete_user, following = request.user).delete()
    
    return HttpResponse(status = 204)

def following_view(request, user_uuid) : 
    user = get_object_or_404(User, uuid = user_uuid )
    followings = Follow.objects.filter(follower = user)
    context = {
        'title' : 'Mengikuti',
        'viewed_user' : user,
        'followings' : followings,
        'is_own_user' : user == request.user
     }
    return render(request, 'userProfile/following.html', context)

def following_cancel(request, following_id) : 
    if request.method == 'POST' :
        cancel_user = get_object_or_404(User, id = following_id)
        Follow.objects.get(following = cancel_user, follower = request.user).delete()
    return HttpResponse(status = 204)

def delete_post(request, delete_post_uuid) : 
    if request.method == 'POST' : 
        try : 
            Post.objects.get(uuid = delete_post_uuid).delete()
            messages.success(request,'Jokes berhasil dihapus !')        
        except Post.DoesNotExist : 
            messages.error(request, 'Data tidak ditemukan')

    return redirect(reverse('user_profile:profil', args=[request.user.uuid]))