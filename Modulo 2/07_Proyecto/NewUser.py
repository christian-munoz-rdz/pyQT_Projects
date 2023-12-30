from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import sys


class RegistroUsuario(QWidget):
    def __init__(self):
        super(RegistroUsuario, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Registro de Usuario")
        self.displayWidgets()

    def displayWidgets(self):
        user_Image = "nuevo_usuario.png"

        try:
            with open(user_Image):
                etiqueta_imagen = QLabel(self)
                pixmap = QPixmap(user_Image)
                etiqueta_imagen.setPixmap(pixmap)
                etiqueta_imagen.move(175, 80)
        except FileNotFoundError:
            print("No se pudo cargar la imagen")

        etiqueta_login = QLabel("Crear nueva cuenta",self)
        etiqueta_login.move(0, 20)
        etiqueta_login.setFont(QFont("Arial", 20))
        etiqueta_login.resize(400, 40)
        etiqueta_login.setAlignment(Qt.AlignCenter)

        #Etiquetas de Nombre de usuario y Nombre Completo
        self.etiqueta_nombre = QLabel("Nombre de usuario", self)
        self.etiqueta_nombre.move(30, 180)

        self.entrada_nombre = QLineEdit(self)
        self.entrada_nombre.move(150, 180)
        self.entrada_nombre.resize(200, 20)

        self.etiqueta_nombre = QLabel("Nombre completo", self)
        self.etiqueta_nombre.move(30, 210)

        self.entrada_completo = QLineEdit(self)
        self.entrada_completo.move(150, 210)
        self.entrada_completo.resize(200, 20)

        self.etiqueta_password = QLabel("Contraseña", self)
        self.etiqueta_password.move(30, 240)

        self.lned_password = QLineEdit(self)
        self.lned_password.setEchoMode(QLineEdit.Password)
        self.lned_password.move(150, 240)
        self.lned_password.resize(200, 20)

        self.confirmar = QLabel("Confirmar contraseña", self)
        self.confirmar.move(30, 270)

        self.lned_confirmar = QLineEdit(self)
        self.lned_confirmar.setEchoMode(QLineEdit.Password)
        self.lned_confirmar.move(150, 270)
        self.lned_confirmar.resize(200, 20)

        #Crear boton de registro
        self.boton_registro = QPushButton("Registrarse", self)
        self.boton_registro.resize(200, 40)
        self.boton_registro.move(100, 310)

        #Crear señal del boton
        self.boton_registro.clicked.connect(self.registro)

    def registro(self):
        texto_password = self.lned_password.text()
        password_confirmar = self.lned_confirmar.text()

        if self.entrada_nombre.text() == "" or self.entrada_completo.text() == "" or texto_password == "" or password_confirmar == "":
            QMessageBox.warning(self, "Error", "Hay campos vacios", QMessageBox.Ok, QMessageBox.Ok)
        elif texto_password != password_confirmar:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden. Por favor, intente de nuevo",
                                QMessageBox.Ok, QMessageBox.Ok)
        else:
            with open("usuarios.txt", "a+") as f:
                f.write(self.entrada_nombre.text() + " ")
                f.write(texto_password + "\n")
            self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistroUsuario()
    window.show()

    sys.exit(app.exec_()).exit(app.exec_())