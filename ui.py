from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from simulation2 import Ui_simulation
#from main_pyqt import AppWidget


class MyWindow(QMainWindow, Ui_simulation):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())