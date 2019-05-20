from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from posts.forms import PostForm
from posts.models import Post


def latest_posts(request):
    #Recuperar los ultimos post de la base de datos
    posts = Post.objects.all().order_by('-modification_date')

    #Creamos el contexto
    context = {'latest_posts': posts[:6]}

    #Crear repuesta HTML con los posts
    html = render(request, 'posts/lastest.html', context)

    #Devolver la respueste HTTP
    return  HttpResponse(html)


def post_detail(request, pk):
    try:

        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return HttpResponseNotFound()

    #Crear un contexto para pasar la informacion a plantilla
    context = {'post': post}

    #Renderiza plantilla
    html = render(request,'posts/detail.html', context)

    #devolver respuesta HTTP
    return HttpResponse(html)


def new_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post successfully created')
            form = PostForm()

    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'posts/new.html', context)


