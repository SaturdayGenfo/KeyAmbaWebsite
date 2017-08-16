from django.shortcuts import render
from models import Post, Comment
from random import randint
from forms import CommentForm, ProverbForm

def home(request):
    n = Post.objects.count()
    p_id = randint(1, n)
    post = Post.objects.get(id=p_id)
    next = p_id + 1
    if next > n:
        next = -1
    prev = p_id -1
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            poster = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            C = Comment()
            C.post = post
            C.poster = poster
            C.text = comment
            C.save()
            
    else:
        form = CommentForm()
    return render(request, "home.html", {"id": p_id, "post": post.saying, "description": post.description, "prev":prev, "next":next, "form":form, "comments":comments})

def show(request, id):
    n = Post.objects.count()
    post = Post.objects.get(id=id)
    next = int(id) + 1
    if next > n:
        next = -1
    prev = int(id) -1

    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            poster = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            C = Comment()
            C.post = post
            C.poster = poster
            C.text = comment
            C.save()
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, "home.html", {"id": id,"post": post.saying, "description": post.description, "prev":prev, "next":next, "form":form, "comments":comments})


def contribute(request):
    eval = True
    if request.method == 'POST':
        form = ProverbForm(request.POST)
        if form.is_valid():
            proverb = form.cleaned_data['proverb']
            desc = form.cleaned_data['description']
            p = Post()
            p.saying = proverb
            p.description = desc
            p.save()
            eval = False
    else:
        form = ProverbForm()
    return render(request, "contribute.html", {'eval': eval, 'form': form})

