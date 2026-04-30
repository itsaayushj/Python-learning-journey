# Stopwatch in PyQt5 
#first try myself->


# incomplete code   

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QPushButton , QLabel , QWidget , QHBoxLayout , QVBoxLayout
from PyQt5.QtCore import Qt , QTime , QTimer
from PyQt5.QtGui import QFont , QFontDatabase
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(900 , 400)
        self.initui()

    def initui(self):
        self.stop_button = QPushButton("⯀")
        self.play_pause = QPushButton("▶")
        self.play_pause.setFixedSize(150 , 150)
        self.stop_button.setFixedSize(150 , 150)
        self.stop_button.setDisabled(True)
        self.timer_label = QLabel("00:00:00.00")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.vlayout = QVBoxLayout()
        self.hlayout = QHBoxLayout()
        self.central_widget.setLayout(self.vlayout)
        self.hlayout.addWidget(self.stop_button)
        self.hlayout.addWidget(self.play_pause)
        self.vlayout.addWidget(self.timer_label , alignment=(Qt.AlignCenter))
        self.vlayout.addLayout(self.hlayout) # to add the second layout!
        
        self.setStyleSheet(""" 
                           QPushButton{
                           font-family: Arial;
                           font-size: 50px;
                           border: 3px solid;
                           border-radius: 75px;
                           }
                           QPushButton:enabled {
                           color: black;
                           background-color: hsl(141, 73%, 55%);
                           }
                           QPushButton:disabled {
                           color: white;
                           background-color: #121212;
                           }
                           QPushButton:hover {
                           font-size: 70px;
                           background-color: hsl(141, 73%, 65%)
                           }
                           QPushButton:pressed {
                           background-color: hsl(141 , 73% , 40%);
                           font-size: 60px;
                           }
                           """)
        self.central_widget.setStyleSheet("background-color: #fae2b1")
        self.timer_label.setStyleSheet("font-size: 150px;")
        font_id = QFontDatabase.addApplicationFont("D:/source/study stuff/python learning journey/python_topics/pyqt5_gui/projects_gui/DS-DIGI.TTF")
        my_font = QFont(QFontDatabase.applicationFontFamilies(font_id)[0])
        self.timer_label.setFont(my_font)


        self.play_pause.clicked.connect(self.play_pause_slot)
        self.stop_button.clicked.connect(self.stop_slot)
    def play_pause_slot(self):
        self.stop_button.setEnabled(True) # so it can be stopped once timer started
        if self.play_pause.text() == "▶" :
            self.play_pause.setText("ıı")
        elif self.play_pause.text() == "ıı" : 
            self.play_pause.setText("▶")
    def stop_slot(self):
        self.stop_button.setDisabled(True) # so it can be stopped once only
        self.play_pause.setText("▶") # to return it to play if its stopped in resume
        print("stopped")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()