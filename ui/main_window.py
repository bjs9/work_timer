from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

import config as c




class MainWindow(QWidget):

    def __init__(self, show:bool=True):
        super().__init__()

        # Window settings
        flags = Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint

        self.setWindowTitle(c.WINDOW_TITLE)
        self.setWindowIcon(QIcon(c.ICON_PATH))
        self.setFixedSize(c.WINDOW_WIDTH, c.WINDOW_HEIGHT)
        self.setWindowFlags(flags)

        # Layout for the window
        layout = QVBoxLayout()
        layout.setObjectName("MainLayout") # for qss
        self.setLayout(layout)

        # Main label with digits
        self.timer_label = QLabel("00:00:00.000")
        self.timer_label.setObjectName("TimerLabel") # for qss
        self.timer_label.setAlignment(Qt.AlignHCenter)
        # self.timer_label.setContentsMargins(0, 80, 0, 0)
        layout.addWidget(self.timer_label)

        if show:
            self.show()