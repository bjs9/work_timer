from PySide6.QtCore import QTimer

from logic.timer import TimerModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # Import only for type hinting to avoid circular imports
    # When using it as a type, wrap the class name in quotes: 'MainWindow'
    from ui.main_window import MainWindow

import config as c



class TimerPresenter:

    def __init__(self, view: 'MainWindow') -> None:
        self.view  = view
        self.model = TimerModel()
        self.timer = QTimer()
        self.timer.setInterval(c.TIMER_INTERVAL)
        self.timer.timeout.connect(self._on_tick)
        self.is_running = False

    
    def toggle(self) -> None:
        if self.is_running:
            self.timer.stop()
            self.view.update_button_text("START")
            self.is_running = False
        else:
            self.model.reset()
            self.timer.start()
            self.view.update_button_text("STOP")
            self.is_running = True

    
    def _on_tick(self) -> None:
        self.model.add_milliseconds(c.TIMER_INTERVAL)
        self.view.update_time_display(self.model.get_time_str())