import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QLabel
from PyQt5.QtGui import QIcon , QFont , QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow) : 
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("revisions\\april2026\\gui_icon.jpeg"))
        self.setGeometry(0 , 0 , 700 , 700 )
        label1 = QLabel("Hello there my old friend!" , self)
        label1.setGeometry(0 , 0 , 300 , 50)
        label1.setFont(QFont("Times New Roman" , 18))
        label1.setStyleSheet("color: red;"
                             "background-color: blue;"
                             "font-weight: bold;"
                             "font-style: italic;"
                             "text-decoration: underline;")
        label2 = QLabel(self)
        pixmap2 = QPixmap("revisions\\april2026\\gui_icon.jpeg")
        label2.setPixmap(pixmap2)
        label2.setGeometry(0 , 51 , 300 , 300)
        label2.setScaledContents(True)

        # lets make the label1 in complete center
        label1.setAlignment(Qt.AlignCenter)

        # lets make the image in right bottom corner of the screen 
        # label2.setGeometry(self.width() - label2.width() , self.height() - label2.height() , label2.width() , label2.height())  That works!

        # lets make the image in center of the page 
        label2.setGeometry((self.width() - label2.width()) //2 , (self.height() - label2.height()) //2  , label2.width() , label2.height())
def main() : 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__' : 
    main()
