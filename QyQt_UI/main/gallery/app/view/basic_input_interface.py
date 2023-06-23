# coding:utf-8
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QAction, QWidget, QVBoxLayout, QButtonGroup, QFrame, QHBoxLayout, QTableWidgetItem
from qfluentwidgets import (Action, DropDownPushButton, DropDownToolButton, PushButton, ToolButton, PrimaryPushButton,
                            HyperlinkButton, ComboBox, RadioButton, CheckBox, Slider, SwitchButton, EditableComboBox,
                            ToggleButton, RoundMenu, FluentIcon, SplitPushButton, SplitToolButton, PrimarySplitToolButton,
                            PrimarySplitPushButton, PrimaryDropDownPushButton, PrimaryToolButton, PrimaryDropDownToolButton,
                            TableWidget, TextEdit)

from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from ..common.style_sheet import StyleSheet
from module.get_user_info import*

# echarts test
from PyQt5.QtWebEngineWidgets import QWebEngineView

the_html_content ='''
<!DOCTYPE html>
<html>
<head>
  <title>Hello World</title>
</head>
<body>
  <h1>Hello World</h1>
</body>
</html>
        '''

class BasicInputInterface(GalleryInterface):
    """ Basic input interface """

    def __init__(self, parent=None):
        translator = Translator()
        super().__init__(
            title=translator.style,
            subtitle='The style of your favorite music is...',
            parent=parent
        )

        # hyperlink button
        self.addExampleCard(
            self.tr('Your Top5 Music Styles'),
            HyperlinkButton('http://127.0.0.1:5000', self.tr('Click Here to Reveal The Anwser!💖')),
            'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
        )

                # text edit
        textEdit = TextEdit(self)
        style, tagIDs = user.get_song_style()
        markdown = user.get_fav_style(tagIDs[0])
        textEdit.setMarkdown(
            markdown)
        textEdit.setFixedHeight(150)
        self.addExampleCard(
            title=self.tr("Your Favorite Music Style"),
            widget=textEdit,
            sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/line_edit/demo.py',
            stretch=1
        )

        self.addExampleCard(
            title=self.tr('Personalized recommendation for you!🎶'),
            widget=RecommendTableFrame(self),
            sourcePath='https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/table_view/demo.py'
        )

    #     # simple push button
    #     self.addExampleCard(
    #         self.tr('A simple button with text content'),
    #         PushButton(self.tr('Standard push button')),
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     # tool button
    #     button = ToolButton(':/gallery/images/kunkun.png')
    #     button.setIconSize(QSize(40, 40))
    #     button.resize(70, 70)
    #     self.addExampleCard(
    #         self.tr('A button with graphical content'),
    #         button,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     # primary color push button
    #     self.addExampleCard(
    #         self.tr('Accent style applied to push button'),
    #         PrimaryPushButton(self.tr('Accent style button')),
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     # primary color tool button
    #     self.addExampleCard(
    #         self.tr('Accent style applied to tool button'),
    #         PrimaryToolButton(FluentIcon.BASKETBALL),
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )


    #     # 2-state check box
    #     self.addExampleCard(
    #         self.tr('A 2-state CheckBox'),
    #         CheckBox(self.tr('Two-state CheckBox')),
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/check_box/demo.py'
    #     )

    #     # 3-state check box
    #     checkBox = CheckBox(self.tr('Three-state CheckBox'))
    #     checkBox.setTristate(True)
    #     self.addExampleCard(
    #         self.tr('A 3-state CheckBox'),
    #         checkBox,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/check_box/demo.py'
    #     )

    #     # combo box
    #     comboBox = ComboBox()
    #     comboBox.addItems(['shoko 🥰', '西宫硝子 😊', '一级棒卡哇伊的硝子酱 😘'])
    #     comboBox.setCurrentIndex(0)
    #     comboBox.setMinimumWidth(210)
    #     self.addExampleCard(
    #         self.tr('A ComboBox with items'),
    #         comboBox,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/combo_box/demo.py'
    #     )

    #     # editable combo box
    #     comboBox = EditableComboBox()
    #     comboBox.addItems([
    #         self.tr('Star Platinum'),
    #         self.tr('Crazy Diamond'),
    #         self.tr("Gold Experience"),
    #         self.tr('Sticky Fingers'),
    #     ])
    #     comboBox.setPlaceholderText(self.tr('Choose your stand'))
    #     comboBox.setMinimumWidth(210)
    #     self.addExampleCard(
    #         self.tr('An editable ComboBox'),
    #         comboBox,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/combo_box/demo.py'
    #     )

    #     # drop down button
    #     menu = RoundMenu(parent=self)
    #     menu.addAction(Action(FluentIcon.SEND, self.tr('Send')))
    #     menu.addAction(Action(FluentIcon.SAVE, self.tr('Save')))
    #     button = DropDownPushButton(self.tr('Email'), self, FluentIcon.MAIL)
    #     button.setMenu(menu)
    #     self.addExampleCard(
    #         self.tr('A push button with drop down menu'),
    #         button,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     button = DropDownToolButton(FluentIcon.MAIL, self)
    #     button.setMenu(menu)
    #     self.addExampleCard(
    #         self.tr('A tool button with drop down menu'),
    #         button,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     # primary color drop down button
    #     button = PrimaryDropDownPushButton(self.tr('Email'), self, FluentIcon.MAIL)
    #     button.setMenu(menu)
    #     self.addExampleCard(
    #         self.tr('A primary color push button with drop down menu'),
    #         button,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     button = PrimaryDropDownToolButton(FluentIcon.MAIL, self)
    #     button.setMenu(menu)
    #     self.addExampleCard(
    #         self.tr('A primary color tool button with drop down menu'),
    #         button,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     # radio button
    #     radioWidget = QWidget()
    #     radioLayout = QVBoxLayout(radioWidget)
    #     radioLayout.setContentsMargins(2, 0, 0, 0)
    #     radioLayout.setSpacing(15)
    #     radioButton1 = RadioButton(self.tr('Star Platinum'), radioWidget)
    #     radioButton2 = RadioButton(self.tr('Crazy Diamond'), radioWidget)
    #     radioButton3 = RadioButton(self.tr('Soft and Wet'), radioWidget)
    #     buttonGroup = QButtonGroup(radioWidget)
    #     buttonGroup.addButton(radioButton1)
    #     buttonGroup.addButton(radioButton2)
    #     buttonGroup.addButton(radioButton3)
    #     radioLayout.addWidget(radioButton1)
    #     radioLayout.addWidget(radioButton2)
    #     radioLayout.addWidget(radioButton3)
    #     radioButton1.click()
    #     self.addExampleCard(
    #         self.tr('A group of RadioButton controls in a button group'),
    #         radioWidget,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/radio_button/demo.py'
    #     )

    #     # horizontal slider
    #     slider = Slider(Qt.Horizontal)
    #     slider.setRange(0, 100)
    #     slider.setValue(30)
    #     slider.setMinimumWidth(200)
    #     self.addExampleCard(
    #         self.tr('A simple horizontal slider'),
    #         slider,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/slider/demo.py'
    #     )

    #     # split button
    #     button = SplitPushButton(self.tr('Choose your stand'), self, FluentIcon.BASKETBALL)
    #     button.setFlyout(self.createStandMenu(button))
    #     self.addExampleCard(
    #         self.tr('A split push button with drop down menu'),
    #         button,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     ikunMenu = RoundMenu(parent=self)
    #     ikunMenu.addActions([
    #         Action(self.tr('Sing')),
    #         Action(self.tr('Jump')),
    #         Action(self.tr("Rap")),
    #         Action(self.tr('Music')),
    #     ])
    #     button = SplitToolButton(":/gallery/images/kunkun.png", self)
    #     button.setIconSize(QSize(30, 30))
    #     button.setFlyout(ikunMenu)
    #     self.addExampleCard(
    #         self.tr('A split tool button with drop down menu'),
    #         button,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     # primary color split button
    #     button = PrimarySplitPushButton(self.tr('Choose your stand'), self, FluentIcon.BASKETBALL)
    #     button.setFlyout(self.createStandMenu(button))
    #     self.addExampleCard(
    #         self.tr('A primary color split push button with drop down menu'),
    #         button,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     button = PrimarySplitToolButton(FluentIcon.BASKETBALL, self)
    #     button.setFlyout(ikunMenu)
    #     self.addExampleCard(
    #         self.tr('A primary color split tool button with drop down menu'),
    #         button,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    #     # switch button
    #     self.switchButton = SwitchButton(self.tr('Off'))
    #     self.switchButton.checkedChanged.connect(self.onSwitchCheckedChanged)
    #     self.addExampleCard(
    #         self.tr('A simple switch button'),
    #         self.switchButton,
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/switch_button/demo.py'
    #     )

    #     # toggle button
    #     self.addExampleCard(
    #         self.tr('A simple ToggleButton with text content'),
    #         ToggleButton(self.tr('Start practicing'), self, FluentIcon.BASKETBALL),
    #         'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/button/demo.py'
    #     )

    # def onSwitchCheckedChanged(self, isChecked):
    #     if isChecked:
    #         self.switchButton.setText(self.tr('On'))
    #     else:
    #         self.switchButton.setText(self.tr('Off'))

    # def createStandMenu(self, button):
    #     menu = RoundMenu(parent=self)
    #     menu.addActions([
    #         Action(self.tr('Star Platinum'), triggered=lambda c, b=button: b.setText(self.tr('Star Platinum'))),
    #         Action(self.tr('Crazy Diamond'), triggered=lambda c, b=button: b.setText(self.tr('Crazy Diamond'))),
    #         Action(self.tr("Gold Experience"), triggered=lambda c, b=button: b.setText(self.tr("Gold Experience"))),
    #         Action(self.tr('Sticky Fingers'), triggered=lambda c, b=button: b.setText(self.tr('Sticky Fingers'))),
    #     ])
    #     return menu
    
class Frame(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.hBoxLayout.setContentsMargins(0, 8, 0, 0)

        self.setObjectName('frame')
        StyleSheet.VIEW_INTERFACE.apply(self)

    def addWidget(self, widget):
        self.hBoxLayout.addWidget(widget)

class RecommendTableFrame(Frame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.table = TableWidget(self)
        self.addWidget(self.table)

        self.table.verticalHeader().hide()
        self.table.setColumnCount(3)
        self.table.setRowCount(20)
        self.table.setHorizontalHeaderLabels([
            self.tr('Title'), self.tr('Artist'), self.tr('Album')
        ])


        # 读取CSV文件
        csv_filename = f"recommendation_{user.id}.csv"

        csv_filepath = os.path.join('recommendation_data', csv_filename)
        songInfos = user.read_recommendation(csv_filepath)

        songInfos += songInfos
        for i, songInfo in enumerate(songInfos):
            for j in range(3):
                self.table.setItem(i, j, QTableWidgetItem(songInfo[j]))

        self.setFixedSize(1000, 900)
        self.table.resizeColumnsToContents()