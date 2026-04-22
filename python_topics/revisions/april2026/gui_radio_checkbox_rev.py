import sys 
from PyQt5.QtWidgets import QWidget , QLayout , QMainWindow , QApplication , QPushButton , QRadioButton , QCheckBox , QLineEdit , QButtonGroup , QVBoxLayout
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700 , 700)
        self.setWindowTitle("Revision on radio , pushbutton  , lineedit and checkbox")
        self.initui()
    def initui(self):
    #     self.checkbox = QCheckBox("do you like football?" , self)
    #     self.checkbox.setGeometry( 0 , 0 , 200 , 20)
    #     self.checkbox.stateChanged.connect(self.checkbox_slot)
    # def checkbox_slot(self , state):
        # if state == Qt.Checked : 
        #     print("You do like football!")
        # else : 
        #     print("You dont like football ! really????")

        self.radio1 = QRadioButton("A")
        self.radio2 = QRadioButton("B")
        self.radio3 = QRadioButton("C") 
        self.radio4 = QRadioButton("1")
        self.radio5 = QRadioButton("2")
        self.group1 = QButtonGroup(self)
        self.group2 = QButtonGroup(self)
        self.group1.addButton(self.radio1)
        self.group1.addButton(self.radio2)
        self.group1.addButton(self.radio3)
        self.group2.addButton(self.radio4)
        self.group2.addButton(self.radio5)
        central_widgit = QWidget()
        self.setCentralWidget(central_widgit)
        layout = QVBoxLayout()
        central_widgit.setLayout(layout)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)
        layout.addWidget(self.radio5)
        self.radio1.toggled.connect(self.radio_slot)
        self.radio2.toggled.connect(self.radio_slot)
        self.radio3.toggled.connect(self.radio_slot)
        self.radio4.toggled.connect(self.radio_slot)
        self.radio5.toggled.connect(self.radio_slot)        
    def radio_slot(self):
        sender = self.sender()
        if sender.isChecked():
            print(f"You chose {sender.text()}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()