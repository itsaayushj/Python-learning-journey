import sys 
from PyQt5.QtWidgets import QApplication , QMainWindow ,  QCheckBox
from PyQt5.QtGui import QFont , QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700 , 700) # just takes size and not coordinates unlike setgeometry . 💡 OS decides position
        self.setWindowTitle("Checkbox in GUI!")
        self.setWindowIcon(QIcon("pyqt5_gui\\gui_icon.jpeg"))
        self.checkbox = QCheckBox("Do you like Pizza?" , self) # creating a checkbox
        self.initui()
    def initui(self):
        self.checkbox.setStyleSheet("font-size: 30px;" 
                                    "font-family: Arial") # could have also done it with Qfont
        self.checkbox.setGeometry(0 , 0 , 300 , 50)
        self.checkbox.setChecked(False)#to preset the textbox to checked/unchecked
        self.checkbox.stateChanged.connect(self.checkbox_slot)
    def checkbox_slot(self , state): # state is provided to us when we interact with checkbox!
        # if state == 2 :
        #     print("You like pizza!")
        # else : 
        #     print("You dont like pizza")
        if state == Qt.Checked: # more readable and a good practice 😭
            print("You like pizza")
        else : 
            print("You dont like pizza")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__' :
    main()
