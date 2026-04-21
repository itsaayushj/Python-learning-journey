import sys 
from PyQt5.QtWidgets import QApplication , QMainWindow , QLineEdit , QPushButton # to get the text from line edit box
from PyQt5.QtGui import QIcon , QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600 , 600)
        self.setWindowIcon(QIcon("pyqt5_gui\\gui_icon.jpeg"))
        self.setWindowTitle("Line edit in PyQt5")
        self.line_edit = QLineEdit(self)
        self.push_button = QPushButton("Submit" , self)
        self.initui()
    def initui(self):
        self.line_edit.setGeometry(10 , 10 , 230 , 50)
        self.line_edit.setPlaceholderText("Enter your name!")
        self.push_button.setGeometry(250 , 10 , 300 , 50) # we could also use layout
        self.push_button.setFont(QFont("Arial" , 20))
        self.line_edit.setFont(QFont("Arial" , 20))
        self.push_button.clicked.connect(self.push_button_slot)
    def push_button_slot(self):
        text = self.line_edit.text() # to get the text from line edit widget
        print(f"Hello {text} !")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()