# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:52:45 2026

@author: Afra
"""
import random
import tkinter as tk
from tkinter import messagebox
contacts=[]

def add_contact():
    name=name_entry.get()
    phone=phone_entry.get()
    email=email_entry.get()
    address=address_entry.get()
    
    contact={"name":name,
           "phone":phone,
           "email":email,
           "address":address}

    contacts.append(contact)
    messagebox.showinfo("Contacts added successfully")
    
    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)
    

def view_contact():
       if not contacts:
           result_label.config(text="No contacts found")
       else:
           text=""
           for cont in contacts:
              text += cont["name"]+"-" + cont["phone"]+"-"+cont["email"]+"-"+cont["address"]+"\n"
           result_label.config(text=text)
              

def search_contact():
     search_name= name_entry.get()
     
     for cont in contacts:
         if search_name==cont["name"]:
             result_label.config(
                 text=cont["name"]+cont["phone"]+
                 cont["email"]+cont["address"])
             return
     result_label.config(text="Contact not found")
     
def update_contact():
    old_name=name_entry.get()
    new_phone=phone_entry.get()
    new_email=email_entry.get()
    new_address=address_entry.get()
    for cont in contacts:
         if old_name==cont["name"]:
            cont["phone"]=new_phone
            cont["email"]=new_email
            cont["address"]=new_address
        
            result_label.config(text="Contact updated successfully")
            return
    result_label.config(text="No contact found")

    
def delete_contact():
    name=name_entry.get()
    
    for cont in contacts:
        if name==cont["name"]:
            contacts.remove(cont)
            
            result_label.config(text="Contact deleted successfully")
            return
    result_label.config(text="no contact found")


root=tk.Tk()
root.title("Contact Book")
root.geometry("500x450")
root.configure(bg="#F5F5F5")


button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.pack(pady=10)

tk.Button(button_frame,text="Add contact", bg="#2C3E50",fg="white",font=("Arial",11,"bold"),padx=10,pady=5,command=add_contact).pack(side=tk.LEFT)
tk.Button(button_frame,text="View contact",bg="#2C3E50",fg="white",font=("Arial",11,"bold"),padx=10,pady=5,command=view_contact).pack(side=tk.LEFT)
tk.Button(button_frame,text="Search contact",bg="#2C3E50",fg="white",font=("Arial",11,"bold"),padx=10,pady=5,command=search_contact).pack(side=tk.LEFT)
tk.Button(button_frame,text="Update contact",bg="#2C3E50",fg="white",font=("Arial",11,"bold"),padx=10,pady=5,command=update_contact).pack(side=tk.LEFT)
tk.Button(button_frame,text="Delete contact",bg="#2C3E50",fg="white",font=("Arial",11,"bold"),padx=10,pady=5,command=delete_contact).pack(side=tk.LEFT)

form_frame=tk.Frame(root,bg="white")
form_frame.pack(pady=15)

tk.Label(form_frame, text="Name", bg="#F5F5F5",fg="#2C3E50",width=10,font=("Arial",11,"bold")).grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame,text="Phone", bg="#F5F5F5",fg="#2C3E50",width=10,font=("Arial",11,"bold")).grid(row=1,column=0,padx=10,pady=5)
phone_entry=tk.Entry(form_frame)
phone_entry.grid(row=1,column=1,padx=10,pady=5)

tk.Label(form_frame,text="Email", bg="#F5F5F5",fg="#2C3E50",width=10,font=("Arial",11,"bold")).grid(row=2,column=0,padx=10,pady=5)
email_entry=tk.Entry(form_frame)
email_entry.grid(row=2,column=1,padx=10,pady=5)

tk.Label(form_frame,text="Address", bg="#F5F5F5",fg="#2C3E50",width=10,font=("Arial",11,"bold")).grid(row=3,column=0,padx=10,pady=5)
address_entry=tk.Entry(form_frame)
address_entry.grid(row=3,column=1,padx=10,pady=5)


result_label=tk.Label(root,text="", bg="#F5F5F5",fg="#2C3E50",font=("Arial",11))
result_label.pack(pady=15)

root.mainloop()