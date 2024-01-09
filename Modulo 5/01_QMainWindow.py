from PyQt5.QtWidgets import QApplication, QAction, QMainWindow
import sys

class Aplication(QMainWindow):
    def __init__(self):
        super(Aplication, self).__init__()
        self.resize(350, 350)
        self.setWindowTitle("Barra de Menu")

        action_menu = QAction("Salir", self)
        action_menu.setShortcut("Ctrl+Q") #Atajo de teclado
        action_menu.triggered.connect(self.close)

        action_menu2 = QAction("Guardar", self)
        action_menu2.setShortcut("Ctrl+S") #Atajo de teclado
        action_menu2.triggered.connect(self.guardar)

        action_menu3 = QAction("Abrir", self)
        action_menu3.setShortcut("Ctrl+O") #Atajo de teclado
        action_menu3.triggered.connect(self.abrir)

        #Crear barra de menu
        barra_menu = self.menuBar()
        barra_menu.setNativeMenuBar(True)

        #Agregar menu a la barra
        menu = barra_menu.addMenu("Archivo")
        menu.addAction(action_menu)
        menu.addAction(action_menu2)
        menu.addAction(action_menu3)

        #Agregar otro menu
        menu2 = barra_menu.addMenu("Editar")
        action_menu4 = QAction("Copiar", self)
        action_menu4.setShortcut("Ctrl+C") #Atajo de teclado
        action_menu4.triggered.connect(self.copiar)
        menu2.addAction(action_menu4)

    def guardar(self):
        print("Guardar")

    def abrir(self):
        print("Abrir")

    def copiar(self):
        print("Copiar")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Aplication()
    ventana.show()

    sys.exit(app.exec_())
