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

          try:
               response = requests.get(url)
               data = response.json() 
               response.raise_for_status() # It checks the code and raise error if its 400-500
               if data["cod"] == 200 :
                    self.display_weather(data)
          except requests.exceptions.HTTPError as HTTPError:   #HTTPERROR when code is 400-500
               match response.status_code : 
                    case 400 : 
                         self.display_errors("Bad request: \nPlease check your input!")
                    case 401 : 
                         self.display_errors("Unauthorised: \nInvalid API Key!")
                    case 403 : 
                         self.display_errors("Forbidden: \nAccess denied")
                    case 404 : 
                         self.display_errors("Not Found: \nCity not found!")
                    case 500 : 
                         self.display_errors("Internal server error: \nPlease try again later!")
                    case 502 : 
                         self.display_errors("Bad gateway: \nInvalid response from the server")
                    case 503 : 
                         self.display_errors("Service unavailable: \nServer is down")
                    case 504 : 
                         self.display_errors("Gateway timeout: \nNO response from the server")
                    case _: # everything else
                         self.display_errors(HTTPError)
          except requests.exceptions.ConnectionError:
               self.display_errors("Connection Error \nPlease check your internet!")
          except requests.exceptions.Timeout:
               self.display_errors("Timeout Error \nThe request timed out")
          except requests.exceptions.TooManyRedirects:
               self.display_errors("Too many Redirects\nCheck the URL")
          except requests.exceptions.RequestException as RequestException:
               self.display_errors(f"Request Exception:\n{RequestException}")
    def display_errors(self , message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
    def display_weather(self , data):
        self.temperature_label.setStyleSheet("font-size: 70px")
        temp_kelvin = data["main"]["temp"]
        temp_celcius = temp_kelvin - 273.15
        temp_fahrenheit = temp_celcius  * (9/5) + 32 
        self.temperature_label.setText(f"{temp_celcius:.0f}°c")
        description = data["weather"][0]["description"]
        self.description_label.setText(description)
        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.weather_emoji(weather_id))

    @staticmethod
    def weather_emoji(weather_id):
          if 200 <= weather_id <= 232 : 
              return "⛈️"
          elif 300 <= weather_id <= 321 :
              return "☔"
          elif 500 <= weather_id <= 531 :
               return "🌧️"
          elif 600 <= weather_id <= 622 :
               return "❄️"
          elif 701 <= weather_id <= 741 :
               return "🌪️"
          elif weather_id == 762 :
               return "🌋"
          elif weather_id == 771 : 
               return "💨"
          elif weather_id == 781 : 
               return "🌪️"
          elif weather_id == 800 :
               return "☀️"
          elif 801 <= weather_id <= 804 : 
               return "☁️"
          else :
               return "⁉️"
          


def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
