import sys
from PyQt6.QtWidgets import QApplication
from qt.client import FSTaggerClient

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = FSTaggerClient()
    main_win.show()
    sys.exit(app.exec())