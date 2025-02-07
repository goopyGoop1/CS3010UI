from datetime import datetime,timedelta
import  time



def part_a():
    start_list = []
    finish_list = []
    start = datetime.now()

    start_str = start.strftime("%H:%M:%S")
    start_list.append(start_str.split(":"))



    s_hour = timedelta(hours = int(start_list[0][0])) 
    s_min = timedelta(minutes = int(start_list[0][1]))
    s_sec = timedelta(seconds = int(start_list[0][2]))

    start_total_sec = (s_hour.total_seconds()) + (s_min.total_seconds()) + (s_sec.total_seconds())

    press = input("Press the return key")

    finish = datetime.now()

    finish_str = finish.strftime("%H:%M:%S")
    finish_list.append(finish_str.split(":"))



    f_hour = timedelta(hours = int(finish_list[0][0])) 
    f_min = timedelta(minutes = int(finish_list[0][1]))
    f_sec = timedelta(seconds = int(finish_list[0][2]))

    finish_total_sec = (f_hour.total_seconds()) + (f_min.total_seconds()) + (f_sec.total_seconds())


    total_time = finish_total_sec - start_total_sec

    print("The total time in  seconds is:", total_time)



def pause(delay):
    start = datetime.now()
    while True:
        diff = (datetime.now() - start)
        diff = diff.total_seconds() * 1000  # Convert to milliseconds
        if diff > delay:
            break


def part_b():
    while True:
        try:
            user_input = int(input("Enter the number of seconds. (0 to exit): "))
            print()
        
            if user_input > 0:
                while user_input >= 0:
                    pause(1000)
                    print(user_input)
                    user_input-= 1 
            
            
            elif user_input == 0:
                print("\nExiting Program")
                break
            
            else:
                print("Invalid input")

        except ValueError:
            print("Invalid input. Please enter an integer.")


def part_c():
    while True:
        try:
            user_input = int(input("Enter the number of seconds. (0 to exit): "))
            print()
        
            if user_input > 0:
                while user_input >= 0:
                    time.sleep(1.0)
                    print(user_input)
                    user_input-= 1 
            
            
            elif user_input == 0:
                print("\nExiting Program")
                break
            
            else:
                print("Invalid input")

        except ValueError:
            print("Invalid input. Please enter an integer.")                    



if __name__ == "__main__":

    part_a()
    print("-" * 50)


    part_b() 
    print("-" * 50)

    part_c()
