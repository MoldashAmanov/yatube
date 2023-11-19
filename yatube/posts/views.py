from django.shortcuts import render

from .models import Post

from django.http import HttpResponse

def index(request):
    latest = Post.objects.order_by("-pub_date")[:10]
    output = []
    for i in latest:
        output.append(i.text)
    return HttpResponse("\n".join(output))

