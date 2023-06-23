# coding: utf-8
from enum import Enum

from PyQt5.QtCore import Qt, QTimer, pyqtProperty, pyqtSignal, QEvent, QPoint
from PyQt5.QtGui import QColor, QPainter, QHoverEvent
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QToolButton, QWidget

from ...common.style_sheet import FluentStyleSheet
from ...common.overload import singledispatchmethod


class Indicator(QToolButton):
    """ Indicator of switch button """

    checkedChanged = pyqtSignal(bool)

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setCheckable(True)
        super().setChecked(False)
        self.resize(37, 16)
        self.__sliderOnColor = QColor(Qt.white)
        self.__sliderOffColor = QColor(Qt.black)
        self.__sliderDisabledColor = QColor(QColor(155, 154, 153))
        self.timer = QTimer(self)
        self.padding = self.height()//4
        self.sliderX = self.padding
        self.sliderRadius = (self.height()-2*self.padding)//2
        self.sliderEndX = self.width()-2*self.sliderRadius
        self.sliderStep = self.width()/50
        self.timer.timeout.connect(self.__updateSliderPos)

    def __updateSliderPos(self):
        """ update slider position """
        if self.isChecked():
            if self.sliderX+self.sliderStep < self.sliderEndX:
                self.sliderX += self.sliderStep
            else:
                self.sliderX = self.sliderEndX
                self.timer.stop()
        else:
            if self.sliderX-self.sliderStep > self.sliderEndX:
                self.sliderX -= self.sliderStep
            else:
                self.sliderX = self.padding
                self.timer.stop()

        self.style().polish(self)

    def setChecked(self, isChecked: bool):
        """ set checked state """
        if isChecked == self.isChecked():
            return

        super().setChecked(isChecked)
        self.sliderRadius = (self.height()-2*self.padding)//2
        self.sliderEndX = self.width()-2*self.sliderRadius - \
            self.padding if isChecked else self.padding
        self.timer.start(5)

    def toggle(self):
        self.setChecked(not self.isChecked())

    def mouseReleaseEvent(self, e):
        """ toggle checked state when mouse release"""
        super().mouseReleaseEvent(e)
        self.sliderEndX = self.width()-2*self.sliderRadius - \
            self.padding if self.isChecked() else self.padding
        self.timer.start(5)
        self.checkedChanged.emit(self.isChecked())

    def resizeEvent(self, e):
        self.padding = self.height()//4
        self.sliderRadius = (self.height()-2*self.padding)//2
        self.sliderStep = self.width()/50
        self.sliderEndX = self.width()-2*self.sliderRadius - \
            self.padding if self.isChecked() else self.padding
        self.update()

    def paintEvent(self, e):
        """ paint indicator """
        # the background and border are specified by qss
        super().paintEvent(e)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        if self.isEnabled():
            color = self.sliderOnColor if self.isChecked() else self.sliderOffColor
        else:
            color = self.sliderDisabledColor

        painter.setBrush(color)
        painter.drawEllipse(int(self.sliderX), int(self.padding),
                            self.sliderRadius*2, self.sliderRadius*2)

    def getSliderOnColor(self):
        return self.__sliderOnColor

    def setSliderOnColor(self, color: QColor):
        self.__sliderOnColor = color
        self.update()

    def getSliderOffColor(self):
        return self.__sliderOffColor

    def setSliderOffColor(self, color: QColor):
        self.__sliderOffColor = color
        self.update()

    def getSliderDisabledColor(self):
        return self.__sliderDisabledColor

    def setSliderDisabledColor(self, color: QColor):
        self.__sliderDisabledColor = color
        self.update()

    sliderOnColor = pyqtProperty(QColor, getSliderOnColor, setSliderOnColor)
    sliderOffColor = pyqtProperty(QColor, getSliderOffColor, setSliderOffColor)
    sliderDisabledColor = pyqtProperty(
        QColor, getSliderDisabledColor, setSliderDisabledColor)


class IndicatorPosition(Enum):
    """ Indicator position """
    LEFT = 0
    RIGHT = 1


class SwitchButton(QWidget):
    """ Switch button class """

    checkedChanged = pyqtSignal(bool)

    @singledispatchmethod
    def __init__(self, parent: QWidget = None, indicatorPos=IndicatorPosition.LEFT):
        """
        Parameters
        ----------
        parent: QWidget
            parent widget

        indicatorPosition: IndicatorPosition
            the position of indicator
        """
        super().__init__(parent=parent)
        self._text = self.tr('Off')
        self._offText =  self.tr('Off')
        self._onText =  self.tr('On')
        self.__spacing = 12
        self.indicatorPos = indicatorPos
        self.hBox = QHBoxLayout(self)
        self.indicator = Indicator(self)
        self.label = QLabel(self._text, self)
        self.__initWidget()

    @__init__.register
    def _(self, text: str = 'Off', parent: QWidget = None, indicatorPos=IndicatorPosition.LEFT):
        """
        Parameters
        ----------
        text: str
            the text of switch button

        parent: QWidget
            parent widget

        indicatorPosition: IndicatorPosition
            the position of indicator
        """
        self.__init__(parent, indicatorPos)
        self._offText = text
        self.setText(text)

    def __initWidget(self):
        """ initialize widgets """
        self.setAttribute(Qt.WA_StyledBackground)
        self.setFixedHeight(37)
        self.installEventFilter(self)

        # set layout
        self.hBox.setSpacing(self.__spacing)
        self.hBox.setContentsMargins(2, 0, 0, 0)

        if self.indicatorPos == IndicatorPosition.LEFT:
            self.hBox.addWidget(self.indicator)
            self.hBox.addWidget(self.label)
            self.hBox.setAlignment(Qt.AlignLeft)
        else:
            self.hBox.addWidget(self.label, 0, Qt.AlignRight)
            self.hBox.addWidget(self.indicator, 0, Qt.AlignRight)
            self.hBox.setAlignment(Qt.AlignRight)

        # set default style sheet
        FluentStyleSheet.SWITCH_BUTTON.apply(self)

        # connect signal to slot
        self.indicator.toggled.connect(self._updateText)
        self.indicator.toggled.connect(self.checkedChanged)

    def eventFilter(self, obj, e: QEvent):
        if obj is self:
            if e.type() == QEvent.MouseButtonPress:
                self.indicator.setDown(True)
            elif e.type() == QEvent.MouseButtonRelease:
                self.indicator.setDown(False)
                self.indicator.toggle()
            elif e.type() == QEvent.Enter:
                self.indicator.setAttribute(Qt.WA_UnderMouse, True)
                e = QHoverEvent(QEvent.HoverEnter, QPoint(), QPoint(1, 1))
                QApplication.sendEvent(self.indicator, e)
            elif e.type() == QEvent.Leave:
                self.indicator.setAttribute(Qt.WA_UnderMouse, False)
                e = QHoverEvent(QEvent.HoverLeave, QPoint(1, 1), QPoint())
                QApplication.sendEvent(self.indicator, e)

        return super().eventFilter(obj, e)

    def isChecked(self):
        return self.indicator.isChecked()

    def setChecked(self, isChecked):
        """ set checked state """
        self._updateText()
        self.indicator.setChecked(isChecked)

    def toggleChecked(self):
        """ toggle checked state """
        self.indicator.setChecked(not self.indicator.isChecked())

    def _updateText(self):
        self.setText(self.onText if self.isChecked() else self.offText)
        self.adjustSize()

    def getText(self):
        return self._text

    def setText(self, text):
        self._text = text
        self.label.setText(text)
        self.adjustSize()

    def getSpacing(self):
        return self.__spacing

    def setSpacing(self, spacing):
        self.__spacing = spacing
        self.hBox.setSpacing(spacing)
        self.update()

    def getOnText(self):
        return self._onText

    def setOnText(self, text):
        self._onText = text
        self._updateText()

    def getOffText(self):
        return self._offText

    def setOffText(self, text):
        self._offText = text
        self._updateText()

    spacing = pyqtProperty(int, getSpacing, setSpacing)
    checked = pyqtProperty(bool, isChecked, setChecked)
    text = pyqtProperty(str, getText, setText)
    onText = pyqtProperty(str, getOnText, setOnText)
    offText = pyqtProperty(str, getOffText, setOffText)