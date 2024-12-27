from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'ABC098dfgas'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ABC123.com@localhost/StudentOverflow'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos de la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)

class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', backref='preguntas')  # Relación para acceder al usuario

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    id_pregunta = db.Column(db.Integer, db.ForeignKey('pregunta.id'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    pregunta = db.relationship('Pregunta', backref='respuestas')  # Relación para acceder a la pregunta
    usuario = db.relationship('Usuario', backref='respuestas')  # Relación para acceder al usuario

@app.route('/')
def index():
    preguntas = Pregunta.query.all()
    return render_template('index.html', preguntas=preguntas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        
        # Verifica si el usuario existe
        usuario = Usuario.query.filter_by(correo=correo).first()
        
        if usuario and check_password_hash(usuario.contrasena, contrasena):
            session['user_id'] = usuario.id
            session['nombre'] = usuario.nombre
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('index'))  # Redirigir a la página de inicio
        else:
            flash('Correo o contraseña incorrectos.', 'danger')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        
        hashed_password = generate_password_hash(contrasena, method='sha256')
        
        nuevo_usuario = Usuario(nombre=nombre, correo=correo, contrasena=hashed_password)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Registro exitoso, por favor inicia sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('nombre', None)
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('index'))

@app.route('/create_question', methods=['POST'])
def create_question():
    if 'user_id' not in session:
        flash('Debes iniciar sesión para hacer una pregunta.', 'danger')
        return redirect(url_for('login'))

    titulo = request.form['titulo']
    contenido = request.form['contenido']
    nueva_pregunta = Pregunta(titulo=titulo, contenido=contenido, id_usuario=session['user_id'])

    db.session.add(nueva_pregunta)
    db.session.commit()
    flash('Pregunta creada exitosamente!', 'success')
    return redirect(url_for('index'))

@app.route('/add_response/<int:pregunta_id>', methods=['POST'])
def add_response(pregunta_id):
    if 'user_id' not in session:
        flash('Debes iniciar sesión para responder.', 'danger')
        return redirect(url_for('login'))

    contenido = request.form['contenido']
    nueva_respuesta = Respuesta(contenido=contenido, id_pregunta=pregunta_id, id_usuario=session['user_id'])

    db.session.add(nueva_respuesta)
    db.session.commit()
    flash('Respuesta agregada exitosamente!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()  # Crea las tablas en la base de datos
    app.run(debug=True)

