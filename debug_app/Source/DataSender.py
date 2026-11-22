from PySide6.QtCore import QObject, Signal
import threading
import time


class DataSender(QObject):
    log_message = Signal(str)

    def __init__(self, port: str, rate: float, parent=None):
        super().__init__(parent)
        self.port = port
        self.rate = rate/1000

        self.timer = None
        self._stop_event = threading.Event()

    def change_settings(self, port: str, rate: float) -> None:
        self.port = port
        self.rate = rate/1000

    def start_sending(self) -> None:
        if self.timer is not None and self.timer.is_alive():
            self.log_message.emit("[ERROR] DataSender already running.")
            return

        self._stop_event.clear()
        self.timer = threading.Thread(target=self.send_data, daemon=True)
        self.timer.start()

    def send_data(self) -> None:
        self.log_message.emit(f"[DataSender] Start: port={self.port}, rate={self.rate}s")
        while not self._stop_event.is_set():
            self.send_once()
            if self._stop_event.wait(self.rate):
                break
        self.log_message.emit(f"[DataSender] Stopped: port={self.port}")

    def send_once(self) -> None:
        self.log_message.emit(f"[SEND] port={self.port} data=SAMPLE DATA at {time.strftime('%H:%M:%S')}")

    def stop_sending(self) -> None:
        self._stop_event.set()
        if self.timer is not None:
            self.timer.join(timeout=2.0)
            self.timer = None