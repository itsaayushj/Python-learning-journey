import sys 
import requests 
from PyQt5.QtWidgets import QApplication , QLabel , QPushButton, QWidget , QLineEdit , QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: " , self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather" , self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initui()
    def initui(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label , alignment= (Qt.AlignCenter))
        vbox.addWidget(self.city_input )
        vbox.addWidget(self.get_weather_button )
        vbox.addWidget(self.temperature_label , alignment= (Qt.AlignCenter))
        vbox.addWidget(self.emoji_label , alignment= (Qt.AlignCenter))
        vbox.addWidget(self.description_label , alignment= (Qt.AlignCenter))
        self.setLayout(vbox)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_Weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
                           QLabel{
                                Font-family: calibri;
                           }
                           QLabel#city_label{
                                font-style: italic;
                                font-size: 40px;
                           }
                           QLineEdit#city_input{
                                font-size: 40px;
                           }
                           QPushButton#get_Weather_button{
                                font-size: 30px;
                                font-weight: bold;
                           }
                           QLabel#temperature_label{
                                font-size: 70px;
                           }
                           QLabel#emoji_label{
                                font-family: segoe UI emoji;
                                font-size: 75px; 
                           }
                           QLabel#description_label{
                                font-size: 45px;
                           }

                          
                           """)
        self.get_weather_button.clicked.connect(self.get_weather_slot)

    def get_weather_slot(self):
        api_key = "4c999ddef7a94055f039de3290859d9c"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        response = requests.get(url)
        data = response.json() 
        print(data)
    def display_errors(self , message):
        pass
    def display_weather(self):
        pass

def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
