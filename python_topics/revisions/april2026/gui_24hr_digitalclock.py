import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QWidget , QVBoxLayout 
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import Qt , QTimer
import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700 , 300)
        self.setStyleSheet("background-color: black;")
        self.initui()
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_time)
        self.update_time()
    def initui(self):
        self.label = QLabel("00:00:00" , self)
        self.label.setStyleSheet("color: green")
        self.label.setFont(QFont("Consolas" , 70))
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.addWidget(self.label , alignment=(Qt.AlignCenter))
        central_widget.setLayout(layout )
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