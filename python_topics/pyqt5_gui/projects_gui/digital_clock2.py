# digital clock 
# tutorial video method 
import sys 
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QWidget , QVBoxLayout
from PyQt5.QtGui import QFont , QFontDatabase
from PyQt5.QtCore import Qt , QTimer , QTime


class digital_clock(QWidget): # insted of Qmainwindow we used Qwidget as it is more simple.
    def __init__(self): # self - clock 
        super().__init__()
        self.time_label = QLabel(self) 
        self.timer = QTimer()
        self.initui()
    def initui(self):
        self.setWindowTitle("Digital Clock in python")
        self.resize(800 , 300)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
                                      "color: green;")
        self.setStyleSheet("background-color: black")
        font_id = QFontDatabase.addApplicationFont("D:/source/study stuff/python learning journey/python_topics/pyqt5_gui/projects_gui/DS-DIGI.TTF") # this returns a id 
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0] #calling the 1st font in font family. this returns the font name
        myfont = QFont(font_family , 100)  # font size 
        self.time_label.setFont(myfont)

        self.timer.start(1000)
        self.timer.timeout.connect(self.update_time)
        self.update_time()
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") # formal for current time
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    clock = digital_clock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()