import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel # to use labels 
from PyQt5.QtGui import QIcon , QFont  # to change fonts of labels 
from PyQt5.QtCore import Qt # to work with alignments for now 
class MainWindow(QMainWindow) : 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("learning qlabels")
        self.setWindowIcon(QIcon("pyqt5_gui\\gui_icon.jpeg"))
        self.setGeometry(0,0 , 500 , 600)
        label1 = QLabel("Hello There! I am label 1 " , self) # window will be a parent widget // we are making window in this constructor.
        label1.setFont(QFont("Verdana" , 30))
        label1.setGeometry(0 , 0 , 1000 , 200)
        #stylesheet will be used just like we use CSS (which i dont know yet 💀)
        label1.setStyleSheet("color : #612013;"
                             "background-color : #284345;"
                             "font-weight : bold;"
                             "font-style : italic;"
                             "text-decoration : underline ;"
                             ) # no , needed after each attribute
        # label1.setAlignment(Qt.AlignRight) # horizontal right
        # label1.setAlignment(Qt.AlignLeft) # horizontal left
        # label1.setAlignment(Qt.AlignTop) # top alignment
        # label1.setAlignment(Qt.AlignVCenter) # vertical center
        # label1.setAlignment(Qt.AlignHCenter) # horizontal center
        # label1.setAlignment(Qt.AlignBottom) # bottom


        # label1.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # | to combine both 
        label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # center & center
        label1.setAlignment(Qt.AlignCenter) # shortcut for center & center




def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()