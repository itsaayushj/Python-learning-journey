import sys 
from PyQt5.QtWidgets import QMainWindow , QApplication , QLabel
from PyQt5.QtGui import QIcon , QFont , QPixmap #for loding , manupulating and displaying images
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("pyqt5_gui\\gui_icon.jpeg"))
        self.setWindowTitle("Images in GUI!")
        self.setGeometry(0 , 0 , 600 , 600)
        label1 = QLabel("Hello World!" , self)
        label1.setFont(QFont("Verdana" , 30))
        label1.setGeometry(0 , 0 , 500 ,100)
        label1.setStyleSheet("color : red;"
                             "background-color : pink;"
                             "font-weight : bold;"
                             "font-style : italic;"
                             "text-decoration : underline")
        label1.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        label2 = QLabel (self)
        label2.setGeometry(0 , 100 , 400 , 400)
        
        pixmap = QPixmap("pyqt5_gui\\gui_icon.jpeg")
        label2.setPixmap(pixmap)
        label2.setScaledContents(True) #to scale the image with the size of label
        
        # to set Alignments

        #label2.setGeometry(self.width() - label2.width() , 0 , label2.width() , label2.height()) # top right

        #label2.setGeometry(self.width() - label2.width() , self.height() - label2.height() , label2.width() , label2.height()) # bottom right

        #label2.setGeometry(0, self.height() - label2.height() , label2.width() , label2.height()) # bottom left

        label2.setGeometry((self.width() - label2.width() ) //2 , (self.height() - label2.height()) //2 , label2.width() , label2.height())  # to make image center
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__' : 
    main()

