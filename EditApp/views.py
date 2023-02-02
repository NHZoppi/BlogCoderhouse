from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.generic import View, DeleteView
from .forms import UpdateProfileForm
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from BlogSocialApp.models import Post
from BlogSocialApp.forms import PostForm
from django.urls import reverse_lazy
# Create your views here.

@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'ChangePass.html', {'form': form})
        
    # Procesa la solicitud POST cuando el usuario envía el formulario para cambiar su contraseña
    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        # Valida el formulario
        if form.is_valid():
            # Guarda los cambios en la contraseña del usuario
            user = form.save()
            # Actualiza la sesión del usuario con la nueva información de autenticación
            update_session_auth_hash(request, user) # Importante!
            # Muestra un mensaje de éxito
            messages.success(request, 'Tu constraseña se ha actualizado!')
            # Redirige al usuario a la página de perfil
            return redirect('profile')
        else:
            # Muestra un mensaje de error si el formulario no es válido
            messages.error(request, 'Porfavor corregi tu error de abajo.')
            return render(request, 'ChangePass.html', {'form': form})




@method_decorator(login_required, name='dispatch')
# Usamos class que hereda de la clase view de django.
class UpdateProfileView(View):
    # La función get es llamada cuando se hace una solicitud GET a la URL correspondiente a esta vista 
    def get(self, request):
        # Crear una instancia de UpdateProfileForm con la información del usuario actual
        form = UpdateProfileForm(instance=request.user)
        # Renderizar la plantilla ChangeProfile.html y pasar el formulario como contexto
        return render(request, 'ChangeProfile.html', {'form': form})
    # La función post es llamada cuando se hace una solicitud POST a la URL correspondiente a esta vista
    def post(self, request):
         # Crear una instancia de UpdateProfileForm con los datos enviados en el request.POST y la información del usuario actual
        form = UpdateProfileForm(request.POST, instance=request.user)
        # Validar los datos enviados
        if form.is_valid():
            # Guardar los cambios realizados en el perfil del usuario
            form.save()
            # Mostrar un mensaje de éxito al usuario
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            # Redirigir al usuario a la página de perfil
            return redirect('profile')
        # Renderizar nuevamente la plantilla ChangeProfile.html y pasar el formulario con los errores como contexto
        return render(request, 'ChangeProfile.html', {'form': form})



def edit_post(request, pk):
    # Obtener el post correspondiente al pk (primary key) especificado
    post = get_object_or_404(Post, pk=pk)
    
    # Verificar si el usuario que está tratando de editar el post es el autor original
    if post.user != request.user:
        # Redirigir al usuario a otra página o mostrar un mensaje de error
        return redirect('post_list')
    
    # Verificar el método HTTP utilizado en la solicitud
    if request.method == "POST":
        # Crear una instancia de PostForm con los datos enviados en el request.POST y la instancia del post original
        form = PostForm(request.POST, instance=post)
        # Validar los datos enviados
        if form.is_valid():
            # Guardar los cambios realizados en el post
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('postusuario')
    else:
        # Crear una instancia de PostForm con la instancia del post original
        form = PostForm(instance=post)
        
    # Renderizar la plantilla edit_post.html y pasar el formulario como contexto
    return render(request, 'edit_post.html', {'form': form})


@method_decorator(login_required, name='dispatch')
# La clase `PostDeleteView` hereda de la clase `DeleteView` de Django
class PostDeleteView(DeleteView):
    # El modelo asociado a esta vista es `Post`
    model = Post
    # El template que se utilizará para mostrar la página de confirmación de eliminación
    template_name = "Delete_post.html"
    # La URL a la que se redirigirá después de que el post se haya eliminado exitosamente
    success_url = reverse_lazy("postusuario")

    # Sobrescribimos el método `delete` para verificar que el usuario que está tratando de eliminar el post es el dueño del post
    def delete(self, request, *args, **kwargs):
        # Obtenemos el objeto de post a eliminar
        self.object = self.get_object()
        # Verificamos que el usuario que está tratando de eliminar el post es el dueño del post
        if self.object.user != self.request.user:
            # Si no es el dueño, redirigimos al usuario a la página de postusuario
            return redirect("postusuario")
        # Obtenemos la URL de éxito
        success_url = self.get_success_url()
        # Eliminamos el post
        self.object.delete()
        # Redirigimos al usuario a la URL de éxito
        return redirect(success_url)