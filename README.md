# Django Blog
Este es un proyecto de Django que permite crear y ver un blog.

## Instalación
Para instalar este proyecto, siga los siguientes pasos:

Clone este repositorio: git clone https://github.com/NHZoppi/BlogCoderhouse.git

Instale las dependencias: pip install -r requirements.txt

Realice las migraciones: python manage.py makemigrations y python manage.py migrate

Corra el servidor de desarrollo: python manage.py runserver

## Uso
Una vez que el servidor esté corriendo, puede acceder al blog a través de la URL http://localhost:8000/.
Para acceder al SuperUser: 
User: Admin
Password: Hola123@

## Modelos del Blog

Tenemos el Post (BlogSocialApp)
Tenemos el Avatar (BlogSocialApp)

## Vistas

### BlogSocialApp vistas:

Inicio (muestra todos los posts)
Login 
Register
Avatar del usuario
post_view (Vista de crear un post nuevo)
profile (Vista del perfil de usuario)
view_name (Mostrar los posteos del usuario conectado)
article_view (muestra todo el contenido del Posteo/articulo)
upload_avatar (Crea un avatar y si ya tiene uno lo cambia)

### AuthApp vistas:

LoginView (Aca herede clases de Django (View))
RegisterView (Aca herede clases de Django (View))
CustomLogoutView (Aca herede clases de Django (LogoutView))

### EditApp vistas:

ChangePasswordView (Aca herede clase de django (View))
UpdateProfileView (Aca herede clase de django (View))
edit_post (Vista para editar post personalizada como funcion)
PostDeleteView (Aca herede clase de django (DeleteView))

### UnitTest
Este test se encuentra en la app BlogSocialApp
Este proyecto incluye pruebas unitarias para verificar la funcionalidad de la vista inicio y sus paginaciones, tambien vemos si funcionan los urls, para acceder a la vista previa de las urls. Puede ejecutar las pruebas con el comando python manage.py test.