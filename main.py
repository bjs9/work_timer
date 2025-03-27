from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

import config as c
import sys




# Start
app = QApplication(sys.argv)

# Set window icon
with open(c.STYLE_PATH, "r") as file:
    app.setStyleSheet(file.read())

main_window = MainWindow()

# End
sys.exit(app.exec())