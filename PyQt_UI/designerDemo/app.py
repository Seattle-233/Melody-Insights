import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

from demo_ui import Ui_Form

class Demo(QWidget, Ui_Form):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()