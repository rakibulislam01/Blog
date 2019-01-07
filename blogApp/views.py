from urllib.parse import quote_plus
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from django.db.models import Q
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        # form.cleaned_data.get("")
        instance.user = request.user
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
    instance        = get_object_or_404(Post, id=id)

    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    # instance = Post.objects.get(id = 1)
    share_string    = quote_plus(instance.content)

    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    today = timezone.now().date()
    queryset_list    = Post.objects.active()  # .order_by("-timestamp") # filter(draft=False).filter(publish__lte=timezone.now())

    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

    query            = request.GET.get("q")

    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator        = Paginator(queryset_list, 5) # Show 25 contacts per page
    page_request_var = "page"
    page             = request.GET.get(page_request_var)
    queryset         = paginator.get_page(page)

    context = {
        "Title": "Post List",
        "object_list": queryset,
        "page_request_var": page_request_var,
        "today" : today
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

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance    = get_object_or_404(Post, id=id)
    form        = PostForm(request.POST or None, request.FILES or None, instance=instance)

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

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Delete")

    return redirect("list")
