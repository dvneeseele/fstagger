from PyQt6.QtCore import QRunnable, QObject, pyqtSignal as Signal, pyqtSlot as Slot, Qt
from PyQt6.QtWidgets import QLabel, QWidget
from PyQt6.QtGui import QPixmap
import time

class loadingSignals(QObject):
    started = Signal()
    result = Signal(QWidget, QPixmap)
    progress = Signal(int)

class loadingWorker(QRunnable):
    def __init__(self, thumbwidget, thumbpath):
        super().__init__()

        self.loadingSignals = loadingSignals()
        self.thumbnailWidget = thumbwidget
        self.filepath = thumbpath

    @Slot()
    def run(self):
        self.loadingSignals.started.emit()
        # time.sleep(3)
        try:
            pixmap = QPixmap(self.filepath)
            scaled = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.loadingSignals.result.emit(self.thumbnailWidget, scaled)
        except:
            print("Exception...")