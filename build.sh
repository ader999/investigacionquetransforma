#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Recopilar archivos estáticos
python manage.py collectstatic --no-input

# Crear un superusuario automáticamente
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('overader', 'aderjasmirzeasrocha@gmail.com', '00040')" | python manage.py shell

# Puedes reemplazar 'nombre_usuario', 'correo@ejemplo.com' y 'contraseña' con los valores deseados
