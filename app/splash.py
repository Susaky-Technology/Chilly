from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout
import Conectors.trabajadores as trabajadores

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        # Configurar una hoja de estilo para el diálogo de login
        self.setStyleSheet('background-image: url("banner.jpg"); background-position: center; background-repeat: no-repeat; color: black')
     

        # Configurar el título y tamaño de la ventana
        self.setWindowTitle('Login - Chilly by Sasuky')
        self.setFixedSize(300, 200)

        # Crear widgets
        self.correo_label = QLabel('Correo electrónico:')
        self.correo_edit = QLineEdit()
        self.contrasena_label = QLabel('Contraseña:')
        self.contrasena_edit = QLineEdit()
        self.contrasena_edit.setEchoMode(QLineEdit.Password)
        self.ingresar_button = QPushButton('Ingresar')

        # Configurar el diseño
        layout = QVBoxLayout()
        layout.addWidget(self.correo_label)
        layout.addWidget(self.correo_edit)
        layout.addWidget(self.contrasena_label)
        layout.addWidget(self.contrasena_edit)
        layout.addWidget(self.ingresar_button)
        self.setLayout(layout)

        # Establecer un estilo para el campo de texto de correo electrónico
        self.correo_edit.setStyleSheet('background: white; color: black')
        self.contrasena_edit.setStyleSheet('background: white; color: black')


        # Conectar la señal "clicked" del botón "Ingresar" a la función "on_ingresar_clicked"
        self.ingresar_button.clicked.connect(self.on_ingresar_clicked)

    def on_ingresar_clicked(self):
        # Comprobar que los campos de correo y contraseña no estén vacíos
        correo = self.correo_edit.text()
        contrasena = self.contrasena_edit.text()
        if correo == '' or contrasena == '':
            # Mostrar un mensaje de error si los campos están vacíos
            self.error_dialog = QDialog(self)
            self.error_dialog.setWindowTitle('Error')
            self.error_dialog.setFixedSize(200, 100)
            self.error_label = QLabel('Los campos no pueden estar vacíos.')
            self.error_layout = QVBoxLayout()
            self.error_layout.addWidget(self.error_label)
            self.error_dialog.setLayout(self.error_layout)
            self.error_dialog.exec_()
        else:
            trabajador = trabajadores.trabajadores()
            if trabajador.login(correo, contrasena) == 'admin':
                self.accept()

if __name__ == '__main__':
    app = QApplication([])
    login_dialog = LoginDialog()
    if login_dialog.exec_() == QDialog.Accepted:
        # Configurar usuario 
        import gui.user_gui
        print("Exitoso")
    app.quit()

