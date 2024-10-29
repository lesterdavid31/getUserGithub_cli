# Obtener Actividad de Usuario en GitHub

Este proyecto es una herramienta de línea de comandos (CLI) que permite obtener las actividades recientes de un usuario en GitHub, como comentarios en problemas, estrellas, creación de pull requests y más.

## Características

- **Consulta de eventos**: Muestra diferentes tipos de eventos que el usuario ha realizado en GitHub, tales como:
  - Comentarios en issues.
  - Pushes a repositorios.
  - Creación de issues.
  - Estrellas en repositorios.
  - Creación y revisión de pull requests.
  - Creación de ramas o etiquetas.
  - Otros eventos específicos de GitHub.
  
- **Línea de comandos**: La herramienta utiliza Click para crear una interfaz fácil de usar en la terminal.
  
- **Validación de entradas**: El nombre de usuario es validado antes de realizar la solicitud a la API de GitHub.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal del proyecto.
- **Requests**: Librería utilizada para realizar solicitudes HTTP a la API de GitHub.
- **Click**: Framework para crear comandos y opciones en la línea de comandos de forma sencilla.

## Instalación y Configuración

### 1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/actividad_usuario_github.git
   cd actividad_usuario_github
   ```

### 1. Crea un entorno virtual y activa el entorno:

   ```bash
   python -m venv env 
    source env/bin/activate   # En Linux/MacOS
    env\Scripts\activate      # En Windows
   ```

### 1. Instala la dependencias:

   ```bash
pip install -r requirements.txt
   ```

## Uso
- para ejecutr la herramienta desde la línea de comandos, utiliza el siguiente comando:
   ```bash
  python cli.py getUserGithub --name '<nombre_usuario_github>'

   ```
   
https://roadmap.sh/projects/github-user-activity
  
   
