# coding:utf-8
from enum import Enum

from PyQt5.QtCore import Qt, QSize, QRectF
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtWidgets import (QSpinBox, QDoubleSpinBox, QToolButton, QHBoxLayout,
                             QDateEdit, QDateTimeEdit, QTimeEdit, QLineEdit, QAbstractSpinBox)

from ...common.style_sheet import FluentStyleSheet, themeColor
from ...common.icon import FluentIconBase, Theme, getIconColor
from ...common.font import setFont
from ...components.widgets import LineEditMenu


class SpinIcon(FluentIconBase, Enum):
    """ Spin icon """

    UP = "Up"
    DOWN = "Down"

    def path(self, theme=Theme.AUTO):
        return f':/qfluentwidgets/images/spin_box/{self.value}_{getIconColor(theme)}.svg'



class SpinButton(QToolButton):

    def __init__(self, icon: SpinIcon, parent=None):
        super().__init__(parent=parent)
        self.isPressed = False
        self._icon = icon
        self.setFixedSize(31, 23)
        self.setIconSize(QSize(10, 10))
        FluentStyleSheet.SPIN_BOX.apply(self)

    def mousePressEvent(self, e):
        self.isPressed = True
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        self.isPressed = False
        super().mouseReleaseEvent(e)

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.SmoothPixmapTransform)

        if self.isPressed:
            painter.setOpacity(0.7)

        self._icon.render(painter, QRectF(10, 9, 11, 11))


class Ui_SpinBox:
    """ Spin box ui """

    def __init__(self, *args, **kwargs):
        pass

    def _setUpUi(self):
        FluentStyleSheet.SPIN_BOX.apply(self)
        self.setButtonSymbols(QSpinBox.NoButtons)
        self.setFixedHeight(33)
        setFont(self)

        self.hBoxLayout = QHBoxLayout(self)
        self.upButton = SpinButton(SpinIcon.UP, self)
        self.downButton = SpinButton(SpinIcon.DOWN, self)

        self.hBoxLayout.setContentsMargins(0, 4, 4, 4)
        self.hBoxLayout.setSpacing(5)
        self.hBoxLayout.addWidget(self.upButton, 0, Qt.AlignRight)
        self.hBoxLayout.addWidget(self.downButton, 0, Qt.AlignRight)
        self.hBoxLayout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        self.upButton.clicked.connect(self.stepUp)
        self.downButton.clicked.connect(self.stepDown)

        self.setAttribute(Qt.WA_MacShowFocusRect, False)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._showContextMenu)

    def _showContextMenu(self, pos):
        menu = LineEditMenu(self.lineEdit())
        menu.exec_(self.mapToGlobal(pos))

    def _drawBorderBottom(self):
        if not self.hasFocus():
            return

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        w, h = self.width(), self.height()
        path.addRoundedRect(QRectF(0, h-10, w, 10), 5, 5)

        rectPath = QPainterPath()
        rectPath.addRect(0, h-10, w, 8)
        path = path.subtracted(rectPath)

        painter.fillPath(path, themeColor())


class SpinBox(QSpinBox, Ui_SpinBox):
    """ Spin box """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._setUpUi()

    def paintEvent(self, e):
        super().paintEvent(e)
        self._drawBorderBottom()


class DoubleSpinBox(QDoubleSpinBox, Ui_SpinBox):
    """ Double spin box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setUpUi()

    def paintEvent(self, e):
        super().paintEvent(e)
        self._drawBorderBottom()


class TimeEdit(QTimeEdit, Ui_SpinBox):
    """ Time edit """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setUpUi()

    def paintEvent(self, e):
        super().paintEvent(e)
        self._drawBorderBottom()


class DateTimeEdit(QDateTimeEdit, Ui_SpinBox):
    """ Date time edit """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setUpUi()

    def paintEvent(self, e):
        super().paintEvent(e)
        self._drawBorderBottom()


class DateEdit(QDateEdit, Ui_SpinBox):
    """ Date edit """

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setUpUi()

    def paintEvent(self, e):
        super().paintEvent(e)
        self._drawBorderBottom()

