from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        # form.cleaned_data.get("")
        instance.save()
        messages.success(request, "Successfully create")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request,"Not Successfully create")
    # if request.method == "POST":
    # print(request.POST)
    # request.POST.get("content")
    # title = request.POST.get("title")
    # Post.objects.create(title = title)

    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    # instance = Post.objects.get(id = 1)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset_list = Post.objects.all()  # .order_by("-timestamp")
    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    queryset = paginator.get_page(page)

    context = {
        "Title": "Post List",
        "object_list": queryset,
        "page_request_var": page_request_var,
    }

    # if request.user.is_authenticated:
    #     context = {
    #         "Title": "List is"
    #     }
    # else:
    #     context = {
    #         "Title": "List is not"
    #     }
    return render(request, "post_list.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        # form.cleaned_data.get("")
        instance.save()
        messages.success(request, "Successfully Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, "Not Successfully Saved")

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }

    return render(request, "post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Delete")

    return redirect("list")
