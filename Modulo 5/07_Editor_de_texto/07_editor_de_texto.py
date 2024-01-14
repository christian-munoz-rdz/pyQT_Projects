from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QTextEdit, QFontDialog, QInputDialog, QFileDialog, QColorDialog
from PyQt5.QtGui import QIcon, QTextCursor, QColor
from PyQt5.QtCore import Qt
import sys

class Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 500)
        self.setWindowTitle('Editor de texto')

        self.widgets()
        self.menu()

    def widgets(self):
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

    def menu(self):
        # Acciones del menu de archivo
        new_act = QAction(QIcon('new.png'), 'Nuevo', self)
        new_act.setShortcut('Ctrl+N')
        new_act.triggered.connect(self.clear_text)

        open_act = QAction(QIcon('open.png'), 'Abrir', self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(self.open_file)

        save_act = QAction(QIcon('save.png'), 'Guardar', self)
        save_act.setShortcut('Ctrl+S')
        save_act.triggered.connect(self.save_file)

        exit_act = QAction(QIcon('exit.png'), 'Salir', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        # Acciones del menu de edicion
        undo_act = QAction(QIcon('undo.png'), 'Deshacer', self)
        undo_act.setShortcut('Ctrl+Z')
        undo_act.triggered.connect(self.text_edit.undo)

        redo_act = QAction(QIcon('redo.png'), 'Rehacer', self)
        redo_act.setShortcut('Ctrl+Shift+Z')
        redo_act.triggered.connect(self.text_edit.redo)

        cut_act = QAction(QIcon('cut.png'), 'Cortar', self)
        cut_act.setShortcut('Ctrl+X')
        cut_act.triggered.connect(self.text_edit.cut)

        copy_act = QAction(QIcon('copy.png'), 'Copiar', self)
        copy_act.setShortcut('Ctrl+C')
        copy_act.triggered.connect(self.text_edit.copy)

        paste_act = QAction(QIcon('paste.png'), 'Pegar', self)
        paste_act.setShortcut('Ctrl+V')
        paste_act.triggered.connect(self.text_edit.paste)

        find_act = QAction(QIcon('find.png'), 'Buscar', self)
        find_act.setShortcut('Ctrl+F')
        find_act.triggered.connect(self.find_action)

        # Acciones del menu de Herramientas
        font_act = QAction(QIcon('font.png'), 'Fuente', self)
        font_act.setShortcut('Ctrl+T')
        font_act.triggered.connect(self.choose_font)

        color_act = QAction(QIcon('color.png'), 'Color', self)
        color_act.setShortcut('Ctrl+Shift+C')
        color_act.triggered.connect(self.choose_color)

        highlight_act = QAction(QIcon('highlight.png'), 'Highlight', self)
        highlight_act.setShortcut('Ctrl+Shift+H')
        highlight_act.triggered.connect(self.choose_background_color)

        # Acciones del menu de Ayuda
        about_act = QAction('About', self)
        about_act.triggered.connect(self.about_dialog)

        # Barra de menu
        menu_bar = self.menuBar()

        # Menus
        # Menu de archivo
        file_menu = menu_bar.addMenu('Archivo')
        file_menu.addAction(new_act)
        file_menu.addSeparator()
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addSeparator()
        file_menu.addAction(exit_act)

        # Menu de edicion
        edit_menu = menu_bar.addMenu('Edicion')
        edit_menu.addAction(undo_act)
        edit_menu.addAction(redo_act)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_act)
        edit_menu.addAction(copy_act)
        edit_menu.addAction(paste_act)
        edit_menu.addSeparator()
        edit_menu.addAction(find_act)

        # Menu de herramientas
        tools_menu = menu_bar.addMenu('Herramientas')
        tools_menu.addAction(font_act)
        tools_menu.addAction(color_act)
        tools_menu.addAction(highlight_act)

        # Menu de ayuda
        help_menu = menu_bar.addMenu('Ayuda')
        help_menu.addAction(about_act)

    def open_file(self):
        try:
            name, ext = QFileDialog.getOpenFileName(self, 'Abrir archivo', '', 'HTML (*.html);; Text Files (*.txt)')

            if name:
                with open(name, 'r', encoding='utf-8') as f:
                    text = f.read()
                    self.text_edit.setText(text)
            else:
                QMessageBox.information(self, 'Error', 'No se ha seleccionado ningun archivo', QMessageBox.Ok)
        except:
            QMessageBox.information(self, 'Error', 'No se ha podido abrir el archivo', QMessageBox.Ok)

    def clear_text(self):
        answer = QMessageBox.question(self, 'Nuevo archivo', '¿Estas seguro de borrar el contenido para crear uno nuevo?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if answer == QMessageBox.Yes:
            self.text_edit.clear()
        else:
            pass

    def save_file(self):
        name, ext = QFileDialog.getSaveFileName(self, 'Guardar archivo', '', 'HTML (*.html);; Text Files (*.txt)')

        if name.endswith('.txt'):
            text = self.text_edit.toPlainText()

            with open(name, 'w', encoding='utf-8') as f:
                f.write(text)
        elif name.endswith('.html'):
            text = self.text_edit.toHtml()

            with open(name, 'w', encoding='utf-8') as f:
                f.write(text)

    def find_action(self):
        buscador, _ = QInputDialog.getText(self, 'Buscar', 'Buscar texto:')
        selecciones = []

        if _ and not self.text_edit.isReadOnly():
            self.text_edit.moveCursor(QTextCursor.Start)
            color = QColor(Qt.yellow)

            while self.text_edit.find(buscador):
                seleccion = QTextEdit.ExtraSelection()
                seleccion.format.setBackground(color)

                seleccion.cursor = self.text_edit.textCursor()

                selecciones.append(seleccion)

        for i in selecciones:
            self.text_edit.setExtraSelections(selecciones)

    def choose_font(self):
        actual = self.text_edit.currentFont()
        font, ok = QFontDialog.getFont(actual, self)

        if ok:
            self.text_edit.setCurrentFont(font)

    def choose_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.text_edit.setTextColor(color)

    def choose_background_color(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.text_edit.setTextBackgroundColor(color)

    def about_dialog(self):
        QMessageBox.about(self, 'Acerca de', 'Este es un editor de texto creado con PyQt5')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('noteblock.png'))
    window = Editor()
    window.show()

    sys.exit(app.exec_())


