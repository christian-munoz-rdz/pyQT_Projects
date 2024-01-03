from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.resize(300, 400)
        self.setWindowTitle("Encuesta")
        self.displayWidgets()

    def displayWidgets(self):
        lbl_titulo = QLabel("Encuesta del curso", self)
        lbl_titulo.setFont(QFont("Arial", 20))
        lbl_titulo.setAlignment(Qt.AlignCenter)

        lbl_pregunta = QLabel("¿Con que puntuación calificas el curso?", self)
        lbl_pregunta.setAlignment(Qt.AlignCenter)

        calificaciones = ["Muy malo", "Malo", "Bueno", "Muy Bueno"]
        hlyt_lbl_cal = QHBoxLayout()

        for cal in calificaciones:
            lbl_cal = QLabel(cal, self)
            hlyt_lbl_cal.addWidget(lbl_cal)

        hlyt_chbox = QHBoxLayout()
        grupo_chbox = QButtonGroup(self)

        for cal in range(len(calificaciones)):
            chbox = QCheckBox(str(cal+1), self)
            grupo_chbox.addButton(chbox)
            hlyt_chbox.addWidget(chbox)

        btn_close = QPushButton("Cerrar", self)
        btn_close.clicked.connect(self.close)
        grupo_chbox.buttonClicked.connect(self.clicked)

        vlyt_principal = QVBoxLayout()
        vlyt_principal.addWidget(lbl_titulo)
        vlyt_principal.addWidget(lbl_pregunta)
        vlyt_principal.addStretch(1)
        vlyt_principal.addLayout(hlyt_lbl_cal)
        vlyt_principal.addLayout(hlyt_chbox)
        vlyt_principal.addStretch(2)
        vlyt_principal.addWidget(btn_close)
        self.setLayout(vlyt_principal)

    def clicked(self, ch):
        print(f"La casilla seleccionada es: {ch.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())