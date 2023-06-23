# coding: utf-8
from typing import List
from PyQt5.QtCore import Qt, pyqtSignal, QEasingCurve, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QFrame, QWidget

from qfluentwidgets import (NavigationInterface, NavigationItemPosition, MessageBox,
                            isDarkTheme, PopUpAniStackedWidget, qrouter)
from qfluentwidgets import FluentIcon as FIF

from .title_bar import CustomTitleBar
from .gallery_interface import GalleryInterface
from .home_interface import HomeInterface
from .basic_input_interface import BasicInputInterface
from .date_time_interface import DateTimeInterface
from .dialog_interface import DialogInterface
from .layout_interface import LayoutInterface
from .icon_interface import IconInterface
from .material_interface import MaterialInterface
from .menu_interface import MenuInterface
from .navigation_view_interface import NavigationViewInterface
from .scroll_interface import ScrollInterface
from .status_info_interface import StatusInfoInterface
from .setting_interface import SettingInterface, cfg
from .text_interface import TextInterface
from .view_interface import ViewInterface
from ..common.config import SUPPORT_URL
from ..components.avatar_widget import AvatarWidget
from ..components.frameless_window import FramelessWindow
from ..common.icon import Icon
from ..common.signal_bus import signalBus
from ..common.style_sheet import StyleSheet
from ..common import resource


class StackedWidget(QFrame):
    """ Stacked widget """

    currentWidgetChanged = pyqtSignal(QWidget)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.view = PopUpAniStackedWidget(self)

        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.view)

        self.view.currentChanged.connect(
            lambda i: self.currentWidgetChanged.emit(self.view.widget(i)))

    def addWidget(self, widget):
        """ add widget to view """
        self.view.addWidget(widget)

    def setCurrentWidget(self, widget, popOut=True):
        widget.verticalScrollBar().setValue(0)
        if not popOut:
            self.view.setCurrentWidget(widget, duration=300)
        else:
            self.view.setCurrentWidget(
                widget, True, False, 200, QEasingCurve.InQuad)

    def setCurrentIndex(self, index, popOut=False):
        self.setCurrentWidget(self.view.widget(index), popOut)


class MainWindow(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.setTitleBar(CustomTitleBar(self))
        self.hBoxLayout = QHBoxLayout(self)
        self.widgetLayout = QHBoxLayout()

        self.stackWidget = StackedWidget(self)
        self.navigationInterface = NavigationInterface(self, True, True)

        # create sub interface
        self.homeInterface = HomeInterface(self)
        self.rankInterface = ViewInterface(self)
        self.basicInputInterface = BasicInputInterface(self)
        self.materialInterface = MaterialInterface(self)
        self.settingInterface = SettingInterface(self)

        # self.iconInterface = IconInterface(self)
        # self.dateTimeInterface = DateTimeInterface(self)
        # self.dialogInterface = DialogInterface(self)
        # self.layoutInterface = LayoutInterface(self)
        # self.menuInterface = MenuInterface(self)
        # self.navigationViewInterface = NavigationViewInterface(self)
        # self.scrollInterface = ScrollInterface(self)
        # self.statusInfoInterface = StatusInfoInterface(self)
        # self.textInterface = TextInterface(self)

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addLayout(self.widgetLayout)
        self.hBoxLayout.setStretchFactor(self.widgetLayout, 1)

        self.widgetLayout.addWidget(self.stackWidget)
        self.widgetLayout.setContentsMargins(0, 48, 0, 0)

        signalBus.switchToSampleCard.connect(self.switchToSample)
        signalBus.supportSignal.connect(self.onSupport)

        self.navigationInterface.displayModeChanged.connect(
            self.titleBar.raise_)
        self.titleBar.raise_()

    def initNavigation(self):
        # add navigation items
        self.addSubInterface(
            self.homeInterface, 'homeInterface', FIF.HOME, self.tr('Home'), NavigationItemPosition.TOP)
        self.navigationInterface.addSeparator()

        self.addSubInterface(
            self.rankInterface, 'rankInterface', Icon.GRID, self.tr('Rank'))
        self.addSubInterface(
            self.basicInputInterface, 'styleInterface', FIF.CHECKBOX, self.tr('Style'))
        self.addSubInterface(
            self.materialInterface, 'commentInterface', FIF.PALETTE, self.tr('Comment'))
        
        # self.addSubInterface(
        #     self.iconInterface, 'iconInterface', Icon.EMOJI_TAB_SYMBOLS, self.tr('Icons'), NavigationItemPosition.TOP)
        # self.addSubInterface(
        #     self.dateTimeInterface, 'dateTimeInterface', FIF.DATE_TIME, self.tr('Date & time'))
        # self.addSubInterface(
        #     self.dialogInterface, 'dialogInterface', FIF.MESSAGE, self.tr('Dialogs'))
        # self.addSubInterface(
        #     self.layoutInterface, 'layoutInterface', FIF.LAYOUT, self.tr('Layout'))
        # self.addSubInterface(
        #     self.menuInterface, 'menuInterface', Icon.MENU, self.tr('Menus'))
        # self.addSubInterface(
        #     self.navigationViewInterface, 'navigationViewInterface', FIF.MENU, self.tr('Navigation'))
        # self.addSubInterface(
        #     self.scrollInterface, 'scrollInterface', FIF.SCROLL, self.tr('Scrolling'))
        # self.addSubInterface(
        #     self.statusInfoInterface, 'statusInfoInterface', FIF.CHAT, self.tr('Status & info'))
        # self.addSubInterface(
        #     self.textInterface, 'textInterface', Icon.TEXT, self.tr('Text'))

        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=AvatarWidget(r'app\resource\images\seattle.jpg'),
            onClick=self.onSupport,
            position=NavigationItemPosition.BOTTOM
        )
        self.addSubInterface(
            self.settingInterface, 'settingInterface', FIF.SETTING, self.tr('Settings'), NavigationItemPosition.BOTTOM)

        #!IMPORTANT: don't forget to set the default route key if you enable the return button
        qrouter.setDefaultRouteKey(self.stackWidget, self.homeInterface.objectName())

        self.stackWidget.currentWidgetChanged.connect(self.onCurrentWidgetChanged)
        self.navigationInterface.setCurrentItem(
            self.homeInterface.objectName())
        self.stackWidget.setCurrentIndex(0)

    def addSubInterface(self, interface: QWidget, objectName: str, icon, text: str, position=NavigationItemPosition.SCROLL):
        """ add sub interface """
        interface.setObjectName(objectName)
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=objectName,
            icon=icon,
            text=text,
            onClick=lambda t: self.switchTo(interface, t),
            position=position,
            tooltip=text
        )

    def initWindow(self):
        self.resize(1160, 780)
        self.setMinimumWidth(760)
        # self.setWindowIcon(QIcon(':/gallery/images/logo.png'))
        self.setWindowIcon(QIcon(r'app\resource\images\logo_red.png'))
        self.setWindowTitle('Melody Insights')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        StyleSheet.MAIN_WINDOW.apply(self)

    def switchTo(self, widget, triggerByUser=True):
        self.stackWidget.setCurrentWidget(widget, not triggerByUser)

    def onCurrentWidgetChanged(self, widget: QWidget):
        self.navigationInterface.setCurrentItem(widget.objectName())
        qrouter.push(self.stackWidget, widget.objectName())

    def resizeEvent(self, e):
        self.titleBar.move(46, 0)
        self.titleBar.resize(self.width()-46, self.titleBar.height())

    def onSupport(self):
        QDesktopServices.openUrl(QUrl(SUPPORT_URL))

    def switchToSample(self, routeKey, index):
        """ switch to sample """
        interfaces = self.findChildren(GalleryInterface)
        for w in interfaces:
            if w.objectName() == routeKey:
                self.stackWidget.setCurrentWidget(w, False)
                w.scrollToCard(index)
