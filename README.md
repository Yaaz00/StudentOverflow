# StudentOverflow: Una plataforma de preguntas y respuestas para estudiantes

StudentOverflow es una aplicación web que permite a los estudiantes hacer preguntas sobre sus materias y recibir respuestas de otros usuarios.  Está inspirada en Stack Overflow.

## Tabla de Contenidos

* [Requisitos]
* [Instalación]
* [Ejecución]



## <a name="requisitos"></a>Requisitos

Para ejecutar este proyecto, necesitarás:

* Python 3.7 o superior
* PostgreSQL (con el usuario `postgres` con contraseña `ABC123.com` y la base de datos `StudentOverflow` creada)
* Las siguientes librerías de Python (instalas con `pip install -r requirements.txt`):
    * Flask==2.0.3
    * Werkzeug==2.0.3
    * Flask-SQLAlchemy==2.5.1
    * Flask-WTF==0.15.1
    * WTForms==2.3.3
    * psycopg2-binary==2.9.1


## <a name="instalación"></a>Instalación

1. Clona este repositorio: `git clone <URL_DE_TU_REPOSITORIO>`
2. Crea un entorno virtual (recomendado): `python -m venv venv`  y actívalo: `source venv/bin/activate` (Linux/macOS) o `venv\Scripts\activate` (Windows).
3. Instala las dependencias: `pip install -r requirements.txt`


## <a name="ejecución"></a>Ejecución

1. Asegúrate de que tu servidor PostgreSQL esté funcionando.
2. Ejecuta la aplicación: `python app.py`
3. Accede a la aplicación en tu navegador: `http://127.0.0.1:5000/`






