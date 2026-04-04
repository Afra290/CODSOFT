# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:51:52 2026

@author: Afra
"""

print("====TO-DO-LIST====")

tasks = [] 
def add_task(): 
    task= input("Enter Your task: ") 
    tasks.append({"task": task, "done": False})
    print("Task added successfully!") 

def view_tasks(): 
    if not tasks: print("No tasks available.")
    else: print("\nYour Tasks:") 
    for i, t in enumerate(tasks, start=1): 
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['task']} - {status}") 
        
def update_task(): 
    view_tasks()
    num = int(input("Enter task number to update: "))
    new_task = input("Enter new task: ") 
    tasks[num-1]["task"] = new_task 
    print("Task updated successfully!") 
    
def delete_task(): 
    view_tasks()
    num = int(input("Enter task number to delete: "))
    tasks.pop(num-1) 
    print("Task deleted successfully!") 
    
def mark_done(): 
    view_tasks() 
    num = int(input("Enter task number to mark as done: "))
    tasks[num-1]["done"] = True 
    print("Task marked as completed!") 
    
def show_progress():
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    if total == 0: 
        print("No tasks available.") 
   
    else: 
        progress = (done / total) * 100 
        print(f"Progress: {progress:.2f}% completed")
        
while True: 
    print("\n===== TO-DO LIST MENU =====") 
    print("1. Add Task")
    print("2. View Tasks") 
    print("3. Update Task") 
    print("4. Delete Task") 
    print("5. Mark Task as Completed")
    print("6. Show Progress") 
    print("7. Exit") 
    choice = input("Enter your choice: ")
    if choice == "1": 
        add_task() 
    
    elif choice == "2":
        view_tasks() 
        
    elif choice == "3":
        update_task()
    
    elif choice == "4": 
        delete_task() 
        
    elif choice == "5":
        mark_done() 
        
    elif choice == "6":
        show_progress() 
        
    elif choice == "7": 
        print("Exiting program...")
        break 
    else: 
        print("Invalid choice!")