from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class EtiquetasPersonalizadas(QLabel):
    def __init__(self, vinculo, parent=None):
        super().__init__()
        self.setOpenExternalLinks(True)
        self.setText(vinculo)
        self.setParent(parent)
class Aplicacion(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar()

    def inicializar(self):
        self.setWindowTitle('Hipervínculo')
        self.mostrar_widgets()

    def mostrar_widgets(self):
        #lbl_facebook = QLabel("Facebook", self)
        #lbl_youtube = QLabel("YouTube", self)

        enlace_facebook = '<a href="https://www.facebook.com">Facebook</a>'
        enlace_youtube = '<a href="https://www.youtube.com">YouTube</a>'

        lbl_facebook = EtiquetasPersonalizadas(enlace_facebook, self)
        lbl_youtube = EtiquetasPersonalizadas(enlace_youtube, self)

        lbl_ico_fb = QLabel(self)
        lbl_ico_yt = QLabel(self)

        ruta_ico_fb = r'images/facebook.png'
        ruta_ico_yt = r'images/youtube.png'

        try:
            with open(ruta_ico_fb):
                pixmap = QPixmap(ruta_ico_fb)
                scaled_pixmap = pixmap.scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                lbl_ico_fb.setPixmap(scaled_pixmap)
            with open(ruta_ico_yt):
                pixmap = QPixmap(ruta_ico_yt)
                scaled_pixmap = pixmap.scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                lbl_ico_yt.setPixmap(scaled_pixmap)
        except FileNotFoundError:
            print('Error: No se pudo cargar la imagen.')

        hlyt_principal = QHBoxLayout(self)
        hlyt_principal.addStretch()
        hlyt_principal.addWidget(lbl_ico_fb)
        hlyt_principal.addWidget(lbl_facebook)
        hlyt_principal.addSpacing(2)
        hlyt_principal.addWidget(lbl_ico_yt)
        hlyt_principal.addWidget(lbl_youtube)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()

    sys.exit(app.exec_())
