from flask import Flask, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import DataRequired, InputRequired

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Clave secreta necesaria para manejar sesiones y CSRF protection
app.config['SECRET_KEY'] = 'secretkey'  


# Definición del formulario usando Flask-WTF
class MyForm(FlaskForm):
    
    # Campo de correo electrónico con validadores de longitud y formato de correo electrónico
    email = StringField('Email', [validators.Length(min=6, max=120), validators.Email()])
    
    # Campo de contraseña con validadores de longitud y requerimiento de datos
    password = PasswordField('Password', validators=[
        DataRequired(), 
        validators.Length(min=6, message=('Little short for an email address?')),
    ])


# Definición de la ruta principal ('/') y manejo de métodos GET y POST
@app.route('/', methods=['GET', 'POST'])
def login():
    
    form = MyForm()  # Instancia del formulario

    # Si la solicitud es POST y los datos del formulario son válidos
    if request.method == 'POST' and form.validate():
        data = {
            'email': form.email.data, 
            'password': form.password.data
        }
        
        # Verificación de credenciales
        if data['email'] == 'admin@email.com' and data['password'] == '12345678':
            
            # Imprimir los datos en la consola (para depuración)
            print(data) 
            
            # Renderizar la plantilla de éxito
            return render_template('success.html')  
        
        else:
            return render_template('login.html', form=form)  # Renderizar la plantilla de inicio de sesión con el formulario
    
    else:
        
        # Si la solicitud es GET o el formulario no es válido, se renderiza la plantilla de inicio de sesión con el formulario
        return render_template('login.html', form=form)

# Ejecutar la aplicación Flask en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)
