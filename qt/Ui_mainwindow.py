# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerVpwicU.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from qt.layouts.flowlayout import FlowLayout
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSplitter, QStatusBar,
    QVBoxLayout, QWidget, QScrollArea, QProgressBar)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2472, 1169)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.tagSidebarContainer = QWidget(self.splitter)
        self.tagSidebarContainer.setObjectName(u"tagSidebarContainer")
        self.verticalLayout = QVBoxLayout(self.tagSidebarContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.queryArea = QWidget(self.tagSidebarContainer)
        self.queryArea.setObjectName(u"queryArea")
        self.queryArea.setStyleSheet(u"background-color: gray")


        self.progress_bar = QProgressBar()

        self.verticalLayout.addWidget(self.queryArea)


        self.pushButton = QPushButton(self.tagSidebarContainer)
        self.pushButton.setObjectName(u"tagManagerBtn")

        self.verticalLayout.addWidget(self.pushButton)

        self.tagSearchBar = QLineEdit(self.tagSidebarContainer)
        self.tagSearchBar.setObjectName(u"tagSearchBar")

        self.verticalLayout.addWidget(self.tagSearchBar)

        self.tagList = QListWidget(self.tagSidebarContainer)
        self.tagList.setObjectName(u"tagList")

        self.verticalLayout.addWidget(self.tagList)

        self.splitter.addWidget(self.tagSidebarContainer)


        self.gallery = QWidget(self.splitter)
        self.gallery.setObjectName(u"gallery")
        self.splitter.addWidget(self.gallery)


        self.flow_layout = FlowLayout(self.gallery)
        self.gallery.setLayout(self.flow_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.gallery)
        self.vscrollbar = scroll_area.verticalScrollBar()
        # scroll_area.verticalScrollBar().valueChanged.connect()

        self.splitter.addWidget(scroll_area)


        self.fileSidebarContainer = QWidget(self.splitter)
        self.fileSidebarContainer.setObjectName(u"fileSidebarContainer")
        self.splitter.addWidget(self.fileSidebarContainer)

        # Sidebar takes up approx a quarter of the window
        self.splitter.setStretchFactor(0, 0) # left sidebar tags
        self.splitter.setStretchFactor(1, 1) # middle gallery area
        self.splitter.setStretchFactor(2, 0) # right sidebar file info

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2472, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.addWidget(self.progress_bar)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Tag Manager", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

