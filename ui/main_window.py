from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, QTimer, QTime
from PySide6.QtGui import QIcon

import config as c




class MainWindow(QWidget):

    def __init__(self, show:bool=True) -> None:
        super().__init__()

        self.is_running: bool = False
        self.elapsed_time: QTime = QTime(0, 0, 0, 0)

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
        self.start_button.clicked.connect(self.toggle_timer)
        layout.addWidget(self.start_button)

        # QTimer
        self.timer = QTimer()
        self.timer.setInterval(10)  # каждые 10 мс
        self.timer.timeout.connect(self.update_timer)

        if show:
            self.show()


    def toggle_timer(self) -> None:
        if self.is_running:
            self.timer.stop()
            self.start_button.setText("Start")
            self.is_running = False
        else:
            self.elapsed_time = QTime(0, 0, 0, 0)
            self.timer.start()
            self.start_button.setText("Stop")
            self.is_running = True


    def update_timer(self) -> None:
        self.elapsed_time = self.elapsed_time.addMSecs(10)
        text = self.elapsed_time.toString("hh:mm:ss.zzz")[:-1]
        self.timer_label.setText(text)