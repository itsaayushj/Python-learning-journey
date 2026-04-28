import sys 
from PyQt5.QtWidgets import QApplication  , QMainWindow , QLabel , QWidget , QHBoxLayout , QPushButton
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800 , 300)
        self.initui()
        self.setWindowTitle("Play , Pause , Stop buttons in Pyqt5")
    def initui(self):
        self.stop_button = QPushButton("⯀")
        self.play_pause = QPushButton("▶")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(self.stop_button  , alignment=(Qt.AlignCenter))
        layout.addWidget(self.play_pause  , alignment=(Qt.AlignCenter))
        self.play_pause.setFixedSize(250 , 250)
        self.stop_button.setFixedSize(250 , 250)
        self.stop_button.setDisabled(True)
        
        
        self.setStyleSheet(""" QPushButton{
                           font-family: Arial;
                           font-size: 80px;
                           border: 3px solid;
                           border-radius: 121px;
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
                           font-size: 145px;
                           background-color: hsl(141, 73%, 65%)
                           }
                           QPushButton:pressed {
                           background-color: hsl(141 , 73% , 40%);
                           font-size: 110px;
                           }
                           """)
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
        print("stopped") # for assurance lmao
def main():             
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
