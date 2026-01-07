#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Recolectar archivos estáticos (CSS/JS) para que se vean bien
python manage.py collectstatic --no-input

# 3. Ejecutar migraciones (Crear tablas en la base de datos de la nube)
python manage.py migrate