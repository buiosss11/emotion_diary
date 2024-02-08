from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    page = request.GET.get("page")

    paginator = Paginator(posts, 4)
    try:
        page_obj = paginator.page(page)
        
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)
    
    context = {"posts": posts,"page_obj":page_obj,"paginator":paginator}
    return render(request, "posts/post_list.html", context)
    



def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {"post": post}

    return render(request, "posts/post_detail.html", context)


def post_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect("post-detail", post_id=new_post.id)
    else:
        post_form = PostForm()
        return render(request, "posts/post_create.html", {"form": post_form})


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("post-list")
    else:
        return render(request, "posts/post_delete.html", {"post": post})


# def post_update(request):

#     return


    