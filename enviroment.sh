#!/bin/sh
activate () {
    . $PWD/venv/bin/activate
  }

export carpeta="venv/"

if [ ! -d $carpeta ]; then
  echo "Creando ambiente virtual..."
  python3 -m venv venv
  echo "Ambiente Creado."
  activate
  export PYTHONPATH=$PWD
  echo "Ambiente activado."
  echo "Instalando requisitos mínimos..."
  pip install -r requirements.txt
  echo "Requisitos mínimos instalados"
else
echo "Ambiente anteriormente creado."
activate
echo "Ambiente activado."
fi
unset carpeta






