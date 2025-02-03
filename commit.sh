#!/bin/bash
echo "Haciendo un nuevo commit "
cd /opt/odoo/custom_addons/zoologico
sudo git add .
sudo git commit -m "$1"
code .
