from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post

# Create your views here.

# list all the posts published
class PostListView(ListView):
    queryset = Post.published.all()
    print(f'This is it: {queryset}')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# list a aprticular post in detail
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post':post},)
