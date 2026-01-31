from qt.ui_main import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow

class FSTaggerClient(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)