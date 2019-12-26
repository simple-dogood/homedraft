from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogz = Blog.objects.order_by('-pub_date')
    return render(request, 'blog/allblogs.html',{'blogz':blogz})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog/detail.html', {'blog':blog_detail})
