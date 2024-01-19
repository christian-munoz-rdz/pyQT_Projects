import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QMessageBox, QFileDialog

class Aplicacion(QWidget):
    def __init__(self):
        super(Aplicacion, self).__init__()
        self.initialize()

    def initialize(self):
        self.resize(300, 400)
        self.setWindowTitle("Notepad")
        self.displayWidgets()

    def displayWidgets(self):
        #Definir botones
        self.btn_clear = QPushButton('Clear', self)
        self.btn_clear.move(10, 20)

        self.btn_save = QPushButton('Save', self)
        self.btn_save.move(195, 20)

        self.btn_open = QPushButton('Open', self)
        self.btn_open.move(105, 20)

        #Definir editor de texto
        self.text_editor = QTextEdit(self)
        self.text_editor.resize(280, 330)
        self.text_editor.move(10, 60)

        #Conectar botones
        self.btn_clear.clicked.connect(self.clear_text)
        self.btn_save.clicked.connect(self.save_text)
        self.btn_open.clicked.connect(self.open_text)

    def clear_text(self):
        pregunta = QMessageBox.question(self, 'Clear', '¿Estas seguro que quieres borrar el texto?',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if pregunta == QMessageBox.Yes:
            self.text_editor.clear()
        else:
            pass

    def save_text(self):
        notepad_text = self.text_editor.toPlainText()
        ruta, tipo = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "ALLFILES(*);; Archivos de texto(*.txt)")

        try:
            with open(ruta, 'w') as f:
                f.write(notepad_text)
        except:
            pass

    def open_text(self):
        ruta, tipo = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "ALLFILES(*);; Archivos de texto(*.txt)")

        try:
            with open(ruta, 'r') as f:
                self.text_editor.setText(f.read())
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aplicacion()
    window.show()

    sys.exit(app.exec_())