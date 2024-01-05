from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QHBoxLayout, QSpinBox, QComboBox, QFormLayout, QTextEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Aplication(QWidget):
    def __init__(self):
        super(Aplication, self).__init__()
        self.resize(300, 400)
        self.setWindowTitle("Hospital Star")
        self.displayWidgets()

    def displayWidgets(self):
        lbl_titulo = QLabel("Cita Medica", self)
        lbl_titulo.setAlignment(Qt.AlignCenter)
        lbl_titulo.setFont(QFont("Arial", 18))

        #Line Edits
        self.lned_nombre = QLineEdit(self)
        self.lned_direccion = QLineEdit(self)
        self.lned_telefono = QLineEdit(self)
        self.lned_telefono.setInputMask("000-000-0000;")

        # Layout Edad, Altura, Peso
        hlyt_edades = QHBoxLayout()
        lbl_edad = QLabel("Edad")
        self.spnbox_edad = QSpinBox(self)
        self.spnbox_edad.setRange(1, 110)
        lbl_altura = QLabel("Altura", self)
        self.lned_altura = QLineEdit(self)
        self.lned_altura.setPlaceholderText("cm")
        lbl_peso = QLabel("Peso", self)
        self.lned_peso = QLineEdit(self)
        self.lned_peso.setPlaceholderText("kg")

        hlyt_edades.addWidget(lbl_edad)
        hlyt_edades.addWidget(self.spnbox_edad)
        hlyt_edades.addWidget(lbl_altura)
        hlyt_edades.addWidget(self.lned_altura)
        hlyt_edades.addWidget(lbl_peso)
        hlyt_edades.addWidget(self.lned_peso)

        # Combo Box Genero
        self.cobox_genero = QComboBox(self)
        self.cobox_genero.addItems(["Masculino", "Femenino", "No Binario"])

        # Text Edit
        self.txtedit_cita = QTextEdit(self)
        self.txtedit_cita.setPlaceholderText("Especifique su cita")

        #ComboBox Tipo de Sangre
        self.cobox_sangre = QComboBox(self)
        self.cobox_sangre.addItems(["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])

        # Layout Hora
        hlyt_hora = QHBoxLayout()
        self.spnbox_hora = QSpinBox(self)
        self.spnbox_hora.setRange(1, 12)
        self.cbox_minutos = QComboBox(self)
        self.cbox_minutos.addItems([":00", ":15", ":30", ":45"])
        self.cbox_am_pm = QComboBox(self)
        self.cbox_am_pm.addItems(["AM", "PM"])

        hlyt_hora.addWidget(self.spnbox_hora)
        hlyt_hora.addWidget(self.cbox_minutos)
        hlyt_hora.addWidget(self.cbox_am_pm)

        #Boton enviar formulario
        btn_enviar = QPushButton("Enviar datos", self)
        btn_enviar.clicked.connect(self.enviar)

        # Layout Principal del Formulario
        flyt_principal = QFormLayout(self)
        flyt_principal.addRow(lbl_titulo)
        flyt_principal.addRow("Nombre", self.lned_nombre)
        flyt_principal.addRow("Direccion", self.lned_direccion)
        flyt_principal.addRow("Telefono", self.lned_telefono)
        flyt_principal.addRow(hlyt_edades)
        flyt_principal.addRow("Genero", self.cobox_genero)
        flyt_principal.addRow("Cita", self.txtedit_cita)
        flyt_principal.addRow("Tipo de Sangre", self.cobox_sangre)
        flyt_principal.addRow("Hora", hlyt_hora)
        flyt_principal.addRow(btn_enviar)

    #Metodo que recibe los datos del formulario
    def enviar(self):
        print("Nombre:", self.lned_nombre.text())
        print("Direccion:", self.lned_direccion.text())
        print("Telefono:", self.lned_telefono.text())
        print("Edad:", self.spnbox_edad.value())
        print("Altura:", self.lned_altura.text())
        print("Peso:", self.lned_peso.text())
        print("Genero:", self.cobox_genero.currentText())
        print("Cita:", self.txtedit_cita.toPlainText())
        print("Tipo de Sangre:", self.cobox_sangre.currentText())
        print("Hora:", self.spnbox_hora.value(), self.cbox_minutos.currentText(), self.cbox_am_pm.currentText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Aplication()
    window.show()

    sys.exit(app.exec_())
