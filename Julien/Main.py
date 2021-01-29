from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QLabel)
import sys


class Menu(QWidget):

    def __init__(self):
        super().__init__()
        self.width = 1920
        self.height = 1080
        self.StartBtn = QPushButton('Choisir un Parcours', self)
        self.StatBtn = QPushButton('Statistiques', self)
        self.ConfigBtn = QPushButton('Statistiques', self)
        self.le = QLabel(self)
        self.initUI()

    def initUI(self):
        # Add button                                                                                                     
        self.StartBtn.setGeometry(round(self.width/10), round(self.height/5), self.width/3,round(self.height/7))

        self.StartBtn.clicked.connect(self.showDialog)

        # Add label
        self.le.move(30, 62)
        self.le.resize(400, 22)

        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter text:')
        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = app.primaryScreen().size()
    ex = Menu()
    sys.exit(app.exec_())
