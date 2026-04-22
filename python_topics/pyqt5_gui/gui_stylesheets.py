# setting up stylesheets in python 
import sys 
from PyQt5.QtWidgets import QApplication , QMainWindow , QLayout , QWidget , QHBoxLayout , QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.initui()
    def initui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        self.setStyleSheet("""
            QPushButton{
                           font-size: 40px;
                           font-family: Arial;
                           padding: 50px 100px;
                           } 
                            """) # bigger string so we used triple quotes """



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()