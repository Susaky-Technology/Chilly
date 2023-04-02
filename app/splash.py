from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    app = QApplication([])
    splash = QSplashScreen(QPixmap('baner.jpg'))
    splash.show()
    splash.showMessage('Cargando...', Qt.AlignCenter, Qt.white)

    # Carga de la aplicación principal aquí

    splash.close()
    app.exec_()
