import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "Alarmbell.mp3"

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            
            # Wait until the user stops the alarm
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False

        time.sleep(1)

if __name__ == "__main__":
    while True:
        alarm_time = input("Enter the alarm time (HH:MM:SS): ")
        try:
            datetime.datetime.strptime(alarm_time, "%H:%M:%S")
            break
        except ValueError:
            print("Invalid time format. Please try again.")

    set_alarm(alarm_time)
