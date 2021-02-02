
#!/usr/bin/python

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Main Menu"
        self.left = 500
        self.top = 400
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.createLayout()
        self.show()

    def createLayout(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        Mainhbox = QHBoxLayout()
        Mainhbox.addStretch(0)
        Mainhbox.addWidget(okButton)
        Mainhbox.addWidget(cancelButton)

        self.setLayout(Mainhbox)


def main():
    app = QApplication(sys.argv)
    Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
