from PIL import Image
import os

dir = os.getcwd()
files = os.listdir(dir)

for image in files:
    if image.endswith('.tiff'):
        ruta = os.path.join(dir, image)
        imagen = Image.open(ruta)
        imagen_redimensionada = imagen.resize((128, 128)).rotate(90)
        name = os.path.splitext(image)[0]
        image_jpeg = os.path.join(dir, f"{name}.jpeg")
        imagen_redimensionada.save(f"{image_jpeg}.jpeg")
        printf(f"{image} convertida a {image_jpg}.jpeg")
