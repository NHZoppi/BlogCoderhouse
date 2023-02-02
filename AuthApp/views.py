from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from django.urls import reverse
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

    # Clase logeo
class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user is not None:
                login(request=request, user=user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('Inicio')
                return redirect(url_exitosa)
            else:
                # Maneja un mensaje de error para el caso en el que el usuario no sea válido
                messages.error(request, 'Usuario y/o contraseña incorrectos')
        return render(request, self.template_name, {'form': form})

    # Clase Registro
class RegisterView(View):
    form_class = RegisterForm
    template_name = 'registro.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            url_exitosa = reverse('Inicio')
            return redirect(url_exitosa)

        return render(request, self.template_name, {'form': form})

    # Clase Deslogueo
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

