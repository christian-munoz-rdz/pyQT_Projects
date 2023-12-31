from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QCheckBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
from NewUser import RegistroUsuario

class LoginApp(QWidget):
    def __init__(self):
        super(LoginApp, self).__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle("Proyecto Final")
        self.loginInterfazUsuario()

    def loginInterfazUsuario(self):
        self.lbl_login = QLabel("Login", self)
        self.lbl_login.move(180, 10)
        self.lbl_login.setFont(QFont("Arial", 20))

        self.lbl_name = QLabel("Nombre", self)
        self.lbl_name.move(30, 60)

        self.lned_name = QLineEdit(self)
        self.lned_name.move(110, 60)
        self.lned_name.resize(220, 20)

        self.lbl_password = QLabel("Password", self)
        self.lbl_password.move(30, 90)

        self.lned_password = QLineEdit(self)
        self.lned_password.setEchoMode(QLineEdit.Password)
        self.lned_password.move(110, 90)
        self.lned_password.resize(220, 20)

        self.btn_login = QPushButton("Login", self)
        self.btn_login.move(100, 140)
        self.btn_login.resize(200, 40)

        self.chbx_spassword = QCheckBox("Mostrar contraseña", self)
        self.chbx_spassword.move(110, 115)
        self.chbx_spassword.setChecked(False)

        self.no_miembro = QLabel("¿Aún no eres miembro?", self)
        self.no_miembro.move(90, 195)
        self.no_miembro.setWordWrap(True)
        self.no_miembro.setFont(QFont("Arial", 7))

        self.btn_registro = QPushButton("Registrate", self)
        self.btn_registro.move(160, 195)

        # Eventos a los slots

        self.btn_registro.clicked.connect(self.registro_usuario)
        self.chbx_spassword.stateChanged.connect(self.show_password)
        self.btn_login.clicked.connect(self.click_login)

    def click_login(self):
        usuarios = {}

        try:
            with open("usuarios.txt") as f:
                for line in f:
                    campo_usuario = line.split(" ")
                    usuario = campo_usuario[0]
                    password = campo_usuario[1].rstrip("\n")
                    usuarios[usuario] = password
        except FileNotFoundError:
            f = ("usuarios.txt", "w")

        usuario = self.lned_name.text()
        password = self.lned_password.text()

        if (usuario, password) in usuarios.items():
            QMessageBox.information(self, "Inicio de sesion exitoso", "Inicio de sesion exitoso", QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Nombre de usuario o contraseña incorrectos", QMessageBox.Close,QMessageBox.Close)

    def show_password(self, state):
        if state == Qt.Checked:
            self.lned_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lned_password.setEchoMode(QLineEdit.Password)

    def registro_usuario(self):
        self.create_new_user = RegistroUsuario()
        self.create_new_user.show()

    def closeEvent(self, event):
        msg_cerrar = QMessageBox.question(self, "¿Cerar Aplicacion", "Estas Seguro que deseas Cerrar la Aplicacion?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if msg_cerrar == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# Correr el Programa
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()

    sys.exit(app.exec_())