import sys 
from PyQt5.QtWidgets import QMainWindow , QApplication , QLabel , QPushButton
from PyQt5.QtGui import QIcon , QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0 , 0 , 700 , 700)
        self.setWindowIcon(QIcon("revisions\\april2026\\gui_icon.jpeg"))
        self.label1 = QLabel("Unclicked" , self)
        self.label1.setGeometry(250 , 400 , 200 , 50)
        self.label1.setFont(QFont("Arial" , 25))
        self.initui()
    def initui(self):
        self.button = QPushButton("Click me!" , self)
        self.button.setGeometry(250 , 250 , 150 , 150)
        self.button.setFont(QFont("Arial" , 25))
        self.button.clicked.connect(self.buttonslot)
    def buttonslot(self):
        print("Clicked!")
        self.button.setDisabled(True)
        self.label1.setText("Clicked!")
        self.button.setText("clicked!")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()