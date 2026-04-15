#pyqt5 introduction
import sys #system 
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtGui import QIcon # to make icons
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # to make the base window
        self.setWindowTitle("My first GUI!")
        self.setWindowIcon(QIcon("pyqt5_gui\\gui_icon.jpeg"))
        self.setGeometry(500,200,500,500) #x,y,width,height

def main() :
    app = QApplication(sys.argv)# arg stands for arguments//helps to access command line arguments intended for it 
    window  = MainWindow() #creates the window abject
    window.show() # to show the window // it will be shown for a small time 
    sys.exit(app.exec_()) # to keep the window running // exec = execute



if __name__ == '__main__' : 
    main()


