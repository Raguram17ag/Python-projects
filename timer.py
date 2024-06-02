import time
from tkinter import *
from tkinter import messagebox
import tkinter as tk

option=int(input("choose  option: 1-countdown  2-stopwatch"))
if(option==1):

    ### Create the interface object
    clockWindow = Tk()
    clockWindow.geometry("500x500")
    clockWindow.title("Countdown Timer")
    clockWindow.configure(background='orange')

    ### Declare variables
    hourString = StringVar()
    minuteString = StringVar()
    secondString = StringVar()

### Set strings to default value
    hourString.set("00")
    minuteString.set("00")
    secondString.set("00")

### Get user input
    hourTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=hourString)
    minuteTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=minuteString)
    secondTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=secondString)

### Center textboxes
    hourTextbox.place(x=170, y=180)
    minuteTextbox.place(x=220, y=180)
    secondTextbox.place(x=270, y=180)

    def runTimer():
        try:
            clockTime = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())
        except:
            print("Incorrect values")

        while(clockTime > -1):
        
            totalMinutes, totalSeconds = divmod(clockTime, 60)

            totalHours = 0
            if(totalMinutes > 60):
                totalHours, totalMinutes = divmod(totalMinutes, 60)

            hourString.set("{0:2d}".format(totalHours))
            minuteString.set("{0:2d}".format(totalMinutes))
            secondString.set("{0:2d}".format(totalSeconds))

        ### Update the interface
            clockWindow.update()
            time.sleep(1)

        ### Let the user know if the timer has expired
            if(clockTime == 0):
                messagebox.showinfo("", "Your time has expired!")

            clockTime -= 1


    setTimeButton = Button(clockWindow, text='Set Time', bd='5', command=runTimer)
    setTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER)

### Keep looping
    clockWindow.mainloop()
else:
      # ***** IMPORTS *****

    # ***** VARIABLES *****
    # use a boolean variable to help control state of time (running or not running)
    running = False
    # time variables initially set to 0
    hours, minutes, seconds = 0, 0, 0

# ***** NOTES ON GLOBAL *****
    # global will be used to modify variables outside functions
    # another option would be to use a class and subclass Frame

    # ***** FUNCTIONS *****
    # start, pause, and reset functions will be called when the buttons are clicked
    # start function
    def start():
        global running
        if not running:
            update()
            running = True

# pause function
    def pause():
        global running
        if running:
        # cancel updating of time using after_cancel()
            stopwatch_label.after_cancel(update_time)
            running = False

# reset function
    def reset():
        global running
        if running:
        # cancel updating of time using after_cancel()
            stopwatch_label.after_cancel(update_time)
            running = False
        # set variables back to zero
        global hours, minutes, seconds
        hours, minutes, seconds = 0, 0, 0
        # set label back to zero
        stopwatch_label.config(text='00:00:00')

# update stopwatch function
    def update():
        # update seconds with (addition) compound assignment operator
        global hours, minutes, seconds
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0
        # format time to include leading zeros
        hours_string = f'{hours}' if hours > 9 else f'0{hours}'
        minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
        seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # update timer label after 1000 ms (1 second)
        stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second (1000 milliseconds), call update function
    # use update_time variable to cancel or pause the time using after_cancel
        global update_time
        update_time = stopwatch_label.after(1000, update)

# ***** WIDGETS *****
# create main window
    root = tk.Tk()
    root.geometry('485x220')
    root.title('Stopwatch')

# label to display time
    stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 80))
    stopwatch_label.pack()

# start, pause, reset, quit buttons
    start_button = tk.Button(text='start', height=5, width=7, font=('Arial', 20), command=start)
    start_button.pack(side=tk.LEFT)
    pause_button = tk.Button(text='pause', height=5, width=7, font=('Arial', 20), command=pause)
    pause_button.pack(side=tk.LEFT)
    reset_button = tk.Button(text='reset', height=5, width=7, font=('Arial', 20), command=reset)
    reset_button.pack(side=tk.LEFT)
    quit_button = tk.Button(text='quit', height=5, width=7, font=('Arial', 20), command=root.quit)
    quit_button.pack(side=tk.LEFT)

# ***** MAINLOOP *****
# run app
    root.mainloop()
