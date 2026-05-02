#stopwatch -> 
# my method 

import sys
from  PyQt5.QtWidgets import QMainWindow , QLabel , QWidget , QVBoxLayout , QHBoxLayout , QPushButton , QApplication
from PyQt5.QtCore import QTime , QTimer , Qt 

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700 , 300)
        self.initui()
        self.button_setter()
        self.time = QTime(0 , 0 , 0 ,0) # hour , minute , second , ms 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
    def initui(self):
        self.time_display = QLabel("00:00:00.00")
        self.play_pause_button = QPushButton("▶")
        self.reset_button = QPushButton("⯀")
        self.reset_button.setDisabled(True)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox.addWidget(self.time_display , alignment=(Qt.AlignCenter))
        self.setLayout(vbox)
        hbox.addWidget(self.reset_button)
        hbox.addWidget(self.play_pause_button)
        vbox.addLayout(hbox)
        #designs
        self.reset_button.setFixedSize(130 , 130)
        self.play_pause_button.setFixedSize(130 , 130)
        self.setStyleSheet(""" QWidget{background-color:        #1e1e2e;}                           
                           QPushButton{
                            font-size: 60px;
                            border: 1px solid;
                            border-radius: 65px;
                            background-color: #6c8196;
                            color: white;
                            border-color: #6c8196;
                           }
                           QPushButton:hover{
                           background-color: #475563;
    
                           }
                           QLabel{
                            font-family: Courier New;
                            font-size: 90px;
                            color: #cbcbcb;
                           font-weight: bold;
                           }
                           
                           """)
    def button_setter(self):
        self.play_pause_button.clicked.connect(self.play_pause_slot)
        self.reset_button.clicked.connect(self.reset_button_slot)
    def play_pause_slot(self):
        self.reset_button.setEnabled(True)
        if self.play_pause_button.text() == "▶":
            self.timer.start(10)
            self.play_pause_button.setText("ıı")
        elif self.play_pause_button.text() == "ıı":
            self.play_pause_button.setText("▶")
            self.timer.stop()
            
    def reset_button_slot(self):
        self.reset_button.setDisabled(True)
        self.play_pause_button.setText("▶")
        self.time = QTime(0 , 0, 0, 0)
        self.timer.stop()
        self.time_display.setText(self.time_format(self.time))
    
    def time_format(self , time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    
    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_display.setText(self.time_format(self.time))
def main():
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()