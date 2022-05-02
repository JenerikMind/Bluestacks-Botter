from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from bluestacks_bot_epoch import RunBot as rb


top = Tk()
top.title("Maple M Botter")
top.geometry("450x300")

runtime_var = tk.StringVar()

def submit():
    runtime = runtime_var.get()
    print("Will now begin botting!")
    rb(int(runtime))
    
# the label for user_name 
runtime_label = Label(top, 
                  text = "Username").place(x = 190,
                                           y = 60)  
    

    
runtime_input = Entry(top,
                      width = 30,
                      textvariable = runtime_var).place(x = 100,
                                               y = 90)  



submit_button = Button(top, 
                       text = "Run",
                       width = 10,
                       command = submit).place(x = 180,
                                         y = 130)

timer_label = Label(top,
                    text="Time left: ").place(x=190,
                                              y=190)
    
top.mainloop() 
