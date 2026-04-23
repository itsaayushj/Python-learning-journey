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
        # Qt needs its own naming system. We can use this name in stylesheet
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        self.setStyleSheet("""
            QPushButton{
                           font-size: 40px;
                           font-family: Arial;
                           padding: 10px 50px;  
                           margin: 20px;
                           border: 3px solid;
                           border-radius: 15px;
                           
                        } 
            QPushButton#button1{
                            background-color: hsl(353, 86%, 57%);
                        }
            QPushButton#button2{
                            background-color: hsl(115, 54%, 56%);
                        }
            QPushButton#button3{
                            background-color: hsl(267, 84%, 61%);
                        }
             QPushButton#button1:hover{
                            background-color: hsl(353, 86%, 77%); 
                        }
            QPushButton#button2:hover{
                            background-color: hsl(115, 54%, 76%);
                        }
            QPushButton#button3:hover{
                            background-color: hsl(267, 84%, 81%);
                        }
                            """) # bigger string so we used triple quotes """
 #increasing the brightness when hover..thatswhy i used hsl over hex


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()