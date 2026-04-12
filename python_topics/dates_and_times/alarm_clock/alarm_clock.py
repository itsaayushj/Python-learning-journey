# a basic alarm clock 
import time 
import datetime
import pygame
source_sound = "dates_and_times\\alarm_clock\\alarm_tune.mp3"
def set_alarm(user_input) : 
    counting_down = True
    while counting_down :
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time > user_input : 
            print("Invalid time!")
            counting_down = False
        if current_time == user_input : 
            print("Time's up!")
            pygame.mixer.init()
            pygame.mixer.music.load(source_sound)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() : 
                time.sleep(1)
            counting_down = False
        else : 
            time.sleep(1)

def main() : 
    user_input = input("Enter alarm time in(HH:MM:SS)")
    set_alarm(user_input)    

if __name__ == "__main__" : 
    main()
