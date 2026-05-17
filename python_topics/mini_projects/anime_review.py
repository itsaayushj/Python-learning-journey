# import requests

# base_url = "https://api.jikan.moe/v4/"
# end_url = "anime?q="
# searched_anime = input("Enter the anime you are searching for: ")
# response = requests.get(f"{base_url}{end_url}{searched_anime}")
# data = response.json()
# print(data['data'][0]['title'])
import requests
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget , QVBoxLayout , QHBoxLayout , QGridLayout , QLayout , QLineEdit , QLabel , QPushButton , QTextEdit
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AnimeDB")
        self.resize(1100 , 600)
        self.initui()
    def initui(self):
        self.user_input_lineedit = QLineEdit()
        self.user_input_lineedit.setPlaceholderText("Enter your anime name")
        self.search_button = QPushButton("Search")
        self.search_button.setDefault(True)
        self.anime_poster = QLabel()
        self.anime_name = QLabel("Name:")
        self.anime_rating = QLabel("Ratings:")
        self.anime_episodes = QLabel("Total Eps:")
        self.anime_year_released = QLabel("Time Period:")
        self.anime_status = QLabel("Status:")
        self.anime_name_output = QLabel()
        self.anime_rating_output = QLabel()
        self.anime_episodes_output = QLabel()
        self.anime_year_released_output = QLabel()
        self.anime_status_output = QLabel()
        self.anime_synopsis = QTextEdit()
        self.anime_synopsis.setReadOnly(True)
        self.widget_group = [self.anime_poster , self.anime_name , self.anime_name_output , self.anime_rating , self.anime_rating_output , self.anime_episodes , self.anime_episodes_output , self.anime_year_released , self.anime_year_released_output , self.anime_status , self.anime_status_output , self.anime_synopsis]
        for widget in self.widget_group : 
            widget.hide()
        self.initial_run_label = QLabel("There is nothing to show here!")
        vbox_main = QVBoxLayout()
        gridlayout1 = QGridLayout()
        hbox1 = QHBoxLayout()
        central_widget = QWidget()
        hbox1.addWidget(self.user_input_lineedit)
        hbox1.addWidget(self.search_button)
        vbox_main.addLayout(hbox1)
        gridlayout1.addWidget(self.anime_poster , 0 , 0 , 5 , 1)
        gridlayout1.addWidget(self.anime_name , 0 , 1 )
        gridlayout1.addWidget(self.anime_name_output , 0 , 2 )
        gridlayout1.addWidget(self.anime_rating , 1 , 1 )
        gridlayout1.addWidget(self.anime_rating_output , 1 , 2 )
        gridlayout1.addWidget(self.anime_episodes , 2 , 1 )
        gridlayout1.addWidget(self.anime_episodes_output , 2 , 2 )
        gridlayout1.addWidget(self.anime_year_released , 3 , 1 )
        gridlayout1.addWidget(self.anime_year_released_output , 3 , 2 )
        gridlayout1.addWidget(self.anime_status , 4 , 1 )
        gridlayout1.addWidget(self.anime_status_output , 4 , 2 )
        self.setCentralWidget(central_widget)
        vbox_main.addLayout(gridlayout1)
        vbox_main.addWidget(self.anime_synopsis)
        vbox_main.addWidget(self.initial_run_label , alignment=(Qt.AlignCenter))
        central_widget.setLayout(vbox_main)
        
        self.anime_poster.setMinimumSize(450 , 450)
        self.search_button.clicked.connect(self.search_button_slot)
    
    def search_button_slot(self):
        try:
            base_url = "https://api.jikan.moe/v4/"
            endpoint = "anime?q="
            query = self.user_input_lineedit.text()
            response = requests.get(f"{base_url}{endpoint}{query}" , timeout=10) # error after 10 seconds
            response.raise_for_status() # raises the error (400-500)
            self.data = response.json()
            # print(self.data) 
            if not self.data.get('data') :
                self.display_errors("Anime Not found !")
            else : 
                self.display_details()
                self.initial_run_label.hide()
        except requests.exceptions.HTTPError : # error 400s-500s
         
            match response.status_code:
                case 400 : 
                    self.display_errors(f"BadRequestException\n")
                case 404 : 
                    self.display_errors(f"BadRequestException\n")
                case 405 : 
                    self.display_errors(f"BadRequestException\n")
                case 429 : 
                    self.display_errors(f"RateLimitException\n")
                case 500 : 
                    self.display_errors(f"UpstreamException\n")
                case 503 : 
                    self.display_errors(f"ServiceUnavailableException\n")
        except requests.exceptions.ConnectionError : 
            
            self.display_errors("Connection Error\nPlease check your internet connection")
        except requests.exceptions.Timeout : 
            
            self.display_errors("Connection Timeout\nPlease try again later")
        except requests.exceptions.TooManyRedirects : 
            
            self.display_errors("Too many redirects\nCheck the URL")
        except requests.exceptions.RequestException as RequestException : 
            
            self.display_errors(f"RequestException\n{RequestException}")
    def display_details(self):
        anime_details = self.data['data'][0] # for ease
        self.anime_name_output.setText(anime_details['title'])
        self.anime_rating_output.setText(str(anime_details['score'])) # settext only accept strings apparently
        self.anime_episodes_output.setText(str(anime_details['episodes']))
        self.anime_year_released_output.setText(anime_details['aired']['string'])
        self.anime_status_output.setText(anime_details['status'])
        
        self.anime_synopsis.setText(anime_details['synopsis'])
        # genetating poster 
        pixmap = QPixmap()
        image_url = anime_details['images']['jpg']['large_image_url']
        image_data = requests.get(image_url).content #.content gets raw binary data of the image otherwise we get   status code , headers etc 
        pixmap.loadFromData(image_data)

        pixmap = pixmap.scaled(
            450 ,
              450 ,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.anime_poster.setPixmap(pixmap)
        for widget in self.widget_group : 
            widget.show()
    def display_errors(self , message) : 
        for widget in self.widget_group : 
            widget.hide()
        self.initial_run_label.setStyleSheet("font-size: 50px")
        self.initial_run_label.setText(message)
        self.initial_run_label.show()

def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()

