# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:56:45 2026

@author: Afra
"""
import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_pass(length):
     character=string.ascii_letters+string.digits+string.punctuation
    
     password=""
     for i in range(length):
         password+=random.choice(character)
        
     return password


def name_pass(name,length):
     character=string.digits+string.punctuation
     password=name+""
   
     for i in range (length-len(name)):
         password+=random.choice(character)
        
     return password
 
def generate():
    try:
        length=int(length_entry.get())
        
        if length<=0:
            messagebox.showerror("Error!,Length must be greater than 0")
            return
        
        if choice.get()==1:
            password=generate_pass(length)
            
        elif choice.get()==2:
            name=name_entry.get() 
            
            if name=="":
                messagebox.showerror("Error!,Name is required")
                return
            password=name_pass(name,length)

        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

name_label = tk.Label(root, text="Enter Name (for Name-Based Password):")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

choice = tk.IntVar()
choice.set(1)

random_radio = tk.Radiobutton(root, text="Random Password", variable=choice, value=1)
random_radio.pack()

name_radio = tk.Radiobutton(root, text="Name-Based Password", variable=choice, value=2)
name_radio.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack(pady=10)


result_var = tk.StringVar()

result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold"), fg="blue")
result_label.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
