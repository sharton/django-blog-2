from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("post_list")

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             form.save_m2m()
#             return redirect('post_list')
#     else:
#         form = PostForm()
#         return render(request, 'blog/post_form.html', {'form': form})


# def post_update(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             # post = form.save(commit=False)
#             # post.author = request.user
#             # post.save()
#             form.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#         return render(request, 'blog/post_form.html', {'form': form})

# C_R_UD

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
