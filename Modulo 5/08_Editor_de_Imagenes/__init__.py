from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QAction, QFileDialog,\
    QDesktopWidget, QMessageBox, QSizePolicy, QToolBar, QStatusBar, QDockWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import sys

class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(650, 650)
        self.setWindowTitle("Editor de Fotos")

        self.centrar_Menu()
        self.barra_Herramientas_Botones()
        self.crear_Menu()
        self.crear_Barra_Herramientas()
        self.widgets_edicion()

    def barra_Herramientas_Botones(self):
        self.muelle_botones = QDockWidget("Barra de Botones")
        self.muelle_botones.setAllowedAreas(Qt.LeftDockWidgetArea)

        #Creacion del contenedor
        self.contenedor = QWidget()

        #Creacion de los botones

        #Boton Rotar 90 grados
        self.btn_rotate90 = QPushButton("Rotar a 90º", self)
        self.btn_rotate90.setMinimumSize(QSize(130, 40))
        self.btn_rotate90.setStatusTip("Rotar imagen a 90 grados")
        self.btn_rotate90.setIcon(QIcon("rotate90.png"))
        self.btn_rotate90.clicked.connect(self.rotar_imagen90)

        #Boton Rotar 180 grados
        self.btn_rotate180 = QPushButton("Rotar a 180º", self)
        self.btn_rotate180.setMinimumSize(QSize(130, 40))
        self.btn_rotate180.setStatusTip("Rotar imagen a 180 grados")
        self.btn_rotate180.setIcon(QIcon("rotate180.png"))
        self.btn_rotate180.clicked.connect(self.rotar_imagen180)

        #Boton Rotar Horizontal
        self.btn_rotar_hor = QPushButton("Rotar Horizontal", self)
        self.btn_rotar_hor.setMinimumSize(QSize(130, 40))
        self.btn_rotar_hor.setStatusTip("Rotar imagen horizontalmente")
        self.btn_rotar_hor.setIcon(QIcon("rotatetohor.png"))
        self.btn_rotar_hor.clicked.connect(self.rotar_hor)

        #Boton Rotar Vertical
        self.btn_rotar_ver = QPushButton("Rotar Vertical", self)
        self.btn_rotar_ver.setMinimumSize(QSize(130, 40))
        self.btn_rotar_ver.setStatusTip("Rotar imagen verticalmente")
        self.btn_rotar_ver.setIcon(QIcon("rotatetovertical.png"))
        self.btn_rotar_ver.clicked.connect(self.rotar_ver)

        #Boton Redimensionar
        self.btn_resize = QPushButton("Redimensionar", self)
        self.btn_resize.setMinimumSize(QSize(130, 40))
        self.btn_resize.setStatusTip("Hacer el tamaño de la imagen a la mitad")
        self.btn_resize.setIcon(QIcon("resize.png"))
        self.btn_resize.clicked.connect(self.resize_imagen)

        #Boton de Salir
        self.btn_exit = QPushButton("Salir", self)
        self.btn_exit.setMinimumSize(QSize(130, 40))
        self.btn_exit.setStatusTip("Cerrar aplicación")
        self.btn_exit.setIcon(QIcon("exit.png"))
        self.btn_exit.clicked.connect(self.close)

        #Añadir los botones a un layout vertical
        vlyt_botones = QVBoxLayout()
        vlyt_botones.addWidget(self.btn_rotate90)
        vlyt_botones.addWidget(self.btn_rotate180)
        vlyt_botones.addStretch(1)
        vlyt_botones.addWidget(self.btn_rotar_hor)
        vlyt_botones.addWidget(self.btn_rotar_ver)
        vlyt_botones.addStretch(1)
        vlyt_botones.addWidget(self.btn_resize)
        vlyt_botones.addStretch(10)
        vlyt_botones.addWidget(self.btn_exit)

        #Añadir el layout al contenedor
        self.contenedor.setLayout(vlyt_botones)

        #Añadir el contenedor al muelle
        self.muelle_botones.setWidget(self.contenedor)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.muelle_botones)
        self.act_herramientas_muelle = self.muelle_botones.toggleViewAction()

    def crear_Menu(self):
        #Accion Abrir
        self.act_open = QAction(QIcon('open.png'), "Abrir", self)
        self.act_open.setShortcut("Ctrl+O")
        self.act_open.setStatusTip("Abrir una nueva imagen")
        self.act_open.triggered.connect(self.abrir_imagen)

        #Accion Guardar
        self.act_save = QAction(QIcon('save.png'), "Guardar", self)
        self.act_save.setShortcut("Ctrl+S")
        self.act_save.setStatusTip("Guardar imagen")
        self.act_save.triggered.connect(self.guardar_imagen)

        #Accion Imprimir
        self.act_print = QAction(QIcon('printer.png'), "Imprimir", self)
        self.act_print.setShortcut("Ctrl+P")
        self.act_print.setStatusTip("Imprimir imagen")
        self.act_print.triggered.connect(self.imprimir_imagen)

        #Accion Salir
        self.act_exit = QAction(QIcon('exit.png'), "Cerrar", self)
        self.act_exit.setShortcut("Ctrl+Q")
        self.act_exit.setStatusTip("Cerrar aplicación")
        self.act_exit.triggered.connect(self.close)

        #Accion Rotar 90 grados
        self.act_rotate90 = QAction(QIcon('rotate90.png'), "Rotar 90º", self)
        self.act_rotate90.setStatusTip("Rotar imagen a 90 grados")
        self.act_rotate90.triggered.connect(self.rotar_imagen90)

        #Accion Rotar 180 grados
        self.act_rotate180 = QAction(QIcon('rotate180.png'), "Rotar 180º", self)
        self.act_rotate180.setStatusTip("Rotar imagen a 180 grados")
        self.act_rotate180.triggered.connect(self.rotar_imagen180)

        #Accion Rotar en Horizontal
        self.act_rotar_hor = QAction(QIcon("rotatetohor.png"), "Rotar Horizontal", self)
        self.act_rotar_hor.setStatusTip("Rotar imagen en horizontal")
        self.act_rotar_hor.triggered.connect(self.rotar_hor)

        #Accion Rotar en Vertical
        self.act_rotar_ver = QAction(QIcon("rotatetovertical.png"), "Rotar Vertical", self)
        self.act_rotar_ver.setStatusTip("Rotar imagen en vertical")
        self.act_rotar_ver.triggered.connect(self.rotar_ver)

        #Accion Redimensionar Imagen
        self.act_resize = QAction(QIcon("resize.png"), "Redimensionar", self)
        self.act_resize.setStatusTip("Redimensionar a la mitad del tamaño")
        self.act_resize.triggered.connect(self.resize_imagen)

        #Accion Limpiar imagen
        self.act_clear = QAction(QIcon("clear.png"), "Limpiar", self)
        self.act_clear.setShortcut("Ctrl+D")
        self.act_clear.setStatusTip("Limpiar imagen actual")
        self.act_clear.triggered.connect(self.limpiar_imagen)

        #Crear barra de menu
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        menu_file = menu_bar.addMenu("Archivo")
        menu_file.addAction(self.act_open)
        menu_file.addAction(self.act_save)
        menu_file.addSeparator()
        menu_file.addAction(self.act_print)
        menu_file.addSeparator()
        menu_file.addAction(self.act_exit)

        menu_edit = menu_bar.addMenu("Edicion")
        menu_edit.addAction(self.act_rotate90)
        menu_edit.addAction(self.act_rotate180)
        menu_edit.addSeparator()
        menu_edit.addAction(self.act_rotar_hor)
        menu_edit.addAction(self.act_rotar_ver)
        menu_edit.addSeparator()
        menu_edit.addAction(self.act_resize)
        menu_edit.addSeparator()
        menu_edit.addAction(self.act_clear)

        menu_view = menu_bar.addMenu("Vista")
        menu_view.addAction(self.act_herramientas_muelle)

        self.setStatusBar(QStatusBar(self))

    def centrar_Menu(self):
        pass
    def crear_Barra_Herramientas(self):
        pass
    def widgets_edicion(self):
        pass

    def abrir_imagen(self):
        pass
    def guardar_imagen(self):
        pass
    def imprimir_imagen(self):
        pass
    def rotar_imagen90(self):
        pass
    def rotar_imagen180(self):
        pass
    def rotar_hor(self):
        pass
    def rotar_ver(self):
        pass
    def resize_imagen(self):
        pass
    def limpiar_imagen(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Editor()
    window.show()
    sys.exit(app.exec_())
