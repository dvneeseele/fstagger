from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Thumb(QWidget):
    def __init__(self, thumbnail_path=None):
        super().__init__()

        self.isSelected = False
        self.color = ''
        self.thumbnail = QLabel()
        self.thumbnail_path = thumbnail_path
        # test image for loading
        self.default_thumbnail = './test_images/loading.png'
        self.thumb_layout = QVBoxLayout()
        self.setStyleSheet("background-color: #45475a")
        self.initUI()

    
    def initUI(self):
        # For now just working on the widget to load the thumbnail for images.
        self.setThumbnailImage()
        self.setLayout(self.thumb_layout)

    def setDefaultThumb(self):
        # No thumbnail cache yet.
        print("using loading thumbnail image")
        img = QPixmap(self.default_thumbnail)
        img_scaled = img.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.thumbnail.setScaledContents(True)
        self.thumbnail.setPixmap(img_scaled)
        self.thumb_layout.addWidget(self.thumbnail)

    def setThumbnailImage(self):
        print(self.thumbnail_path)
        if self.thumbnail_path == None:
            img = QPixmap(self.default_thumbnail)
            img_scaled = img.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.thumbnail.setScaledContents(True)
            self.thumbnail.setPixmap(img_scaled)
            self.thumb_layout.addWidget(self.thumbnail)
        else:
            print("thumbnail was passed")
            print(self.thumbnail_path)
            img = QPixmap(self.thumbnail_path)
            img_scaled = img.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.thumbnail.setScaledContents(True)
            self.thumbnail.setPixmap(img_scaled)
            self.thumb_layout.addWidget(self.thumbnail)

