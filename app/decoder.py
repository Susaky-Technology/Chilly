import base64

# Obtener los datos de la imagen en formato bytes
datos_imagen = bytes()

# Decodificar los datos de la imagen en base64
imagen_decodificada = base64.b64decode(datos_imagen)

# Guardar la imagen en un archivo
with open('foto.jpg', 'wb') as f:
    f.write(imagen_decodificada)

