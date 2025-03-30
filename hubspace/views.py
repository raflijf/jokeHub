from django.shortcuts import render, redirect
from .forms import postForm, commentForm, searchForm
from .models import Post, Category, Reaction, Comment
from django.contrib import messages
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.urls import reverse
from accounts.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request) : 
    if request.user.is_authenticated : 
        context = {
            'title' : 'beranda',
            'posts' : Post.objects.all().order_by('-created_at'),
            'data_likes' : [i.post.id  for i in Reaction.objects.filter(user = request.user, type = 'like')],
            'data_dislike' : [i.post.id for i in Reaction.objects.filter(user = request.user, type = 'dislike')],
             
        }   
  
        return render(request, 'hubspace/homepage.html', context) 
    else : 
        return redirect('landing:home')

@login_required(login_url='accounts:signin')
def create(request) : 
    form = postForm(request.POST or None)
    listCategory = Category.objects.all()
    context = {
        'title' : 'Buat',
        'form' : form,
        'list_category' : listCategory
    }

    if form.is_valid() : 
        content = form.cleaned_data.get('content')
        category = request.POST.get('category')
        Post(
            content = content, 
            category = Category.objects.get(name = category),
            user = request.user
        ).save()
        messages.success(request, 'Berhasil menambahkan jokes baru !')
        return redirect('hubspace:homepage')
            
    return render(request, 'hubspace/create.html', context)

def addNewCategory(request) : 
    if request.method == 'POST' : 
        try :
            value = request.POST.get('name_category')
            Category(name=value.lower()).save()

        except IntegrityError : 
            pass

    return redirect('hubspace:create')

def reaction(request, reaction_type, post_id) :
    if request.method == 'POST' :
        try :
            post = Post.objects.get(id = post_id)
            Reaction(user = request.user, post = post, type = reaction_type ).save()
        except IntegrityError :
            pass

    return HttpResponse(status = 204)

def deltete_reaction(request, reaction_type, post_id ) :
    if request.method == 'POST':
        post = Post.objects.get(id = post_id)
        Reaction.objects.get(user = request.user, post = post, type = reaction_type).delete()
    return HttpResponse(status = 204)

def comment(request, post_uuid ) :
    post = Post.objects.get(uuid = post_uuid)
    comment_form = commentForm(request.POST or None)
    context = {
        'title' : 'Komentar',
        'post' : post,
        'data_likes' : [i.post.id  for i in Reaction.objects.filter(user = request.user, type = 'like')],
        'data_dislike' : [i.post.id for i in Reaction.objects.filter(user = request.user, type = 'dislike')],
        'commentform' : comment_form,
        'comments' : post.comment.all().order_by('-created_at'),
        'count_commnent' : post.comment.count()
        
    }
    if comment_form.is_valid() :
        Comment(
            user = request.user,
            post = post,
            content = comment_form.cleaned_data['content']
        ).save()
        return redirect(reverse('hubspace:comment', args=[post_uuid]))


    return render(request, 'hubspace/comment.html', context)

def delete_comment(request, id_comment) : 
    if request.method == 'POST' :
        request.user.comment.get(id = id_comment).delete()

    return HttpResponse(status = 204)

@login_required(login_url='accounts:signin')
def search(request) :
    context = {
        'categories' : Category.objects.all(),
        'post_categories' : {},
        'users' : {},
        'search' : searchForm,
        'data_likes' : [i.post.id  for i in Reaction.objects.filter(user = request.user, type = 'like')],
        'data_dislike' : [i.post.id for i in Reaction.objects.filter(user = request.user, type = 'dislike')],
    }

    if 'search' in request.GET :
        context['search'] = searchForm(initial={'search' : request.GET['search']})
        post = Post.objects.filter(content__icontains = request.GET['search'])
        if post.exists() :
            context['post_categories'] = post
        else : 
            category =  Category.objects.filter(name = request.GET.get('search')).first()
            post = Post.objects.filter(category = category) 
            context['post_categories'] = post if post.exists() else 'not exists'

        users = User.objects.filter(username__icontains = request.GET['search'])
        context['users'] = users if users.exists() else 'not exists'

    elif request.GET :
        category = Category.objects.get(name = request.GET['category'])
        post_catgories = Post.objects.filter(category = category)
        context['post_categories'] = post_catgories if post_catgories.exists() else 'not exists'
        
    else :
        context['post_categories'] = False
        context['users']  = False

    return render(request, 'hubspace/search.html', context)


