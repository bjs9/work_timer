from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

import config as c




class MainWindow(QWidget):

    def __init__(self, show:bool=True):
        super().__init__()

        flags = Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint

        self.setWindowTitle(c.WINDOW_TITLE)
        self.setWindowIcon(QIcon(c.ICON_PATH))
        self.setFixedSize(c.WINDOW_WIDTH, c.WINDOW_HEIGHT)
        self.setWindowFlags(flags)

        label = QLabel("Hello, World!", parent=self)
        label.setAlignment(Qt.AlignCenter)

        if show:
            self.show()