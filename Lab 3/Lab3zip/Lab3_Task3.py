from datetime import datetime,timedelta
import  time
import tkinter as tk



def countdown(user_input):
    if user_input >= 0:
        label.config(text=str(user_input))
        root.after(1000,countdown, user_input -1)

    else:
        label.config(text="BYE!!!")

def init_countdown():
        try:
            user_input = int(entry.get())
        
            if user_input > 0:
                countdown(user_input) 
            
            
            elif user_input == 0:
                label.config(text = "Exiting Program")
            
            else:
                label.config(text = "Invalid input")

        except ValueError:
            label.config(text = "Invalid input. Please enter an integer.") 







root = tk.Tk()
root.title("Lab 3 Task 2")
root.geometry("300x300")

entry = tk.Entry(root)
entry.pack(pady=10)


label = tk.Label(root, text="Starting Countdown!!!", font= ("Arial bold", 15) )
label.pack(pady=20)



botton  = tk.Button(root, text = "Start Countdown", command = init_countdown)
botton.pack()


root.mainloop()

