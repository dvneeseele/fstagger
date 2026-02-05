from db.FSTDBHandler import FSTDBHandler
from core.FSTFileHandler import FSTFileHandler
from qt.layouts.flowlayout import FlowLayout
from db.FSTDBHandler import File
from qt.ui_main import Ui_MainWindow
from PyQt6.QtCore import QThreadPool, QTimer, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtWidgets import QMainWindow, QWidget
from PyQt6.QtGui import QPixmap
from qt.widgets.thumb import Thumb
from qt.threading import loadingSignals, loadingWorker

class FSTaggerClient(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.database = FSTDBHandler()
        self.filehandler = FSTFileHandler()

        self.thumbLoadingPool = QThreadPool.globalInstance()

        # This should let the main window load before loading the default thumbnails.
        QTimer.singleShot(2, self.loadThumbs)

    # Just to create a test db with paths and images. no metadata, names, or details.
    def testImportFiles(self):
        test_list_files = self.filehandler.importFiles()
        self.database.testCreateFiles(test_list_files)


    def loadThumbs(self):
        # self.statusbar.showMessage('test message', 5000)
        self.progress_bar.setFormat("Loading files - %p%")
        all_files = self.database.getAllRecords(File)
        total_files = all_files.count()
        print(f"Total Files: {total_files}")
        self.progress_bar.setRange(1, total_files)
        
        total = 0
        for f in all_files:
            fs = f[0]
            self.thumbnail = Thumb()
            self.flow_layout.addWidget(self.thumbnail)

            loading_worker = loadingWorker(self.thumbnail, fs)
            loading_worker.loadingSignals.result.connect(self.loadingComplete)
            loading_worker.loadingSignals.started.connect(self.loadingStart)

            total += 1
            self.thumbLoadingPool.start(loading_worker)

    @Slot()
    def loadingStart(self):
        print("worker started")
    
    @Slot(QWidget, QPixmap)
    def loadingComplete(self, thumbwidget, pixmap):
        # Update the widget's pixmap from the thread and increment the progress bar.
        thumbwidget.updateImage(pixmap)
        pct = self.progress_bar.value() + 1
        self.progress_bar.setValue(pct)

        # print("Value: ", self.progress_bar.value())

