import tkinter as tk
from tkinter import ttk
from bluestacks_bot_epoch import RunBot as rb


root = tk.Tk()
root.title("Maple M Botter")
root.geometry("450x300")

runtime_var = tk.StringVar()

def submit():
    runtime = runtime_var.get()
    print("Will now begin botting!")
    rb(int(runtime))
    
# the label for user_name 
runtime_label = ttk.Label(root, 
                  text = "# of minutes to run?").place(x = 155,
                                           y = 60)  
    

    
runtime_input = ttk.Entry(root,
                      width = 30,
                      textvariable = runtime_var).place(x = 100,
                                               y = 90)  



submit_button = ttk.Button(root, 
                       text = "Run",
                       width = 10,
                       command = submit).place(x = 180,
                                         y = 130)

timer_label = ttk.Label(root,
                    text="Time left: ").place(x=190,
                                              y=190)
    
root.mainloop() 
