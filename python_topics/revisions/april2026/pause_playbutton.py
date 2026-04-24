import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QHBoxLayout , QWidget , QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600 , 300)
        self.initui()
    def initui(self):
            self.endbutton = QPushButton("■")
            self.pausebutton = QPushButton("▶")
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
            layout = QHBoxLayout()
            central_widget.setLayout(layout)
            layout.addWidget(self.endbutton)
            layout.addWidget(self.pausebutton)
            self.endbutton.setFixedSize(250 , 250) # to make it circle it needs to be fixed height and width and with resize it can change so we used fixed size
            self.pausebutton.setFixedSize(250 , 250)
            self.endbutton.setEnabled(False)
            self.setStyleSheet("""
                            QPushButton{
                               font-size: 80px;
                               font-family: Arial;
                                padding: 90px;
                               margin: 20px;
                               border: 3px solid;
                               border-radius: 100px;
                               }
                                """)


        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()