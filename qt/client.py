from db.FSTDBHandler import FSTDBHandler
from core.FSTFileHandler import FSTFileHandler
from qt.layouts.flowlayout import FlowLayout
from qt.ui_main import Ui_MainWindow
from PyQt6.QtCore import QThreadPool, QTimer, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtWidgets import QMainWindow


class FSTaggerClient(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.database = FSTDBHandler()
        self.filehandler = FSTFileHandler()

        # going to need threading for loading each file/widget
        self.thumbLoadingPool = QThreadPool.globalInstance()

        QTimer.singleShot(0, self.testImportFiles)

    # Just to create a test db with paths and images. no metadata, names, or details.
    def testImportFiles(self):
        test_list_files = self.filehandler.importFiles()
        self.database.testCreateFiles(test_list_files)



