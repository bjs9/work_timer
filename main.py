from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon


import config as c
import sys




# Создаём объект приложения (обязательный шаг для любого PySide6 GUI)
app = QApplication(sys.argv)

# Загружаем стили из внешнего файла
with open(f"{c.ASSETS_DIR}/style.qss", "r") as file:
    app.setStyleSheet(file.read())

# Создаём окно (родительский виджет)
window = QWidget()
window.setWindowTitle("Work Timer")
window.setWindowIcon(QIcon(f"{c.ASSETS_DIR}/icon.png"))

# Устанавливаем фиксированный размер окна
window.setFixedSize(400, 200)  # ширина: 400, высота: 200

# Отключаем кнопку "Развернуть на весь экран"
flags = Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint
window.setWindowFlags(flags)

# Создаём простой виджет — текстовую надпись
label = QLabel("Hello, World!", parent=window)
label.setAlignment(Qt.AlignCenter)  # Центрируем текст

# Показываем эту надпись в окне
window.show()

# Запускаем главный цикл приложения
sys.exit(app.exec())