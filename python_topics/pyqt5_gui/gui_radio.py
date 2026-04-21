# radio button in pyqt5
import sys
from PyQt5.QtWidgets import (QMainWindow , QApplication , QVBoxLayout, QLayout ,
                             QWidget ,
                              QRadioButton , QButtonGroup) # to group together different radio buttons
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700 , 700)
        self.setWindowTitle("Radio buttons in PyQt5!")
        self.radio1 = QRadioButton("Messi" )
        self.radio2 = QRadioButton("Cristiano" )
        self.radio3 = QRadioButton("Lewandowski" )
        self.radio4 = QRadioButton("Ballon'dor" )
        self.radio5 = QRadioButton("World cup")
        self.button_group1 = QButtonGroup(self) #not visual, just logic; groups buttons logically; not part of UI. Buttons still inside central widget
        self.button_group2 = QButtonGroup(self)
        self.setWindowIcon(QIcon("pyqt5_gui\\gui_icon.jpeg"))
        self.initui()
    def initui(self):
        central_widgit = QWidget()
        layout = QVBoxLayout()
        central_widgit.setLayout(layout)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)
        layout.addWidget(self.radio5)
        self.setCentralWidget(central_widgit)
        self.setStyleSheet("QRadioButton{"
                           "font-size: 30px ;"
                           "font-family: Arial;" 
                           "padding : 10px;"
                           "}") # to set multiple sylesheet together
        
        #----------------To ADD BUTTONS IN GROUP----------------
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        #----------------TO PRINT THE RESPONSE----------------
        self.radio1.toggled.connect(self.radio_button_slot)
        self.radio2.toggled.connect(self.radio_button_slot)
        self.radio3.toggled.connect(self.radio_button_slot)
        self.radio4.toggled.connect(self.radio_button_slot)
        self.radio5.toggled.connect(self.radio_button_slot)
    def radio_button_slot(self): 
        radio_toggled = self.sender() # self sender is a method in Qmainwindow which got inherited by Main window thats why we are using self
        # print(radio_toggled.text()) # self.sender() returns memory addres 
        if radio_toggled.isChecked(): # it will print 2 time if this line is not there. once when checked and once when unchecked
            print(f"{radio_toggled.text()} is selected!") 


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()