from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


import config as c
import sys




app = QApplication(sys.argv)

with open(c.STYLE_PATH, "r") as file:
    app.setStyleSheet(file.read())


flags = Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint

window = QWidget()
window.setWindowTitle(c.WINDOW_TITLE)
window.setWindowIcon(QIcon(c.ICON_PATH))
window.setFixedSize(c.WINDOW_WIDTH, c.WINDOW_HEIGHT)
window.setWindowFlags(flags)




label = QLabel("Hello, World!", parent=window)
label.setAlignment(Qt.AlignCenter)


window.show()


sys.exit(app.exec())