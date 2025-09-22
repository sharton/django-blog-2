from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



# Post.objects.all()
# Post.objects.get(id=1)
# Post.objects.filter()
# author = User.objects.get(username='pushkin')
# Filters :
    # contains 
    # exact =
    # startwith
    # endwith 
    # gt >
    # gte >=
    # lt < 
    # lte <=
