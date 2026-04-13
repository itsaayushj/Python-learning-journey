# Multithreading  = Used to perform multiple tasks concurrently (multitasking)
#          Good for I/O bound tasks like reading files or fetching data from APIs
#                   threading.Thread(target=My_function)

import threading 
import time

def walk_dog(name):
    time.sleep(4) 
    print(f"You finished walking {name}!")

def trash_out():
    time.sleep(3)
    print("You took out the trash!")

def get_mails():
    time.sleep(2)
    print("You took the mails!")

chore1 = threading.Thread(target=walk_dog , args=("courage" , ))
chore1.start()
chore2 = threading.Thread(target=trash_out)
chore2.start()
chore3 = threading.Thread(target=get_mails)
chore3.start()

chore1.join()# this waits until the chore1 is done. Then it will proceed
chore2.join()
chore3.join()

print("All chores are done!")

def win_game():
    time.sleep(6)
    print("You won the game")    

def win_round():
    time.sleep(4)
    print("You won the round")

def win_duel():
    time.sleep(2) 
    print("You won the duel!")

game_play1 = threading.Thread(target=win_game)
game_play2 = threading.Thread(target=win_round)
game_play3 = threading.Thread(target=win_duel)

game_play1.start()
game_play2.start()
game_play3.start()

game_play1.join()
game_play2.join()
game_play3.join()

print("game over")


