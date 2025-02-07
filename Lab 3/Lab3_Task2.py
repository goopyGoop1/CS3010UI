from datetime import datetime,timedelta
import  time
import tkinter as tk



def countdown(user_input, label):
    try:
        
            if user_input > 0:
                while user_input >= 0:
                    label.config(text=str(user_input))
                    time.sleep(1.0)
                    print(user_input)
                    user_input-= 1 
            
            
            elif user_input == 0:
                print("\nExiting Program")
            
            else:
                print("Invalid input")

    except ValueError:
            print("Invalid input. Please enter an integer.")









root = tk.Tk()
root.title("Lab 3 Task 2")
root.geometry("300x300")

# entry = tk.Entry(root)
# entry.pack(pady=10)

label = tk.Label(root, text="Starting Countdown!!!", font= ("Arial bold", 20) )
label.pack(pady=20)


countdown(10, label)





# botton  = tk.Button(root, text = "Start Countdown", command = init_countdown)
# botton.pack()


root.mainloop()
