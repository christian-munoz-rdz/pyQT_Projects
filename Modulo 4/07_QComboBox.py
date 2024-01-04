from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QSpinBox
from PyQt5.QtGui import QFont
from  PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.resize(250, 250)
        self.setWindowTitle("QComboBox")
        self.displayWidgets()

    def displayWidgets(self):
        self.lbl_titulo = QLabel("Escoge los articulos", self)
        self.lbl_titulo.setFont(QFont("Arial", 20))
        self.lbl_titulo.setAlignment(Qt.AlignCenter)

        self.lista_comida = {"Escoge producto": 0, "Huevo": 17, "Sandwich": 20, "Queso": 1,
                             "Platano": 8, "Naranja": 6, "Hot Cakes": 25, "Pan": 9,"Coca-cola": 15,
                             "Pepsi": 12, "Agua": 8}

        self.hlyt_combobox = QHBoxLayout()
        self.cobox_comida1 = QComboBox()
        self.cobox_comida2 = QComboBox()
        self.cobox_comida1.addItems(self.lista_comida)
        self.cobox_comida2.addItems(self.lista_comida)
        self.hlyt_combobox.addWidget(self.cobox_comida1)
        self.hlyt_combobox.addWidget(self.cobox_comida2)

        self.lbl_productos = QLabel("Escoge dos productos")

        self.lbl_total = QLabel("Total: $")
        self.lbl_total.setFont(QFont("Arial", 13))
        self.lbl_total.setAlignment(Qt.AlignRight)

        self.btn_pagar = QPushButton("Pagar")
        self.btn_pagar.close()

        self.spnbox1 = QSpinBox()
        self.spnbox2 = QSpinBox()
        self.spnbox1.setMaximum(10)
        self.spnbox2.setMaximum(10)
        self.spnbox1.setPrefix("Cantidad: ")
        self.spnbox2.setPrefix("Cantidad: ")
        hlyt_spinbox = QHBoxLayout()
        hlyt_spinbox.addWidget(self.spnbox1)
        hlyt_spinbox.addWidget(self.spnbox2)

        vlyt_principal = QVBoxLayout()
        vlyt_principal.addWidget(self.lbl_titulo)
        vlyt_principal.addLayout(self.hlyt_combobox)
        vlyt_principal.addLayout(hlyt_spinbox)
        vlyt_principal.addWidget(self.lbl_productos)
        vlyt_principal.addWidget(self.lbl_total)
        vlyt_principal.addWidget(self.btn_pagar)

        self.seleccion1 = ""
        self.seleccion2 = ""

        self.setLayout(vlyt_principal)

        self.cobox_comida1.activated[str].connect(self.escogido1)
        self.cobox_comida2.activated[str].connect(self.escogido2)
        self.spnbox1.valueChanged.connect(self.fun_seleccion)
        self.spnbox2.valueChanged.connect(self.fun_seleccion)

    def escogido1(self, seleccion):
        if seleccion != "Escoge producto":
            self.seleccion1 = seleccion
            self.fun_seleccion()

    def escogido2(self, seleccion):
        if seleccion != "Escoge producto":
            self.seleccion2 = seleccion
            self.fun_seleccion()

    def fun_seleccion(self):
        cantidad1 = self.spnbox1.value()
        cantidad2 = self.spnbox2.value()
        try:
            self.lbl_total.setText(f"Total: ${(self.lista_comida[self.seleccion1]*cantidad1) + (self.lista_comida[self.seleccion2]*cantidad2)}")
            self.lbl_productos.setText(f"Haz Escogido: {self.seleccion1} y {self.seleccion2}")
            self.btn_pagar.show()
        except:
            self.lbl_productos.setText("Escoge dos productos")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())