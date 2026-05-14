# import requests

# base_url = "https://api.jikan.moe/v4/"
# end_url = "anime?q="
# searched_anime = input("Enter the anime you are searching for: ")
# response = requests.get(f"{base_url}{end_url}{searched_anime}")
# data = response.json()
# print(data['data'][0]['title'])

import sys
from PyQt5.QtWidgets import QMainWindow , QApplication , QWidget , QVBoxLayout , QHBoxLayout , QGridLayout , QLayout , QLineEdit , QLabel , QPushButton

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

        vbox_main = QVBoxLayout()
        vbox1 = QVBoxLayout()
        hbox1 = QHBoxLayout()
        central_widget = QWidget()
        hbox1.addWidget(self.user_input_lineedit)
        hbox1.addWidget(self.search_button)
        vbox_main.addLayout(hbox1)

        self.setCentralWidget(central_widget)
        central_widget.setLayout(vbox_main)
    
def main(): 
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()

