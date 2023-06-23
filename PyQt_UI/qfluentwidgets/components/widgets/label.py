# coding:utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QLabel


class PixmapLabel(QLabel):
    """ Label for high dpi pixmap """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__pixmap = QPixmap()

    def setPixmap(self, pixmap: QPixmap):
        self.__pixmap = pixmap
        self.setFixedSize(pixmap.size())
        self.update()

    def pixmap(self):
        return self.__pixmap

    def paintEvent(self, e):
        if self.__pixmap.isNull():
            return

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.SmoothPixmapTransform)
        painter.setPen(Qt.NoPen)
        painter.drawPixmap(self.rect(), self.__pixmap)
