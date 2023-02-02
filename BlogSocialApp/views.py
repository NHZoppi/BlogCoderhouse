from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm, AvatarUploadForm
from django.core.paginator import Paginator
from .models import Avatar

def inicio(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'Functions/inicio.html', {'posts': posts})

def about(request):
    return render(request, 'Functions/about.html')

@login_required
def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('Inicio')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'Functions/postear.html', context)

# Perfil del usuario
@login_required
def profile(request):
    return render(request, 'Functions/profile.html')

# Vista de posteos del usuario
def view_name(request):
    user_posts = Post.objects.filter(user=request.user)
    paginator = Paginator(user_posts, 5)
    page = request.GET.get('page')
    user_posts = paginator.get_page(page)
    return render(request, 'Functions/profilePosts.html', {'user_posts': user_posts})


# Vista de articulo completo
def article_view(request, article_id):
    article = Post.objects.get(id=article_id)
    context = {'article': article}
    return render(request, 'Functions/article.html', context)

# Avatar del Usuario
@login_required
def upload_avatar(request):
    if request.method == 'POST':
        # Obtiene los datos del formulario, incluyendo la imagen subida
        form = AvatarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Obtiene la instancia del formulario
            instance = form.save(commit=False)
            instance.user = request.user
            # Si el usuario ya tiene un avatar asociado, elimina la imagen anterior
            try:
                old_avatar = Avatar.objects.get(user=request.user)
                old_avatar.image.delete()
                old_avatar.delete()
            except Avatar.DoesNotExist:
                pass
            # Guarda la nueva imagen
            instance.save()
            return redirect('profile')
    else:
        # Si el método es GET, muestra el formulario vacío
        form = AvatarUploadForm()
    return render(request, 'avatar/upload.html', {'form': form})