# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:01:21 2026

@author: Afra
"""

import random
import tkinter as tk
from tkinter import messagebox

user_score=0
computer_score=0

choices=["Rock","Paper","Scissors"]
def play(user_choice):
    global user_score,computer_score
    
    computer_choice=random.choice(choices)
    
    if user_choice==computer_choice:
        result="It's a tie!"
    elif(
        (user_choice=="Rock" and computer_choice=="Scissors")or
        (user_choice=="Paper"and computer_choice=="Rock")or
        (user_choice=="Scissors"and computer_choice=="Paper")):
            result="You win!🎉"
            user_score+=1
    else:
        result= "Computer wins!😥"
        computer_score+=1
    
    result_label.config(
       text=f"You chose: {user_choice}\n"
            f"Computer chose:{computer_choice}\n"
            f"Result:{result}\n"
            f"Score->Your score={user_score}|Computer score={computer_score}"
           )
   
    
def reset_game():
    global user_score,computer_score
    user_score=0
    computer_score=0
    result_label.config(text="Game Restart!Choose Rock Paper or Scissors.")
    
window=tk.Tk()
window.title("Rock,Paper and Scissors game!")
window.geometry("400x400")
window.config(bg="lightpink")

title_label=tk.Label(
    window,
    text="Rock-Paper-Scissors Game!",
    font=("Arial",16,"bold"),
    bg="lightpink"
    )


title_label.pack(pady=10)

instruction_label=tk.Label(
    window,
    text="Choose Rock,Paper or Scissors:",
    font=("Arial",12),
    bg="lightpink"
    )

instruction_label.pack(pady=5)

# Buttons
rock_button=tk.Button(
    window,
    text="Rock ✊ ",
    width=15,
    font= 14,
    command=lambda:play("Rock")
    )

rock_button.pack(pady=5)

paper_button=tk.Button(
    window,
    text="Paper📃",
    width=15,
    font=14,
    command=lambda:play("Paper")
    )

paper_button.pack(pady=5)

scissors_button=tk.Button(
    window,
    text="Sciccors ✂",
    width=15,
    font=14,
    command=lambda:play("Scissors")
    )

scissors_button.pack(pady=5)

# Result label
result_label=tk.Label(
    window,
    text="Make your move!🎮",
    font=("Arial",12,),
    bg="lightpink",
    justify="center",
    )
result_label.pack(pady=20)

# Reset button
reset_button=tk.Button(
    window,
    text="Reset Game",
    width=15,
    font=14,
    command=reset_game
   )
reset_button.pack(pady=10)

window.mainloop()