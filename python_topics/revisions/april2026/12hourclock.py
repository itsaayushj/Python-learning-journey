import sys 
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QVBoxLayout 
from PyQt5.QtGui import QFont , QFontDatabase
from PyQt5.QtCore import Qt, QTime , QTimer

class digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600 , 200)
        self.initui()
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_time)
        self.update_time()
    def initui(self):
        self.setStyleSheet("background-color: black;")
        self.label = QLabel("00:00:00 AM")
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label.setStyleSheet("color: green;")
        layout.addWidget(self.label , alignment=(Qt.AlignCenter))
        font_id =QFontDatabase.addApplicationFont("pyqt5_gui/projects_gui/DS-DIGI.TTF")
        font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.label.setFont(QFont(font_name , 80))

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.label.setText(current_time)
def main():
    app = QApplication(sys.argv)
    clock = digital_clock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
