import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QLineEdit , QPushButton , QLabel
from PyQt5.QtGui import QFont 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500 , 500)
        self.initui()
    def initui(self):
        self.lineedit = QLineEdit(self)
        self.lineedit.setGeometry(0 , 0 , 250 , 50)  
        self.lineedit.setFont(QFont("Arial" , 20))
        self.button = QPushButton("Submit" , self)
        self.button.setGeometry(260 , 0 , 200 , 50)
        self.button.clicked.connect(self.button_slot)
        self.lineedit.setPlaceholderText("Enter Your Name")
        self.label1 = QLabel("Who are you ? 🤨🤨🔫 " , self)
        self.label1.setGeometry(50 , 150 , 900 , 50)
        self.label1.setFont(QFont("Arial" , 30))

    def button_slot(self):
        text = self.lineedit.text()
        print(f"hello {text}")
        if text == "Thanos": 
            self.label1.setText("ayy backup you purple baloon😡")
        else :
            self.label1.setText(f"oww, hello {text}. 😅")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

