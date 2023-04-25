import Conectors.init as init
import requests
import json

class facturas(init.conexion):
    def __init__(self):
        global URL
        URL = self.API+"/facturas/"
        global maquetador
        maquetador = init.conexion()

    def listar(self):
        response = requests.get(URL)
        seteado = json.loads(response.text)
        # maquetador.maquetador_facturas(seteado)
        return seteado

    def buscar(self, id):
        try:
            response = requests.get(URL+str(id))
            seteado = json.loads(response.text)
            maquetador.maquetador_facturas(seteado)
            return True
        except:
            print('ID no existen')
            return False

    def insertar(self, datos): # Aqui de entrada debe ser un array
        data = dict(
            cliente = datos[0],
            fecha = datos[1],
            ciudad = datos[2],
            compras = datos[3],
            subtotal = datos[4],
            descuento = datos[5],
            iva = datos[6],
            total = datos[7],
        )
        try:
            response = requests.post(URL, json=data)
            return True
        except:
            return False

    def editar(self, ID, datos):
        try:
            print(ID)
            if self.buscar(ID):
                data = dict(
                    cliente = datos[0],
                    fecha = datos[1],
                    ciudad = datos[2],
                    compras = datos[3],
                    subtotal = datos[4],
                    descuento = datos[5],
                    iva = datos[6],
                    total = datos[7],
                )       
                response = requests.put(URL+str(ID), json=data)
                return True
        except:
            print('No Existe el ID')
            return False

    def eliminar(self, id):
        try:
            if self.buscar(id):
                response = requests.delete(URL+str(id))
                print('Funciona')
                return True
        except:
            print('No Existe el ID')
            return False

if __name__=='__main__':
    fac = facturas()
    fac.listar()
    # post = ['Coca', 2, 0.50, 1, 1001001]
    fac.insertar(post)