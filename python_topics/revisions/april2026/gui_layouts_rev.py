import sys 
from PyQt5.QtWidgets import (QMainWindow , QApplication , QLabel , QWidget ,
                              QVBoxLayout , QHBoxLayout , QGridLayout)
from PyQt5.QtGui import QFont , QPixmap , QIcon 
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_gui()
        self.setGeometry(0 , 0 , 500 , 500)
    def init_gui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("1")
        label2 = QLabel("2")
        label3 = QLabel("3")
        label4 = QLabel("4")
        label5 = QLabel("5")
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__" : 
    main()