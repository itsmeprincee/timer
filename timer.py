from tkinter import *
from tkinter import font
from tkinter import messagebox
import time

global hours
global minutes
global seconds
#creating start mehtod that is used to count the time...that displayed in the window..
def start():
    global hours
    global minutes
    global seconds
    global master
    try:
        temp = int(hours.get())*3600+int(minutes.get())*60+int(seconds.get())
    except:
        messagebox.showerror("Input Error","please enter valid inputs")
    while temp>-1:
        mins,secs=divmod(temp,60)
        hour =0
        if mins>60:
            hour,mins = divmod(mins,60)
        hours.set(hour)
        minutes.set(mins)
        seconds.set(secs)
        master.update()
        time.sleep(1)
        if temp==0:
            messagebox.showinfo("Time","Time's up!!!")
        temp -=1


#creating main method that will displays the all the widgets..
def main():
    #window creation
    global hours
    global minutes
    global seconds
    global master
    master = Tk()
    master.title("Timer")
    master.geometry("700x350+100+100")
    master.config(bg="#2c313c")
    master.resizable(False,False)
    #heading for master window
    main_heading=Label(master,text="Stop Watch",font =font.Font(family="Helvetica",size=20),fg="#fff",bg="#2c313c")
    main_heading.pack()
    start_button=Button(master,text="Start",font =font.Font(family="Helvetica",size=20),fg="#fff",bg="crimson",bd=0,width=15,command=start)
    start_button.pack(side=BOTTOM)
    #creating frame for main window
    parent = Frame(master,bg='#2c313c')
    parent.pack()
    #creating widgets
    #declaring of variables
    hours = StringVar()
    minutes = StringVar()
    seconds= StringVar()
    #initializing the variables
    hours.set("00")
    minutes.set("00")
    seconds.set("00")
    #creating number icons for displaying time..
    hours_number = Entry(parent,fg="#fff",bg="#b871ce",font=font.Font(family="times new roman",size=50),width=4,textvariable=hours,bd=0,justify="center")
    hours_number.grid(row =0,column=0,padx=10,pady=10,ipady=50)
    minutes_number = Entry(parent,bg="#599bd3",fg="#fff",font=font.Font(family="times new roman",size=50),width=4,textvariable=minutes,bd=0,justify="center")
    minutes_number.grid(row=0,column=1,padx=10,pady=10,ipady=50)
    seconds_number = Entry(parent,bg="#98c379",fg="#fff",font=font.Font(family="times new roman",size=50),width=4,textvariable=seconds,bd=0,justify="center")
    seconds_number.grid(row=0,column=2,padx=10,pady=10,ipady=50)
    #creating number text for what it displays
    hours_text = Label(parent,text="Hours",pady=10,padx=10,bg="#b871ce",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
    hours_text.grid(row=1,column=0,padx=10,pady=10)
    minutes_text = Label(parent,text ="Minutes",pady=10,padx=10,bg="#599bd3",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
    minutes_text.grid(row=1,column=1,padx=10,pady=10)
    seconds_text = Label(parent,text="Seconds",pady=10,padx=10,bg="#98c379",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
    seconds_text.grid(row=1,column=2,padx=10,pady=10)
    parent.mainloop()

if __name__ == "__main__":
    main()
