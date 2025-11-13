# FROM BASE PYTHON 11
FROM python:3.12-slim

# DIRECTORIO DE TRABAJO
WORKDIR /app

# COPIAR LOS ARCHIVOS NECESARIOS
COPY . /app

# INSTALAR DEPENDENCIAS
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir Flask python-dotenv

# EXPONER EL PUERTO
EXPOSE 80

# EJECUTAR LA APLICACION
CMD ["python", "app.py"]
