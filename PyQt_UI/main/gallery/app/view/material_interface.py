# coding:utf-8
from PyQt5.QtGui import QColor, QPixmap
from qfluentwidgets.components.widgets.acrylic_label import AcrylicLabel
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import PixmapLabel
from PyQt5.QtCore import Qt

from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from ..common.config import cfg
from module.get_user_info import*


class MaterialInterface(GalleryInterface):
    """ Material interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title=t.comment,
            subtitle='What do others think of your favorite songs?',
            parent=parent
        )

        # self.label = AcrylicLabel(
        #     0, QColor(105, 114, 168, 0))
        self.label = PixmapLabel(self)

        self.label.setPixmap(QPixmap(f'comment\wordcloud_{user.id}.png').scaled(
            775, 1000, Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))
        
        cfg.blurRadius.valueChanged.connect(self.onBlurRadiusChanged)

        self.addExampleCard(
            self.tr('Wordcloud of your favorite songs\' comments 💬💭💬'),
            self.label,
            'https://github.com/zhiyiYo/PyQt-Fluent-Widgets/blob/master/examples/acrylic_label/demo.py',
            stretch=1
        )

    def onBlurRadiusChanged(self, radius: int):
        self.label.blurRadius = radius
        self.label.setImage(':/gallery/images/chidanta.jpg')
