'''Create an alarm clock that lets user set up the time for an alarm clock and it reproduces a youtube video at random from a URL text file'''

import time
import tkinter as tk
import webbrowser
import random as rd
from tkinter import messagebox
import threading
import os

#get random youtube url
def get_random_alarm_url():
    '''get a random youtube url'''
    current_directory = os.path.dirname(os.path.abspath(__file__)) #get current directory
    file = os.path.join(current_directory, "urls.txt") #adding our file to the directory
    with open(file, "r") as database:
        youtube_urls = database.readlines()
    random_url = rd.choice(youtube_urls)
    return random_url

#defining the class
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        

        window_width = 400
        window_height = 200

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.title("Alarm Clock")
        self.resizable(0,0)

        self.create_widgets()

    
    def create_widgets(self):
        '''Method to create widgets for our alarm clock'''
        #Show label instructions
        self.instructions_label = tk.Label(self, text="Input alarm time like this (HH:SS:SS)")
        self.instructions_label.pack()
        
        #Show entry for the time
        self.time_input = tk.Entry(self)
        self.time_input.pack()

        #Validate time button
        self.start_time_button = tk.Button(self, text="Start Alarm", command=self.validate_alarm_input)
        self.start_time_button.pack()

  

        

        

    
    def validate_alarm_input(self):
        '''This methos evaluates what the user has entered in the entry time_input'''

        #obtain user input
        self.time_entered = self.time_input.get()

        
        try:
            #convert time into a time structure
            time.strptime(self.time_entered, "%H:%M:%S")
            self.start_alarm()
        except ValueError:
            messagebox.showerror("Invalid Format", "The entered time is not valid. Use format HH:MM:SS")



    def set_alarm(self):
        '''This sets up the alarm. Constantly checks if the time has reached and then reproduces YouTube Video''' 
        while True:
            current_time = time.strftime("%H:%M:%S") #Check what is the current system time
            if current_time == self.time_entered: #compares current time with the alarm set
                url = get_random_alarm_url().strip()
                webbrowser.open(url) #opens the youtube
                messagebox.showinfo("Alarm!", "It is time to wake up!")
                break #break it so it is not an infinite loop
            time.sleep(1)

    def start_alarm(self):
        '''Method that starts another thread so we have another program flow at the same time'''
        alarm_thread = threading.Thread(target= self.set_alarm)
        alarm_thread.start()















if __name__ == "__main__":
    app = App()
    app.mainloop()