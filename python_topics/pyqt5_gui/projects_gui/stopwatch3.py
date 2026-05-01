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
    def initui(self):
        self.time_display = QLabel("00:00:00")
        self.play_pause_button = QPushButton("▶")
        self.reset_button = QPushButton("⯀")
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
                            font-size: 70px
                            font-color: #cbcbcb
                           }
                           
                           """)
        
def main():
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()