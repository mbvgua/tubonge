from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Post

# Create your views here.

# list all the posts published
def post_list(request):
    posts = Post.published.all()

    return render (request, 
                   'blog/post/list.html', 
                   {'posts':posts},)

# list a aprticular post in detail
def post_detail(request, id):
#     try:
#         posts = Post.published.get(id=id)
#     except:
#         raise Http404('Post does not exist')
    
#     return render(request,
#                   'blog/post/detail.html',
#                   {'posts':posts},)
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post':post},)
