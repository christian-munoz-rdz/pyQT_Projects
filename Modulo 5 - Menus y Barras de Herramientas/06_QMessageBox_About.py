from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
import sys

class Aplication(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("About MessageBox")

            self.btn_dialog = QPushButton("Presioname", self)
            vlyt_principal = QVBoxLayout(self)
            vlyt_principal.addWidget(self.btn_dialog)

            self.btn_dialog.clicked.connect(self.presionado)

        def presionado(self):
            QMessageBox.about(self, "About", "Esto es un texto meramente informativo")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/android.png"))
    window = Aplication()
    window.show()
    sys.exit(app.exec_())