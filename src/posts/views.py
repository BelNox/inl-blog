from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.

from .models import Post


def post_create(request):
    return HttpResponse("<h1>Create</h1>")



def post_detail(request):
    #instance = Post.objects.get(id=1)
    instance = get_object_or_404(Post, id=1)
    context = {
        "title": instance.title,
        "instance": instance,

    }

    return render(request, "postDetail.html", context)



def post_list(request):
    querySet = Post.objects.all()
    context = {
        "title": "List",
        "objectList": querySet,

    }


    return render(request, "index.html", context)



def post_update(request):
    return HttpResponse("<h1>Update</h1>")



def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
