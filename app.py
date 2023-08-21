# Autor:Valeria Ivonne Gutierrez Martinez
# Importa los módulos Flask,jsonify,request,session,redirect y url
 
from flask import Flask, jsonify, request, session, redirect, url_for

# Autor:Valeria Ivonne Gutierrez Martinez
#Importa los modulos pymysql,bcrypt,hashpw, gensalt
import pymysql

# Autor:Valeria Ivonne Gutierrez Martinez, aqui se empieza a crear la instancia para flask.
app = Flask(__name__)

# Autor:Valeria Ivonne Gutierrez Martinez
# Aqui se configura la direccion de mi base de datos en MYSQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost' 
# Aqui se configura el usuario que uso para acceder a mi base
app.config['MYSQL_DATABASE_USER'] = 'root' 
# Esta es mi contraseña para mi base de datos, puse mi nombre para que no se me olvide 
app.config['MYSQL_DATABASE_PASSWORD'] = 'Valeria'  
# Este es el nombre que le puse a mi base de datos
app.config['MYSQL_DATABASE_DB'] = 'evaluacionvaleria' 


# Autor:Valeria Ivonne Gutierrez Martinez
# Se crea una conexion a MySQL
mysql = pymysql.connect(
    # Aqui se especifica el host para la base de datos
    host=app.config['MYSQL_DATABASE_HOST'],
    # Se establece el nombre 
    user=app.config['MYSQL_DATABASE_USER'],
    # Sirve para la autenticacion de la contraseña
    password=app.config['MYSQL_DATABASE_PASSWORD'],
    # Aqui se indica el nombre de la base de datos a la que me voy a conectar
    db=app.config['MYSQL_DATABASE_DB']
)

# Autor:Valeria Ivonne Gutierrez Martinez
#Inicio del metodo POST
@app.post('/register')
def login():

   # Para obtener los datos desde JSON
    datos = request.get_json()  
    # Para obtener el email de los datos
    email = datos.get('email')  
    # Para obtener la contraseña de los datos
    password = datos.get('password')  

    # Aqui se creo un cursor para tener interaccion con la base de datos
    cursor = mysql.cursor(pymysql.cursors.DictCursor)  
    # Aqui se hace una consulta SQL para tener el usuario con el email que se dio
    cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
    # Sirve para dar el primer usuario que se parezca al email que se ingreso
    usuarios = cursor.fetchone()  
    if usuarios:
        stored_password = usuarios['password'] #Obtiene la contra

       # Sirve si la contraseña almacenada coincide con la contraseña proporcionada
        if stored_password == password:
            # Inicia una sesion
            session['logged_in'] = True  
            # Da un mensaje de inicio se sesion
            return {'message': 'Inicio de sesión exitoso'}  
        else:
            return {'error': 'La contraseña no coincide, intentalo nuevamente'} # Da un mensaje si no es correcto
    else:
        return {'error': 'El correo no está registrado en la base de datos'}

# Autor:Valeria Ivonne Gutierrez Martinez
#Inicio del metodo GET, para mostrar la tabla de los datos
@app.get('/showtable')
def ver_tabla():
    #Para verificar si el usuario inicio sesion
    if 'logged_in' not in session or not session['logged_in']:
         #Redirige al registro si aun no se inicia la sesion
        return redirect(url_for('register')) 

   #Se crea un cursor para la interaccion con la base de datos
    cursor = mysql.cursor(pymysql.cursors.DictCursor)  
      #Aqui se hace una consulta SQL para obtener todos los usuarios
    cursor.execute('SELECT * FROM usuarios')
     # Obtener todos los usuarios en formato de diccionario
    usuarios = cursor.fetchall()  
    # Para obtener los datos desde JSON
    return jsonify(usuarios) 


# Autor:Valeria Ivonne Gutierrez Martinez
# Metodo POST
@app.post('/add_user')
# Para agregar usuarios
def agregar_usuario():

    try:
        # Para obtener los datos desde JSON
        datos = request.get_json()  
        # Aqui se obtiene el valor del numero de control de los datos
        numero_de_control = datos.get('numero_de_control')  
         # Aqui se obtiene el valor de usuario
        usuario = datos.get('usuario')  
        # Aqui se obtiene el valor de password
        password = datos.get('password') 
        # Aqui se obtiene el valor de email
        email = datos.get('email') 
        # Aqui se obtiene el valor de nombre 
        nombre = datos.get('nombre') 
        # Aqui se obtiene el valor de telefono 
        telefono = datos.get('telefono')  
        # Aqui se obtiene el valor de municipio
        municipio = datos.get('municipio')  
        #Se crea un cursor para la interaccion con la base de datos
        cursor = mysql.cursor()  
        #Para una consulta SQL para insertar un nuevo usuario
        cursor.execute('INSERT INTO usuarios (numero_de_control, usuario, password, email, nombre, telefono, municipio) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                       (numero_de_control, usuario, password, email, nombre, telefono, municipio))
        #Para guardar los cambios en la base de datos
        mysql.commit()  

        #Da un mensaje si el ususario se agrego 
        return {'message': 'Usuario agregado exitosamente'}, 201  
    except Exception as e:
        #Da mensaje de error 
        return {'error': 'No se agrego el usuario, intentelo nuevamente', 'details': str(e)},404


