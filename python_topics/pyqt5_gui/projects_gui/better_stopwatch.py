#stopwatch -> 
# my method 

import sys
from  PyQt5.QtWidgets import QMainWindow , QLabel , QWidget , QVBoxLayout , QHBoxLayout , QPushButton , QApplication
from PyQt5.QtCore import QTime , QTimer , Qt 
import json 

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("An outdated Stopwatch with features no one need")
        self.resize(800 , 400)
        self.initui()
        self.button_setter()
        self.time = QTime(0 , 0 , 0 ,0) # hour , minute , second , ms 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.total_pause_time = 0
        self.pause_start_time = None
        self.pause_time_label.setObjectName("pause_time_label")
        self.flag_display.setObjectName("bottom_display") # same name to history label too
        self.flags = []
        self.filepath = "pyqt5_gui/projects_gui/better_stopwatch_history.json"
        self.history_reader()
    def initui(self):
        self.history_display = QLabel("Just checking if its right")
        self.flag_display = QLabel()
        self.time_display = QLabel("00:00:00.00")
        self.play_pause_button = QPushButton("▶")
        self.reset_button = QPushButton("⯀")
        self.reset_button.setDisabled(True)
        self.pause_time_label = QLabel(" Total pause time - 00:00:00.00")
        self.flag_button = QPushButton("🏳️")
        self.flag_button.setDisabled(True)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox.addWidget(self.time_display , alignment=(Qt.AlignCenter))
        vbox.addWidget(self.pause_time_label , alignment=(Qt.AlignCenter))
    
        self.setLayout(vbox)
        hbox.addWidget(self.reset_button)
        hbox.addWidget(self.play_pause_button)
        hbox.addWidget(self.flag_button)
        vbox.addLayout(hbox)
        hbox2.addWidget(self.flag_display)
        hbox2.addWidget(self.history_display)
        vbox.addLayout(hbox2)
        #designs
        self.reset_button.setFixedSize(130 , 130)
        self.play_pause_button.setFixedSize(130 , 130)
        self.flag_button.setFixedSize(130 , 130)
        self.history_display.setObjectName("bottom_display")
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
                           QLabel#pause_time_label{
                        font-size: 20px
                           }
                           QLabel#bottom_display{
                        font-size: 20px
                           }
                           """)
    def button_setter(self):
        self.play_pause_button.clicked.connect(self.play_pause_slot)
        self.reset_button.clicked.connect(self.reset_button_slot)
        self.flag_button.clicked.connect(self.flag_button_slot)
    def play_pause_slot(self):
        self.reset_button.setEnabled(True)
        if self.play_pause_button.text() == "▶":
            if self.pause_start_time is not None :
                self.pause_duration = self.pause_start_time.msecsTo(QTime.currentTime())
                self.total_pause_time += self.pause_duration
                self.pause_start_time = None
                print(self.total_pause_time) # just to check 
                self.pause_time_label.setText(f"Total pause time - {self.pause_time_format()}")
            self.flag_button.setEnabled(True)
            self.timer.start(10)
            self.play_pause_button.setText("ıı")
        elif self.play_pause_button.text() == "ıı":
            self.pause_start_time = QTime.currentTime()
            self.play_pause_button.setText("▶")
            self.timer.stop()
            
    def reset_button_slot(self):
        self.reset_button.setDisabled(True)
        self.play_pause_button.setText("▶")
        self.time = QTime(0 , 0, 0, 0)
        self.timer.stop()
        self.time_display.setText(self.time_format(self.time))
        self.total_pause_time = 0 
        self.pause_time_label.setText(" Total pause time - 00:00:00.00")
        self.flag_button.setEnabled(False)
        self.flags.clear()
        self.flag_display.setText("")
    def time_format(self , time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    
    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_display.setText(self.time_format(self.time))
    
    def pause_time_format(self):
        total_msec = self.total_pause_time # for my ease
        hour = total_msec // 3600000
        minute = (total_msec % 3600000) // 60000
        second = (total_msec % 60000) // 1000
        millisecond = (total_msec % 1000) // 10 
        return f"{hour:02}:{minute:02}:{second:02}.{millisecond:02}"
    def flag_button_slot(self):   
        if not self.time == QTime(0 , 0 , 0 , 0):
            current_flags =self.time_format(self.time)
            self.flags.append(current_flags)
           # print("Your flags are - " , end=" ")
            # print(self.flags)
            
            # current_text = self.flag_display.text()
            current_text = ""
            flag_num2 = 0
            for x in self.flags:
                flag_num2 += 1 
                current_text += (f"Flag {flag_num2:02} - {x} \n")
            self.flag_display.setText(current_text)
                
    def history_reader(self):
        with open(self.filepath , "r") as file :
            self.json_reader = json.load(file)


def main():
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()