from django.test import TestCase

# Create your tests here.
from django.test import Client, TestCase
from django.contrib.auth.models import User
from .models import Post

class InicioViewTestCase(TestCase):
    def setUp(self):
        # Creamos un usuario y contraseña
        self.username = 'testuser'
        self.password = 'secret'
        self.user = User.objects.create_user(username=self.username, password=self.password)

        # Creamos una serie de post para la prueba
        for i in range(15):
            Post.objects.create(title='Test Title {}'.format(i), content='Test Content {}'.format(i), user=self.user)
        # Creamos el Client ya que este nos perimete hacer peticiones HTTP  y verificar el estado de respuesta, templates utilizados, etc.
        self.client = Client()

    def test_inicio_view(self):
        # Iniciamos sesión con el usuario de prueba
        self.client.login(username=self.username, password=self.password)

        # Hacemos una petición a la vista inicio
        response = self.client.get('')

        # Verificamos que la respuesta sea correcta (200 indica que la solicitud tuvo exito)
        # Si nos saliera un 404 tendriamos un error ahi
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Functions/inicio.html')

        # Verificamos que se estén mostrando 5 posts por página
        self.assertEqual(len(response.context['posts']), 5)

        # Hacemos una petición a la segunda página
        response = self.client.get('/?page=2')

        # Verificamos que la respuesta sea correcta
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Functions/inicio.html')

        # Verificamos que se estén mostrando 5 posts por página
        self.assertEqual(len(response.context['posts']), 5)