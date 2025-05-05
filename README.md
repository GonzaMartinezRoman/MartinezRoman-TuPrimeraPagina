# 69535_Python
# **Tu primera página**

**Web de gestion de clientes de la red de gimnasios ficticia "Training-Center"**

Objeto: Constituye la base de datos de clientes del gimnasio, a la cual puede acceder el personal administrativo, con un Usuario y Contraseñas personales, para registrar nuevos clientes, visualizar la ficha de un cliente y modificar o eliminar clientes. 

Descripción: 
- La paǵina contiene una vista de Inicio, "Inicio" con un mensaje de bienvenida, 
- Una vista "Registrar Cliente" a través de la cual se carga la información de un nuevo cliente y se almacena en la base de datos, 
- Una vista "Lista de Clientes" donde pueden verse todos los clientes registrados en la base de datos, acceder a la ficha de cada cliente (vista de detalle) y modificar o elilimar un determinado cliente.

Admin: gonzalomartinezroman / @$1234
usuarios: 
usuario_de_prueba_1 / @$123456
Gonza / @$GMR1986

quedé en ultima clase 2:53:05
---
# Puntos para la entrega final

- [x] Entrega individual
- [x] subir a github
- [x] readme como la entrega 3
- [ ] video de maximo 10 min que muestre la pagina y sus funcionalidades (con o sin audio)
  - programas que pueden utilizar freecam8, obs, filmora 12, etc.
- [x] No agregar la Base de datos (el archivo db.sqlite3) en la entrega. Deberia estar en el .gitignore
- [x] Uso de herencia de templates
- [x] Exista gitignore con:
```
<carpeta del entorno virtual>
__pycache__
db.sqlite3
media
```

Estos ultimos son por el hecho de no compartir la info de tu bd y, aparte, las imagenes son archivos muy pesados que no es recomendable tenerlos en el repo. En cambio, las imagenes que sean parte del codigo del proyecto deberian guardarse en la carpeta static.

- [ ] Existencia del archivo requirements.txt actualizado.
- [ ] Tener en cuenta al manejar forms con imagenes hay que adaptar el template, y la vista...no solo el modelo y el formulario.
- [x] Uso de minimo 2 clases basadas en vista.
- [x] Uso de minimo un mixin en una CBV y un decorador en una view comun.
- [ ] Hacer uso de Estaticos (carpeta static con la carga de templates desde bootstrap)
- [x] Una vista de inicio
- [x] Acceso a una vista "Acerca de mi"/"About"
- [ ] Crear un modelo principal que contenga los siguiente campos como minimo: 3 Charfield  (o 2 Charfield y un Integerfield), 1 campo de imagen, 1 de fecha
- [x] Vista de listado de los objetos del modelo principal (modelo a eleccion). En la cual cada objeto mostrara solo alguno de sus datos
- [ ] Mensaje que de aviso en caso de no haber ningun objeto creado o al utilizar el buscador no encontrar tampoco algun objeto
- [x] Desde el listado:
    1. poder acceder a una vista que muestre el detalle de el objeto seleccionado
    2. poder acceder a una vista de creacion, una de edicion y una de borrado de los objetos del listado
- [ ] [va por su cuenta] Acomodar el modelo para que maneje un campo de imagen y todas las pantallas relacionadas al modelo lo tengan en cuenta a este nuevo campo.
- [x] Registrar en el apartado de admin todos los modelos creados
- [x] Tener una app para el manejo de todas las vistas relacionadas al usuario/autenticacion
- [x] Desarrollar las vistas para un login, un logout y el registro de un usuario al cual se le solicite: username, email, password
- [ ] [va por su cuenta] Crear una vista de perfil donde se muestren los datos del usuario:
  - nombre
  - apellido
  - email
  - avatar
  - [va por su cuenta] Campo a eleccion (biografia, fecha de nacimiento, gustos, hobbies, etc)
- [ ] Desde el perfil, crear un acceso a una vista de edicion de estos datos.