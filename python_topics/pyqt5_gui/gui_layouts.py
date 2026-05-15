import sys
from PyQt5.QtWidgets import (QMainWindow , QApplication , QLabel ,
                              QWidget , QVBoxLayout , QHBoxLayout , QGridLayout )

class MainWindow(QMainWindow) : 
    def __init__(self):
        super().__init__()
        self.setGeometry(0 , 0 , 500 , 500)
        self.setWindowTitle("Layouts in GUI!" )
        self.initui()

    def initui(self):
        central_widget = QWidget() # making it a widget first
        self.setCentralWidget(central_widget) # turning it into central widget , central widget = main content of window
        label1 = QLabel("#1" ) # we wont add self here because then it will be assigned to Mainwindow but we want it to be assigned to central widget so we will let it assign the correct parent automatically
        label2 = QLabel("#2" ) # when adding layout then no self, unless setting something manually. eg - move, setGeometry
        label3 = QLabel("#3" )
        label4 = QLabel("#4" )
        label5 = QLabel("#5" )
        label1.setStyleSheet("color: red;"
                             "background-color: yellow")
        label2.setStyleSheet("color: blue;"
                             "background-color: red")
        label3.setStyleSheet("color: green;"
                             "background-color: blue")
        label4.setStyleSheet("color: yellow;"
                             "background-color: green")
        label5.setStyleSheet("color: purple;"
                             "background-color: pink")

        grid = QGridLayout() # calling the constructor
        central_widget.setLayout(grid) # SETTING THE LAYOUT
        grid.addWidget(label1 , 0 , 0) # for v and h layout no numbers are needed but order matters 
        grid.addWidget(label2 , 0 , 1) # the numbers are used as tables (rows , cols , rowspan , colspan)
        grid.addWidget(label3 , 1, 0)
        grid.addWidget(label4 , 1 , 1)
        grid.addWidget(label5 , 2 , 0)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


