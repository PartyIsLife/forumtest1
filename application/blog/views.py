from django.shortcuts import render

from blog.models import Post


def post_list(request):
    posts = Post.objects.filter().order_by()
    return render(request,'blog/post_list.html',{'posts':posts})
# Create your views here.
