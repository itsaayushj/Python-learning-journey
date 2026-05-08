import sys 
import requests 
from PyQt5.QtWidgets import QApplication , QLabel , QPushButton, QWidget , QLineEdit , QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __initt__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
