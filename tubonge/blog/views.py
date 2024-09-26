from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail
from tubonge.settings import EMAIL_HOST_USER


# Create your views here.
# list all the posts published
def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # if page request is not an integer return the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page request is out of range, return last page
        posts = paginator.page(paginator.num_pages)

    return render (request, 
                   'blog/post/list.html', 
                   {'posts':posts},)

# list a prticular post in detail
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

# sharing the posts via email
def post_share(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    sent = False
    
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        # if input within form is valid
        if form.is_valid():
            cd = form.cleaned_data      #key:value pairs of input
            post_url = request.build_absolute_uri( post.get_absolute_url() )
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n"\
                    f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, EMAIL_HOST_USER, [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request,
                  'blog/post/share.html',
                  {'post':post, 'form':form, 'sent':sent})
