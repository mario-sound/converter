#!/usr/bin/env python3

from PIL import Image  # Importar la clase Image de la biblioteca Pillow para el manejo de imágenes
import os  # Importar el módulo os para trabajar con funcionalidades del sistema operativo

dir = os.getcwd()  # Obtener el directorio actual de trabajo
files = os.listdir(dir)  # Obtener una lista de los archivos en el directorio actual
output_dir = '/opt/icons'  # Definir la carpeta de salida donde se guardarán las imágenes convertidas

# Iterar a través de cada archivo en el directorio actual
for image in files:
    if image.endswith('_48dp'):  # Verificar si el nombre del archivo termina con '_48dp'
        ruta = os.path.join(dir, image)  # Construir la ruta completa del archivo
        imagen = Image.open(ruta)  # Abrir la imagen utilizando la biblioteca Pillow
        
        # Verificar si la imagen no está en modo RGB y convertirla a ese modo si es necesario
        if imagen.mode != 'RGB':
            imagen = imagen.convert('RGB')
        
        # Redimensionar la imagen a 128x128 píxeles y rotarla 90 grados en sentido horario
        imagen = imagen.resize((128, 128)).rotate(90)
        
        # Definir la ruta completa para guardar la imagen en la carpeta de salida
        image_path = os.path.join(output_dir, image)
        
        # Guardar la imagen con el formato JPEG en la ubicación especificada
        imagen.save(image_path, format='JPEG')
