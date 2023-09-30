from django.urls import reverse
from django.shortcuts import redirect ,render ,get_object_or_404
from django.core.paginator import Paginator, Page

from django.urls import reverse
from .models import Post


def volver_app_inicio(request):
    # Construye la URL de la vista en app1 que deseas redirigir
    url_destino = reverse('inicio')

    # Realiza la redirección a la vista en app1
    return redirect(url_destino)

# Create your views here.

def blog_app(request):
    # Obtener todos los objetos Post ordenados por fecha de publicación en orden descendente
    posts = Post.objects.all().order_by('-fecha_de_publicacion')

    # Configurar la paginación
    paginator = Paginator(posts, 5)  # Divide las publicaciones en páginas de 10 elementos por página

    page_number = request.GET.get('page')  # Obtiene el número de página de la URL
    page = paginator.get_page(page_number)  # Obtiene la página actual

    # Definir el contexto con los posts paginados
    context = {
        'page': page,
    }

    # Renderizar la plantilla y pasar el contexto
    return render(request, 'blog.html', context)

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'detalle_post.html', {'post': post})



def detalle_de_entrada(request, id):
    # Lógica para recuperar la entrada del blog con el ID proporcionado
    entrada = Entrada.objects.get(pk=id)
    # Lógica adicional si es necesario
    return render(request, 'blog/detalle_de_entrada.html', {'entrada': entrada})

"""def posts(request):
    # Obtener todos los objetos Post
    posts = Post.objects.all()

    # Definir el contexto con los posts
    context = {
        'posts': posts,
    }

    # Renderizar la plantilla y pasar el contexto
    return render(request, 'postear.html', context)"""
