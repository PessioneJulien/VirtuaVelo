from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("oui ma page")
        self.label = QtWidgets.QLabel(self)
        self.StartButton = QtWidgets.QPushButton(self)
        self.initUI()

    def initUI(self):
        self.label.setText("wesh wesh")
        self.label.move(50, 50)

        self.StartButton.setText("le bouton")
        self.StartButton.move(150, 150)
        self.StartButton.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You clicked the button")
        self.Update()

    def Update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    win = Menu()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
