import sys 
from PyQt5.QtWidgets import QMainWindow , QApplication , QLabel
from PyQt5.QtGui import QIcon
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.setWindowIcon(QIcon("pyqt5_gui\\gui_icon.jpeg"))
        self.setGeometry(0 , 0 , 400 , 400)

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
#===========================Incomplete code===========================