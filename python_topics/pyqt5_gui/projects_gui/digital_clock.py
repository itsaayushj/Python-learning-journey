# digital clock in python 
# self code
import sys 
from PyQt5.QtWidgets import QMainWindow , QApplication , QLabel , QWidget , QVBoxLayout 
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import Qt , QTimer
import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600 , 200)
        self.setStyleSheet("background-color: black;")
        self.initui()
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_time)
        self.update_time()

    def initui(self):
        self.label = QLabel("00:00:00")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout1 = QVBoxLayout()
        central_widget.setLayout(layout1)
        layout1.addWidget(self.label ,alignment=(Qt.AlignCenter))

        self.label.setStyleSheet("color: #007c00;")
        self.label.setFont(QFont("Consolas" , 60))
        self.label.setAlignment(Qt.AlignCenter)
    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()