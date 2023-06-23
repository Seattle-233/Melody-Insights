# coding:utf-8
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QListWidgetItem, QFrame, QTreeWidgetItem, QHBoxLayout,
                             QTreeWidgetItemIterator, QTableWidgetItem)
from qfluentwidgets import TreeWidget, TableWidget, ListWidget

from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from ..common.style_sheet import StyleSheet
from module.api import*
from module.get_user_info import*
# from demo import*


class ViewInterface(GalleryInterface):
    """ View interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title=t.rank,
            subtitle="Do you want to know which song you have listened to the most?",
            parent=parent
        )
        # table view
        self.addExampleCard(
            title=self.tr('Your songs rank🎶'),
            widget=TableFrame(self),
            sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/table_view/demo.py'
        )

        # # list view
        # self.addExampleCard(
        #     title=self.tr('A simple ListView'),
        #     widget=ListFrame(self),
        #     sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/list_view/demo.py'
        # )


        # # tree view
        # frame = TreeFrame(self)
        # self.addExampleCard(
        #     title=self.tr('A simple TreeView'),
        #     widget=frame,
        #     sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/tree_view/demo.py'
        # )

        # frame = TreeFrame(self, True)
        # self.addExampleCard(
        #     title=self.tr('A TreeView with Multi-selection enabled'),
        #     widget=frame,
        #     sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/tree_view/demo.py'
        # )


class Frame(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setContentsMargins(0, 8, 0, 0)

        self.setObjectName('frame')
        StyleSheet.VIEW_INTERFACE.apply(self)

    def addWidget(self, widget):
        self.hBoxLayout.addWidget(widget)


class ListFrame(Frame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.listWidget = ListWidget(self)
        self.addWidget(self.listWidget)

        stands = [
            self.tr("Star Platinum"), self.tr("Hierophant Green"),
            self.tr("Made in Haven"), self.tr("King Crimson"),
            self.tr("Silver Chariot"), self.tr("Crazy diamond"),
            self.tr("Metallica"), self.tr("Another One Bites The Dust"),
            self.tr("Heaven's Door"), self.tr("Killer Queen"),
            self.tr("The Grateful Dead"), self.tr("Stone Free"),
            self.tr("The World"), self.tr("Sticky Fingers"),
            self.tr("Ozone Baby"), self.tr("Love Love Deluxe"),
            self.tr("Hermit Purple"), self.tr("Gold Experience"),
            self.tr("King Nothing"), self.tr("Paper Moon King"),
            self.tr("Scary Monster"), self.tr("Mandom"),
            self.tr("20th Century Boy"), self.tr("Tusk Act 4"),
            self.tr("Ball Breaker"), self.tr("Sex Pistols"),
            self.tr("D4C • Love Train"), self.tr("Born This Way"),
            self.tr("SOFT & WET"), self.tr("Paisley Park"),
            self.tr("Wonder of U"), self.tr("Walking Heart"),
            self.tr("Cream Starter"), self.tr("November Rain"),
            self.tr("Smooth Operators"), self.tr("The Matte Kudasai")
        ]
        for stand in stands:
            self.listWidget.addItem(QListWidgetItem(stand))

        self.setFixedSize(300, 380)


class TreeFrame(Frame):

    def __init__(self, parent=None, enableCheck=False):
        super().__init__(parent)
        self.tree = TreeWidget(self)
        self.addWidget(self.tree)

        item1 = QTreeWidgetItem([self.tr('JoJo 1 - Phantom Blood')])
        item1.addChildren([
            QTreeWidgetItem([self.tr('Jonathan Joestar')]),
            QTreeWidgetItem([self.tr('Dio Brando')]),
            QTreeWidgetItem([self.tr('Will A. Zeppeli')]),
        ])
        self.tree.addTopLevelItem(item1)

        item2 = QTreeWidgetItem([self.tr('JoJo 3 - Stardust Crusaders')])
        item21 = QTreeWidgetItem([self.tr('Jotaro Kujo')])
        item21.addChildren([
            QTreeWidgetItem(['空条承太郎']),
            QTreeWidgetItem(['空条蕉太狼']),
            QTreeWidgetItem(['阿强']),
            QTreeWidgetItem(['卖鱼强']),
            QTreeWidgetItem(['那个无敌的男人']),
        ])
        item2.addChild(item21)
        self.tree.addTopLevelItem(item2)
        self.tree.expandAll()
        self.tree.setHeaderHidden(True)

        self.setFixedSize(300, 380)

        if enableCheck:
            it = QTreeWidgetItemIterator(self.tree)
            while(it.value()):
                it.value().setCheckState(0, Qt.Unchecked)
                it += 1


class TableFrame(Frame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.table = TableWidget(self)
        self.addWidget(self.table)

        self.table.verticalHeader().hide()
        self.table.setColumnCount(5)
        self.table.setRowCount(100)
        self.table.setHorizontalHeaderLabels([
           self.tr('Rank'), self.tr('Title'), self.tr('Artist'),self.tr('Album'), self.tr('Playcount')
        ])


        # 读取CSV文件
        
        csv_filename = f"all_rank_data_{user.id}.csv"

        csv_filepath = os.path.join('rank_data', csv_filename)
        songInfos = user.read_rank(csv_filepath)

        songInfos += songInfos
        for i, songInfo in enumerate(songInfos):
            for j in range(5):
                self.table.setItem(i, j, QTableWidgetItem(songInfo[j]))

        self.setFixedSize(1400, 1100)
        self.table.resizeColumnsToContents()
