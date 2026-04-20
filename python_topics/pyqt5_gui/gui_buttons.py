import sys 
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel , QPushButton
from PyQt5.QtGui import QIcon , QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0 , 0 , 500 , 500)
        self.setWindowIcon(QIcon("pyqt5_gui\\gui_icon.jpeg"))
        self.setWindowTitle("Buttons in GUI with the help of PyQt5")
        self.button = QPushButton("Click me!" , self) # creating the button
        self.label = QLabel("Hello There!" , self)
        self.initui()

    def initui(self):
        self.button.setGeometry(150 , 150 , 200 , 200)
        self.button.setFont(QFont("Arial" , 30))
        self.label.setGeometry(170 , 330 , 400 , 100)
        self.label.setFont(QFont("Arial" , 25))
        self.button.clicked.connect(self.if_clicked) # here we didnt say if_clicked() because we are not calling the function itself but to run it when the button is clicked! 
        # NOTE : It follows signal.connect(slot) // when the signal happens (clicked for eg-) connect it to slot (here it is if_clicked) 
    def if_clicked(self):
        # print("Button Was clicked!")
        # self.button.setDisabled(True)
        self.label.setText("Clicked!") # to change the text of the label 
        self.button.setDisabled(True) # to disable the button
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()