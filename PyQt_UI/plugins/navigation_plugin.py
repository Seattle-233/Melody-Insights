# coding: utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin

from qfluentwidgets import NavigationInterface, NavigationPanel, Pivot

from plugin_base import PluginBase


class NavigationPlugin(PluginBase):

    def group(self):
        return super().group() + ' (Navigation)'


class NavigationInterfacePlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Navigation interface plugin """

    def createWidget(self, parent):
        return NavigationInterface(parent, True, True)

    def icon(self):
        return super().icon("NavigationView")

    def name(self):
        return "NavigationInterface"


class NavigationPanelPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Navigation panel plugin """

    def createWidget(self, parent):
        return NavigationPanel(parent)

    def icon(self):
        return super().icon("NavigationView")

    def name(self):
        return "NavigationPanel"


class PivotPlugin(NavigationPlugin, QPyDesignerCustomWidgetPlugin):
    """ Navigation panel plugin """

    def createWidget(self, parent):
        p = Pivot(parent)
        for i in range(1, 4):
            p.addItem(f'Item{i}', f'Item{i}', print)

        p.setCurrentItem('Item1')
        return p

    def icon(self):
        return super().icon("Pivot")

    def name(self):
        return "Pivot"
