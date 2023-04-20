import base64

with open('banner.jpg', 'rb') as f:
    imagen_bytes = f.read()
    imagen_base64 = base64.b64encode(imagen_bytes).decode('utf-8')

datos = {'imagen': imagen_base64}

print(datos)

