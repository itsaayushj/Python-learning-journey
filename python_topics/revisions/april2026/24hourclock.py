import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QLabel , QWidget , QVBoxLayout
from PyQt5.QtCore import QTime , QTimer 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700 , 250)
        self.setWindowTitle("Digital clock!")
        self.initui()
    def initui(self):
        self.setStyleSheet("background-color: black;")
        self.mainlabel = QLabel()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(self.mainlabel)
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()