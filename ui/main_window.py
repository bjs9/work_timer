from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from logic.presenter import TimerPresenter

import config as c




class MainWindow(QWidget):

    def __init__(self, show:bool=True) -> None:
        super().__init__()

        self.presenter = TimerPresenter(self)

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
        self.timer_label = QLabel("00:00:00.00")
        self.timer_label.setObjectName("TimerLabel") # for qss
        self.timer_label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.timer_label)

        # Start/Stop button
        self.start_button = QPushButton("Start")
        self.start_button.setObjectName("MainButton")
        self.start_button.clicked.connect(self.presenter.toggle)
        layout.addWidget(self.start_button)

        if show:
            self.show()


    def update_time_display(self, text: str) -> None:
        self.timer_label.setText(text)


    def update_button_text(self, text: str) -> None:
        self.start_button.setText(text)