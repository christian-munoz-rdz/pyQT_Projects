from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont, QPixmap
import sys

class PerfilUsuario(QWidget):

    def __init__(self):
        super(PerfilUsuario, self).__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setGeometry(100, 100, 300, 470)
        self.setWindowTitle('Perfil de usuario')
        self.mostrarImagenes()
        self.mostrarLabels()

    def mostrarImagenes(self):
        foto_perfil = r"C:\Users\itzel\OneDrive\Documentos\Christian\pyQT_Projects\resources\IMGCURSO\SECCION 2\profile_image.png"
        fondo = r"C:\Users\itzel\OneDrive\Documentos\Christian\pyQT_Projects\resources\IMGCURSO\SECCION 2\skyblue.jpg"

        try:
            with open(fondo):
                label_fondo = QLabel(self)
                pixmap = QPixmap(fondo)
                label_fondo.setPixmap(pixmap)

        except FileNotFoundError:
            print('Imagen no encontrada')

        try:
            with open(foto_perfil):
                label_foto = QLabel(self)
                pixmap = QPixmap(foto_perfil)
                label_foto.setPixmap(pixmap)
                label_foto.move(100, 25)

        except FileNotFoundError:
            print('Imagen no encontrada')

    def mostrarLabels(self):
        usuario = QLabel(self)
        usuario.setText('John Doe')
        usuario.move(100, 155)
        usuario.setFont(QFont('Arial', 17))

        biografia_title = QLabel(self)
        biografia_title.setText('Biografía:')
        biografia_title.move(15, 185)
        biografia_title.setFont(QFont('Arial', 17))

        biografia = QLabel(self)
        biografia.setText('Soy un desarrollador de software con 10 años de experiencia en el desarrollo de aplicaciones de escritorio y web.')
        biografia.move(15, 220)
        biografia.setWordWrap(True)

        skills_title = QLabel(self)
        skills_title.setText('Skills:')
        skills_title.move(15, 270)
        skills_title.setFont(QFont('Arial', 17))

        skills = QLabel(self)
        skills.setText('python | java | c++ | c# | php | javascript | html | css')
        skills.move(15, 300)
        skills.setWordWrap(True)

        experience_title = QLabel(self)
        experience_title.setText('Experiencia:')
        experience_title.move(15, 340)
        experience_title.setFont(QFont('Arial', 17))

        experience1 = QLabel(self)
        experience1.setText('Desarrollador de software en Acme Inc. (2010 - 2015)')
        experience1.move(15, 370)
        experience1.setWordWrap(True)

        experience2 = QLabel(self)
        experience2.setText('Desarrollador de software en ABC Inc. (2015 - 2020)')
        experience2.move(15, 400)
        experience2.setWordWrap(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PerfilUsuario()
    window.show()

    sys.exit(app.exec_())