# Modulo del Sistema
import sys
import base64

# Modulo de Conexion
import Conectors.productos as productos

# Modulos de Qt5
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon, QPixmap, QImage

class interface(QMainWindow):
    producto = productos.productos()

    def __init__(self):
        super().__init__()
        # Cargamos el XML de Qt
        uic.loadUi("gui/user_gui.ui", self)
        # Modificamos los tamaños de la tabla
        self.tabla_productos.setColumnWidth(0,50)
        self.tabla_productos.setColumnWidth(1,200)
        self.tabla_productos.setColumnWidth(2,70)
        self.tabla_productos.setColumnWidth(3,60)
        self.cargador_tabla_componentes()
        self.menu_opciones()

    def cargador_tabla_componentes(self):
        """
        Por cada llamado a la funcion la variable productos almacena nuevos datos
        si la llamamos como propiedad de clase, esta no almacena los nuevos datos.
        """
        # productos= db_connect.productos()
        produ= productos.productos()
        produ= produ.listar()
        fila=0
        self.tabla_productos.setRowCount(len(produ))
        for individual in produ:
            self.tabla_productos.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(individual['id'])))
            self.tabla_productos.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(individual['nombre'])))
            self.tabla_productos.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(individual['cantidad'])))
            self.tabla_productos.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(individual['precio'])))
            self.tabla_productos.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(individual['valor_total'])))
            fila=fila+1
        # Cargamos la seleccion
        self.tabla_productos.cellClicked.connect(self.eleccion_producto)
        # Cargamos boton seleccionar
        self.seleccionar_productos.clicked.connect(self.seleccionar)
        # Cargamos boton de cargar
        self.boton_productos.clicked.connect(self.cargador_tabla_componentes)


    def eleccion_producto(self):
        try:
            global codigoSeleccion
            codigoSeleccion= int(self.tabla_productos.selectedIndexes()[0].data())
            linea= int(self.tabla_productos.currentRow())
            self.tabla_productos.selectRow(linea)
            self.mensaje_productos.setText("")
            print(f"Linea:{linea} ID:{codigoSeleccion}")

            # Añadiendo imagen
 
            for foto in self.producto.listar():
                binary_data = bytes(foto['foto_producto']['data'])
                image = QImage.fromData(binary_data)
                self.imagen.setPixmap(QPixmap.fromImage(image))           
            """
            pixmap= QPixmap()
            pixmap.loadFromData(imagen)
            self.imagen.setPixmap(pixmap)
            """


            self.seleccionar()

            return codigoSeleccion
        except:
            self.mensaje_productos.setText("[Seleccione el ID del Producto]")

    def menu_opciones(self):
        # Deshabilitamos los campos de Nombre e ID para las opciones de Editar y Eliminar
        self.id_editar.setEnabled(False)
        self.nombre_editar.setEnabled(False)
        self.id_eliminar.setEnabled(False)
        self.nombre_eliminar.setEnabled(False)
        # Boton para insertar elementos
        self.boton_insertar.clicked.connect(self.insertar)
        # Boton para Editar elementos
        self.boton_editar.clicked.connect(self.editar)
        # Boton para Eliminar elementos
        self.boton_eliminar.clicked.connect(self.eliminar)

    def limpieza(self):
        # Limpiamos los registros
        self.nombre_insertar.setText("")
        self.cantidad_insertar.setText("")
        self.precio_insertar.setText("")
        # Campos Editar
        self.nombreEntrada_editar.setText("")
        self.nombre_editar.setText("")
        self.cantidad_editar.setText(" ")
        self.precio_editar.setText(" ")
        self.id_editar.setText(" ")
        # Campos Eliminar
        self.nombre_eliminar.setText(" ")
        self.id_eliminar.setText(" ")

    """
    Desde aquí comienzan las funciones de los botones
    --> Parte logica
    """
    # Boton de seleccionar
    def seleccionar(self):
        try:
            salida = self.producto.listar()
            for individual in salida:
                codigo=str(individual['id'])
                global nombreSeleccion
                nombreSeleccion=str(individual['nombre'])
                # Mostramos en la opcion de Editar
                self.id_editar.setText(codigo)
                self.nombre_editar.setText(nombreSeleccion)
                # Mostramos en la opcion de Eliminar
                self.id_eliminar.setText(codigo)
                self.nombre_eliminar.setText(nombreSeleccion)
                return nombreSeleccion
        except:
            self.mensaje_productos.setText("[ID no seleccionado]")

    def insertar(self):
        # Obtenemos la entrada del usuario
        try:
            nombre= str(self.nombre_insertar.text())
            cantidad= int(self.cantidad_insertar.text())
            precio= float(self.precio_insertar.text())
            valor_total = precio*cantidad
            foto= 'd'
            datos = [nombre, cantidad, precio, valor_total, foto]
            self.producto.insertar(datos)
            self.cargador_tabla_componentes()
            self.mensaje_insertar.setText("[ Realizado con Exito ]")
        except:
            self.mensaje_insertar.setText("[ Error 104 ]")

    def editar(self):
        try:
            codigo= str(self.id_editar.text())
            nombre= str(self.nombreEntrada_editar.text())
            cantidad= int(self.cantidad_editar.text())
            precio= float(self.precio_editar.text())
            valor_total = precio*cantidad
            foto_producto= "d"
            datos = [nombre, cantidad, precio, valor_total, foto_producto]
            if self.producto.editar(codigo, datos):
                self.mensaje_editar.setText("[Realizado con Exito]")
            else:
                print(codigo, "El id no existe hablo desde la GUI")
            self.cargador_tabla_componentes()
        except:
            self.mensaje_editar.setText("[Error 104]")

    def eliminar(self):
        try:
            codigo= self.id_editar.text()
            self.producto.eliminar(codigo)
            self.mensaje_eliminar.setText("[Borrado con Exito]")
            self.cargador_tabla_componentes()
        except:
            self.mensaje_eliminar.setText("[Error ID no seleccionado]")

if __name__=='__main__':
    app= QApplication(sys.argv)
    GUI= interface()
    GUI.show()
    sys.exit(app.exec_())

else:
    app= QApplication(sys.argv)
    GUI= interface()
    GUI.show()
    sys.exit(app.exec_())
