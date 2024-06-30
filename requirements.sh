#!/bin/bash

# Comprobar si el script se está ejecutando como root
if [ "$EUID" -ne 0 ]
  then echo "Por favor, ejecute este script como root."
  exit
fi

# Actualizar e instalar pip y las dependencias
echo "Actualizando lista de paquetes e instalando pip..."
apt update && apt install -y python3-pip

# Instalar las dependencias de Python
echo "Instalando dependencias de Python..."
pip3 install argparse passlib colorama

# Crear una copia del script en /usr/bin
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/passwordGenerator.py"
TARGET_PATH="/usr/bin/passwordGenerator"

echo "Copiando el script a /usr/bin..."
cp "$SCRIPT_PATH" "$TARGET_PATH"
chmod +x "$TARGET_PATH"

echo "Instalación completada. Puede ejecutar el script con 'passwordGenerator' desde cualquier lugar."
