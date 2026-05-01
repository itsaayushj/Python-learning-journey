# stopwatch in python

#2nd way (tutorial)->

import sys 
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QVBoxLayout , QHBoxLayout , QPushButton , QWidget 
from PyQt5.QtCore import QTimer , QTime , Qt
from PyQt5.QtGui import QFont , QFontDatabase

class stopwatch(QWidget): 
    def __init__(self):
        super().__init__()
        self.resize(600 , 300)
        self.time = QTime( 0 , 0 , 0 , 0) # hour , minute , second , millisecond
        self.time_display = QLabel("00:00:00.00" , self)
        self.start_button = QPushButton("start" , self)
        self.stop_button = QPushButton("stop" , self)
        self.reset_button = QPushButton("reset" , self)
        self.timer = QTimer(self)
        self.initui()

    def initui(self):
        self.setWindowTitle("Stopwatch in python")
        self.time_display.setStyleSheet("background-color: #f9e2af; font-size: 100px")
        self.setStyleSheet("""QPushButton{
                           background-color: #fab387;
                           border: 2px solid;
                           font-size: 50px;
                           }
                           QPushButton:hover{
                           background-color: #fab420;
                           border: 2px solid;
                           font-size: 50px;
                           }""")
        font_id = QFontDatabase.addApplicationFont("D:/source/study stuff/python learning journey/python_topics/pyqt5_gui/projects_gui/DS-DIGI.TTF")
        myfont = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.time_display.setFont(QFont(myfont))
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.time_display , alignment=(Qt.AlignCenter))      
        self.setLayout(vbox)
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)
        self.start_button.clicked.connect(self.start_slot)
        self.stop_button.clicked.connect(self.stop_slot)
        self.reset_button.clicked.connect(self.reset_slot)
        self.timer.timeout.connect(self.update_display)
    def start_slot(self):
        self.timer.start(10) # interval of timeout every 10 ms
    def stop_slot(self):
        self.timer.stop()
    def reset_slot(self):
        self.time = QTime(0 , 0 , 0 ,0) #reseting the time
        self.time_display.setText(self.format_time(self.time))
        self.timer.stop()
    def format_time(self , time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10 # to get 2 digit ms not 3 digit default 
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}" # :02 to add 00 infront of them by default
    def update_display(self):
        self.time = self.time.addMSecs(10) # to add 10ms in time 
        self.time_display.setText(self.format_time(self.time))
def main():
    app = QApplication(sys.argv)
    window = stopwatch()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
