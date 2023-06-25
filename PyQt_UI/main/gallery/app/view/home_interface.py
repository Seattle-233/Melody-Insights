# coding:utf-8
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPixmap, QPainter, QColor, QBrush, QPainterPath
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from qfluentwidgets import ScrollArea, isDarkTheme, FluentIcon
from ..common.config import cfg, HELP_URL, REPO_URL,  FEEDBACK_URL, BILI_URL
from ..common.icon import Icon, FluentIconBase
from ..components.link_card import LinkCardView
from ..components.sample_card import SampleCardView
from ..common.style_sheet import StyleSheet


class BannerWidget(QWidget):
    """ Banner widget """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFixedHeight(336)
        self.vBoxLayout = QVBoxLayout(self)
        self.galleryLabel = QLabel('Melody Insights', self)
        self.banner = QPixmap(':/gallery/images/header1.png')
        self.linkCardView = LinkCardView(self)

        self.galleryLabel.setObjectName('galleryLabel')

        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(0, 20, 0, 0)
        self.vBoxLayout.addWidget(self.galleryLabel)
        self.vBoxLayout.addWidget(self.linkCardView, 1, Qt.AlignBottom)
        self.vBoxLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.linkCardView.addCard(
            # ':/gallery/images/logo.png',
            r'app\resource\images\logo_red.png',
            self.tr('Getting started'),
            self.tr('An overview of Melody Insights.'),
            HELP_URL
        )

        self.linkCardView.addCard(
            FluentIcon.GITHUB,
            self.tr('GitHub repo'),
            self.tr(
                'The latest version of  Melody Insights.'),
            REPO_URL
        )


        self.linkCardView.addCard(
            FluentIcon.FEEDBACK,
            self.tr('Send feedback'),
            self.tr('Help us improve PyQt-Fluent-Widgets by providing feedback.'),
            FEEDBACK_URL
        )

        self.linkCardView.addCard(
            r'app\resource\images\bili.png',
            self.tr('Bilibili channel'),
            self.tr(
                'Contact me on Bilibili! Subscribe to my channel!'),
            BILI_URL
        )

        self.linkCardView.addCard(
            r'app\resource\images\silverwolf.png',
            self.tr('HACKED BY \nSILVER WOLF'),
            self.tr(
                '\"Return my 76 game accounts to me immediately!\"😡'),
            "https://www.bilibili.com/video/BV15o4y1u7pH"
        )
    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform | QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        w, h = self.width(), 200
        path.addRoundedRect(QRectF(0, 0, w, h), 10, 10)
        path.addRect(QRectF(0, h-50, 50, 50))
        path.addRect(QRectF(w-50, 0, 50, 50))
        path.addRect(QRectF(w-50, h-50, 50, 50))
        path = path.simplified()

        # draw background color
        if not isDarkTheme():
            painter.fillPath(path, QColor(206, 216, 228))
        else:
            painter.fillPath(path, QColor(0, 0, 0))

        # draw banner image
        pixmap = self.banner.scaled(
            self.size(), transformMode=Qt.SmoothTransformation)
        path.addRect(QRectF(0, h, w, self.height() - h))
        painter.fillPath(path, QBrush(pixmap))


class HomeInterface(ScrollArea):
    """ Home interface """

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.banner = BannerWidget(self)
        self.view = QWidget(self)
        self.vBoxLayout = QVBoxLayout(self.view)

        self.__initWidget()
        self.loadSamples()

    def __initWidget(self):
        self.view.setObjectName('view')
        StyleSheet.HOME_INTERFACE.apply(self)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidget(self.view)
        self.setWidgetResizable(True)

        self.vBoxLayout.setContentsMargins(0, 0, 0, 36)
        self.vBoxLayout.setSpacing(40)
        self.vBoxLayout.addWidget(self.banner)
        self.vBoxLayout.setAlignment(Qt.AlignTop)

    def loadSamples(self):
        """ load samples """
        # view samples
        collectionView = SampleCardView(self.tr('Top 100 Songs You Have Listened🎧'), self.view)
        collectionView.addSampleCard(
            icon=":/gallery/images/controls/DataGrid.png",
            title="Songs Ranking",
            content=self.tr(
                "The songs sorted by the number of times you have listened to them"),
            routeKey="rankInterface",
            index=0
        )
        self.vBoxLayout.addWidget(collectionView)

        # basic input samples
        basicInputView = SampleCardView(
            self.tr("The style of music you like🎵"), self.view)
        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/ColorPaletteResources.png",
            title="Top5 Music Styles",
            content=self.tr(
                "Clik the heyperlink button to see the top5 music styles you like."),
            routeKey="styleInterface",
            index=0
        )

        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/Sound.png",
            title="Favorite Music Style",
            content=self.tr(
                "A summary of your favorite music style."),
            routeKey="styleInterface",
            index=1
        )

        basicInputView.addSampleCard(
            icon=":/gallery/images/controls/Grid.png",
            title="Personalied Recommendation",
            content=self.tr(
                "The songs recommended for you based on your favorite music style."),
            routeKey="styleInterface",
            index=2
        )

        # basicInputView.addSampleCard(
        #     icon=":/gallery/images/controls/Checkbox.png",
        #     title="CheckBox",
        #     content=self.tr("A control that a user can select or clear."),
        #     routeKey="styleInterface",
        #     index=5
        # )
        # basicInputView.addSampleCard(
        #     icon=":/gallery/images/controls/ComboBox.png",
        #     title="ComboBox",
        #     content=self.tr(
        #         "A drop-down list of items a user can select from."),
        #     routeKey="basicInputInterface",
        #     index=7
        # )
        # basicInputView.addSampleCard(
        #     icon=":/gallery/images/controls/DropDownButton.png",
        #     title="DropDownButton",
        #     content=self.tr(
        #         "A button that displays a flyout of choices when clicked."),
        #     routeKey="basicInputInterface",
        #     index=9
        # )
        # basicInputView.addSampleCard(
        #     icon=":/gallery/images/controls/RadioButton.png",
        #     title="RadioButton",
        #     content=self.tr(
        #         "A control that allows a user to select a single option from a group of options."),
        #     routeKey="basicInputInterface",
        #     index=13
        # )
        # basicInputView.addSampleCard(
        #     icon=":/gallery/images/controls/Slider.png",
        #     title="Slider",
        #     content=self.tr(
        #         "A control that lets the user select from a range of values by moving a Thumb control along a track."),
        #     routeKey="basicInputInterface",
        #     index=14
        # )
        # basicInputView.addSampleCard(
        #     icon=":/gallery/images/controls/SplitButton.png",
        #     title="SplitButton",
        #     content=self.tr(
        #         "A two-part button that displays a flyout when its secondary part is clicked."),
        #     routeKey="basicInputInterface",
        #     index=15
        # )
        # basicInputView.addSampleCard(
        #     icon=":/gallery/images/controls/ToggleSwitch.png",
        #     title="SwitchButton",
        #     content=self.tr(
        #         "A switch that can be toggled between 2 states."),
        #     routeKey="basicInputInterface",
        #     index=19
        # )
        # basicInputView.addSampleCard(
        #     icon=":/gallery/images/controls/ToggleButton.png",
        #     title="ToggleButton",
        #     content=self.tr(
        #         "A button that can be switched between two states like a CheckBox."),
        #     routeKey="basicInputInterface",
        #     index=20
        # )
        self.vBoxLayout.addWidget(basicInputView)

        # material samples
        materialView = SampleCardView(self.tr('Comments of your favorite songs📝'), self.view)
        materialView.addSampleCard(
            icon=":/gallery/images/controls/Acrylic.png",
            title="Wordcloud of comments ",
            content=self.tr(
                "A wordcloud of your favorite songs\' comments."),
            routeKey="commentInterface",
            index=0
        )
        self.vBoxLayout.addWidget(materialView)

        # # date time samples
        # dateTimeView = SampleCardView(self.tr('Date & time samples'), self.view)
        # dateTimeView.addSampleCard(
        #     icon=":/gallery/images/controls/CalendarDatePicker.png",
        #     title="CalendarPicker",
        #     content=self.tr("A control that lets a user pick a date value using a calendar."),
        #     routeKey="dateTimeInterface",
        #     index=0
        # )
        # dateTimeView.addSampleCard(
        #     icon=":/gallery/images/controls/DatePicker.png",
        #     title="DatePicker",
        #     content=self.tr("A control that lets a user pick a date value."),
        #     routeKey="dateTimeInterface",
        #     index=2
        # )
        # dateTimeView.addSampleCard(
        #     icon=":/gallery/images/controls/TimePicker.png",
        #     title="TimePicker",
        #     content=self.tr(
        #         "A configurable control that lets a user pick a time value."),
        #     routeKey="dateTimeInterface",
        #     index=4
        # )
        # self.vBoxLayout.addWidget(dateTimeView)

        # # dialog samples
        # dialogView = SampleCardView(self.tr('Dialog samples'), self.view)
        # dialogView.addSampleCard(
        #     icon=":/gallery/images/controls/Flyout.png",
        #     title="Dialog",
        #     content=self.tr("A frameless message dialog."),
        #     routeKey="dialogInterface",
        #     index=0
        # )
        # dialogView.addSampleCard(
        #     icon=":/gallery/images/controls/ContentDialog.png",
        #     title="MessageBox",
        #     content=self.tr("A message dialog with mask."),
        #     routeKey="dialogInterface",
        #     index=1
        # )
        # dialogView.addSampleCard(
        #     icon=":/gallery/images/controls/ColorPicker.png",
        #     title="ColorDialog",
        #     content=self.tr("A dialog that allows user to select color."),
        #     routeKey="dialogInterface",
        #     index=2
        # )
        # self.vBoxLayout.addWidget(dialogView)

        # # layout samples
        # layoutView = SampleCardView(self.tr('Layout samples'), self.view)
        # layoutView.addSampleCard(
        #     icon=":/gallery/images/controls/Grid.png",
        #     title="FlowLayout",
        #     content=self.tr(
        #         "A layout arranges components in a left-to-right flow, wrapping to the next row when the current row is full."),
        #     routeKey="layoutInterface",
        #     index=0
        # )
        # self.vBoxLayout.addWidget(layoutView)

 

        # # menu samples
        # menuView = SampleCardView(self.tr('Menu samples'), self.view)
        # menuView.addSampleCard(
        #     icon=":/gallery/images/controls/MenuFlyout.png",
        #     title="RoundMenu",
        #     content=self.tr(
        #         "Shows a contextual list of simple commands or options."),
        #     routeKey="menuInterface",
        #     index=0
        # )
        # self.vBoxLayout.addWidget(menuView)

        # # navigation
        # navigationView = SampleCardView(self.tr('Navigation'), self.view)
        # navigationView.addSampleCard(
        #     icon=":/gallery/images/controls/Pivot.png",
        #     title="Pivot",
        #     content=self.tr(
        #         "Presents information from different sources in a tabbed view."),
        #     routeKey="navigationViewInterface",
        #     index=0
        # )
        # self.vBoxLayout.addWidget(navigationView)

        # # scroll samples
        # scrollView = SampleCardView(self.tr('Scrolling samples'), self.view)
        # scrollView.addSampleCard(
        #     icon=":/gallery/images/controls/ScrollViewer.png",
        #     title="ScrollArea",
        #     content=self.tr(
        #         "A container control that lets the user pan and zoom its content smoothly."),
        #     routeKey="scrollInterface",
        #     index=0
        # )
        # self.vBoxLayout.addWidget(scrollView)

        # # state info samples
        # stateInfoView = SampleCardView(self.tr('Status & info samples'), self.view)
        # stateInfoView.addSampleCard(
        #     icon=":/gallery/images/controls/ProgressRing.png",
        #     title="StateToolTip",
        #     content=self.tr(
        #         "Shows the apps progress on a task, or that the app is performing ongoing work that does block user interaction."),
        #     routeKey="statusInfoInterface",
        #     index=0
        # )
        # stateInfoView.addSampleCard(
        #     icon=":/gallery/images/controls/InfoBar.png",
        #     title="InfoBar",
        #     content=self.tr(
        #         "An inline message to display app-wide status change information."),
        #     routeKey="statusInfoInterface",
        #     index=3
        # )
        # stateInfoView.addSampleCard(
        #     icon=":/gallery/images/controls/ProgressBar.png",
        #     title="ProgressBar",
        #     content=self.tr(
        #         "Shows the apps progress on a task, or that the app is performing ongoing work that doesn't block user interaction."),
        #     routeKey="statusInfoInterface",
        #     index=7
        # )
        # stateInfoView.addSampleCard(
        #     icon=":/gallery/images/controls/ProgressRing.png",
        #     title="ProgressRing",
        #     content=self.tr(
        #         "Shows the apps progress on a task, or that the app is performing ongoing work that doesn't block user interaction."),
        #     routeKey="statusInfoInterface",
        #     index=9
        # )
        # stateInfoView.addSampleCard(
        #     icon=":/gallery/images/controls/ToolTip.png",
        #     title="ToolTip",
        #     content=self.tr(
        #         "Displays information for an element in a pop-up window."),
        #     routeKey="statusInfoInterface",
        #     index=1
        # )
        # self.vBoxLayout.addWidget(stateInfoView)

        # # text samples
        # textView = SampleCardView(self.tr('Text samples'), self.view)
        # textView.addSampleCard(
        #     icon=":/gallery/images/controls/TextBox.png",
        #     title="LineEdit",
        #     content=self.tr("A single-line plain text field."),
        #     routeKey="textInterface",
        #     index=0
        # )
        # textView.addSampleCard(
        #     icon=":/gallery/images/controls/NumberBox.png",
        #     title="SpinBox",
        #     content=self.tr(
        #         "A text control used for numeric input and evaluation of algebraic equations."),
        #     routeKey="textInterface",
        #     index=1
        # )
        
        # self.vBoxLayout.addWidget(textView)

