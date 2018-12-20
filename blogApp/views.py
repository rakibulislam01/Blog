from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def post_create(request):
    return HttpResponse("Create")


def post_detail(request):
        return HttpResponse("Detail")


def post_list(request):
    context = {
        "Title": "List"
    }
    return render(request,"index.html",context)


def post_update(request):
    return HttpResponse("Update")


def post_delete(request):
    return HttpResponse("Delete")