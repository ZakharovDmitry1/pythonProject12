import sys
from random import choice, randint
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPixmap
from PyQt5.QtWidgets import *
from PIL import Image


class MyWidget(QMainWindow, QSlider):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'untitled.ui', self)
        self.do_paint = False
        self.slider.valueChanged[int].connect(self.visibility)
        self.run()

    def visibility(self, p_int):
        print(p_int)
        im = Image.open('img.png')
        im.convert('RGBA')
        im.putalpha(int(255 * p_int / 100))
        im.save('img.png')
        self.label.setPixmap(QPixmap('img.png'))

    def run(self):
        self.slider.setValue(99)

    def valueChanged(self, p_int):
        print(p_int)
        return p_int


if __name__ == '__main__':
    im = Image.open('img2.png')
    im.save('img.png')
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
