from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.


def post_create(request):
    return HttpResponse("Create")


def post_detail(request):
    instance = get_object_or_404(Post, id = 3)
    # instance = Post.objects.get(id = 1)
    context = {
        "title": instance.title,
        "instance" : instance,
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()
    context = {
        "Title": "It's working",
        "object_list": queryset,
        }

    # if request.user.is_authenticated:
    #     context = {
    #         "Title": "List is"
    #     }
    # else:
    #     context = {
    #         "Title": "List is not"
    #     }
    return render(request,"index.html",context)


def post_update(request):
    return HttpResponse("Update")


def post_delete(request):
    return HttpResponse("Delete")