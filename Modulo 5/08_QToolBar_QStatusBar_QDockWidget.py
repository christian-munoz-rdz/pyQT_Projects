import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QStatusBar, QTextEdit, QDockWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt

class Aplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 400)
        self.setWindowTitle("Menu Básico 2")

        self.setCentralWidget(QTextEdit())

        self.crearMenu()
        self.crearToolBar()
        self.crearMuelle()

        self.setStatusBar(QStatusBar(self))

    def crearMenu(self):
        self.act_exit = QAction(QIcon('images/android.png'), 'Exit', self)
        self.act_exit.setStatusTip("Cerrar Aplicación")
        self.act_exit.setShortcut('Ctrl+Q')
        self.act_exit.triggered.connect(self.close)

        act_maximize = QAction('Maximize', self, checkable=True)
        act_maximize.setStatusTip("Maximizar Pantalla")
        act_maximize.setShortcut('F11')
        act_maximize.triggered.connect(self.maximize)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        menu_file = menu_bar.addMenu('Archivo')
        menu_file.addAction(self.act_exit)

        vista_menu = menu_bar.addMenu('Vista')
        sub_menu_apariencia = vista_menu.addMenu('Apariencia')
        sub_menu_apariencia.addAction(act_maximize)

    def maximize(self, state):
        if state:
            self.showMaximized()
        else:
            self.showNormal()

    def crearToolBar(self):
        tool_bar = QToolBar('Barra de Herramientas', self)
        tool_bar.setIconSize(QSize(32, 32))
        self.addToolBar(tool_bar)

        tool_bar.addAction(self.act_exit)

    def crearMuelle(self):
        muelle = QDockWidget("Ejemplo Muelle")
        muelle.setAllowedAreas(Qt.AllDockWidgetAreas)
        muelle.setWidget(QTextEdit())
        self.addDockWidget(Qt.LeftDockWidgetArea, muelle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()
    sys.exit(app.exec_())