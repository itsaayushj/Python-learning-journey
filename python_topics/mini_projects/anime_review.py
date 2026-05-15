# import requests

# base_url = "https://api.jikan.moe/v4/"
# end_url = "anime?q="
# searched_anime = input("Enter the anime you are searching for: ")
# response = requests.get(f"{base_url}{end_url}{searched_anime}")
# data = response.json()
# print(data['data'][0]['title'])
import requests
import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget , QVBoxLayout , QHBoxLayout , QGridLayout , QLayout , QLineEdit , QLabel , QPushButton
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
        central_widget.setLayout(vbox_main)
        
        self.anime_poster.setMinimumSize(450 , 450)
        self.search_button.clicked.connect(self.search_button_slot)
    
    def search_button_slot(self):
        base_url = "https://api.jikan.moe/v4/"
        endpoint = "anime?q="
        query = self.user_input_lineedit.text()
        response = requests.get(f"{base_url}{endpoint}{query}")
        data = response.json()
        anime_details = data['data'][0] # for ease
        self.anime_name_output.setText(anime_details['title'])
        self.anime_rating_output.setText(str(anime_details['score'])) # settext only accept strings apparently
        self.anime_episodes_output.setText(str(anime_details['episodes']))
        self.anime_year_released_output.setText(anime_details['aired']['string'])
        self.anime_status_output.setText(anime_details['status'])

        # genetating poster 
        pixmap = QPixmap()
        image_url = anime_details['images']['jpg']['large_image_url']
        image_data = requests.get(image_url).content #.content gets raw binary data of the image otherwise we get   status code , headers etc 
        pixmap.loadFromData(image_data)

        pixmap.scaled(
            450 ,
              450 ,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.anime_poster.setPixmap(pixmap)S

def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()

