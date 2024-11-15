# TDAddle

Backend del juego TDAddle

---
# Setup (Linux)

## Prerequisitos
- Python 3.x
- pip install manager

## Pasos para instalar

1. Clonar el repositorio
```bash
   git clone https://github.com/JuampiAmboage/TDAddle.git
   cd <repository_directory>
```

2. Crear y activar un entorno virtual
```bash 
    python3 -m venv venv
    source venv/bin/activate
```

3. Una vez dentro, instalar Django y otras dependencias
```bash
    pip install -r requirements.txt
```

4. Migrar las tablas a la base de datos

```bash
    python3 manage.py migrate
```

5. Crear un superusuario
```bash
    python3 manage.py createsuperuser
```

6. Iniciar el servidor (corre en el puerto 8000)
```bash
    python3 manage.py runserver
```

# Rutas
   - **/admin**: si ya te creaste un superusuario, te logeás y te da acceso a una interfaz para administrar las bases
   - **/api**: acceso a la API
