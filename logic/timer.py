from PySide6.QtCore import QTime




class TimerModel:
    
    def __init__(self) -> None:
        self._elapsed_time: QTime = QTime()

    
    def reset(self) -> None:
        self._elapsed_time = QTime(0, 0, 0, 0)


    def add_milliseconds(self, ms: int) -> None:
        self._elapsed_time = self._elapsed_time.addMSecs(ms)


    def get_time_str(self) -> str:
        return self._elapsed_time.toString("hh:mm:ss.zzz")[:-1]  # "00:00:00.00"