import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QLabel , QWidget , QVBoxLayout
from PyQt5.QtCore import QTime , QTimer , Qt
from PyQt5.QtGui import QFont , QFontDatabase 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(700 , 250)
        self.setWindowTitle("Digital clock!")
        self.initui()
        self.update_timer()
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_timer)
    def initui(self):
        self.setStyleSheet("background-color: black;")
        self.mainlabel = QLabel()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(self.mainlabel , alignment=(Qt.AlignCenter))
        self.mainlabel.setStyleSheet("color: green;"
                                     "font-size: 90px;")
        font_id = QFontDatabase.addApplicationFont("D:/source/study stuff/python learning journey/python_topics/pyqt5_gui/projects_gui/DS-DIGI.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family)
        self.mainlabel.setFont(my_font)
    def update_timer(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") 
        self.mainlabel.setText(current_time)




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()