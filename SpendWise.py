import tkinter as tk
from tkinter import messagebox
from datetime import datetime

#Intializing the main window
root= tk.Tk()
root.title("Spend Wise")
root.geometry("700x600") #set window size
root.configure(bg="light gray")

#Create and style frames
header_frame=tk.Frame(root,bg="#879a98")
header_frame.pack(fill="x")
input_frame=tk.Frame(root,bg="#428484")
input_frame.pack(fill="x")
list_frame = tk.Frame(root, bg="black")
list_frame.pack(fill="both", expand=True)
button_frame = tk.Frame(root, bg="#85CFDB")
button_frame.pack(fill="x")

#header label style
header_label=tk.Label(header_frame,text="SPEND WISE",bg="#879a98",fg="black",font=("Helvetica",20,"bold"))
header_label.pack()

#monthyear label style
monthyear_label =tk.Label(input_frame,text="Month and Year (MM/YYYY) : ",bg="#428484",font=("Times New Roman",15))
monthyear_label.grid(row=0,column=0,sticky="w",padx=10,pady=5)
monthyear_entry = tk.Entry(input_frame)
monthyear_entry.grid(row=0, column=1, padx=10, pady=5)

#Expense label style
expense_label = tk.Label(input_frame, text="Brief about your Expense : ", bg="#428484",font=("Times New Roman",15))
expense_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
expense_entry = tk.Entry(input_frame)
expense_entry.grid(row=1, column=1, padx=10, pady=5)

#Amountspent label style
amountspent_label = tk.Label(input_frame, text="Amount spent (₹) : ", bg="#428484",font=("Times New Roman",15))
amountspent_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
amountspent_entry = tk.Entry(input_frame)
amountspent_entry.grid(row=2, column=1, padx=10, pady=5)

#Intializing data structure to store expenses
expenseslist = {}

#Function to add an expense 
def  addexp():
    expense = expense_entry.get()
    amountspent = amountspent_entry.get()
    monthyear = monthyear_entry.get()
    
    if monthyear not in expenseslist:
        expenseslist[monthyear] = []
    
    if expense and amountspent:
        expenseslist[monthyear].append((expense , float(amountspent)))
        update_listbox(monthyear)
        updatetot(monthyear)
        expense_entry.delete(0,"end")
        amountspent_entry.delete(0,"end")
        monthyear_entry.delete(0,"end")
    else:
        messagebox.showerror("Error !!","Both Expense and amount must be provided !")

#Function to delete an expense from the list
def delexp():
    monthyear = monthyear_entry.get()
    if monthyear in expenseslist:
        selected_item = expense_listbox.curselection()
        if selected_item:
            index = selected_item[0]
            if 0 <= index < len(expenseslist[monthyear]):
                # Get the expense to be deleted
                expense_to_delete = expenseslist[monthyear][index]
                expenseslist[monthyear].remove(expense_to_delete)
                update_listbox(monthyear)
                updatetot(monthyear)
            else:
                messagebox.showerror("Error !!", "Invalid selection.")
        else:
            messagebox.showerror("Error !!", "Please select an expense to delete.")
    else:
        messagebox.showerror("Error !!", "Month/Year not found in expenses list.")


def updateexp():
    selected_item = expense_listbox.curselection()
    expense = expense_entry.get()
    amountspent = amountspent_entry.get()
    monthyear= monthyear_entry.get()
    
    if selected_item and monthyear in expenseslist:
        index = selected_item[0]
        if expense and amountspent:
            expenseslist[monthyear][index]= (expense,float(amountspent))
            update_listbox(monthyear)
            updatetot(monthyear)
            expense_entry.delete(0,"end")
            amountspent_entry.delete(0,"end")
        else:
            messagebox.showerror("Error !!","Both Expense and amount must be provided !")
    else:
        messagebox.showerror("Error","Please select an expense to update the values ")

#Function to update the listbox
def update_listbox(monthyear):
    expense_listbox.delete(0,"end")
    if monthyear in expenseslist:
        for expense , amount in expenseslist[monthyear]:
            expense_listbox.insert("end",f"{expense}  :   ₹{amount:.2f}")

#Function to update the total expenses for the selected month
def updatetot(monthyear):
    total=0
    if monthyear in expenseslist:
        total=sum(amount for _,amount in expenseslist[monthyear])
    total_label.config(text=f"TOTAL EXPENSES FOR {monthyear}: ₹{total:.2f}")

#Function to exit the program
def exitprog():
    root.destroy()


#Button to add current date 
def addcurrdate():
    now = datetime.now()
    currdate=now.strftime("%m/%Y")
    monthyear_entry.insert(0,currdate)

addcurrdate_button = tk.Button(input_frame, text="Add Current Date", command=addcurrdate, bg="#00ecec", fg="black",font=("Times New Roman",12))
addcurrdate_button.grid(row=0, column=2, padx=6, pady=6)

#Add expense button style
addexp_button = tk.Button(input_frame, text="Add Expense", command=addexp, bg="#00ecec", fg="black",font=("Times New Roman",12))
addexp_button.grid(row=3, column=0, columnspan=2,pady=10)

#delete expense button style
delete_button = tk.Button(button_frame, text="Delete Expense", command=delexp, bg="#bef389", fg="black",font=("Times New Roman",12))
delete_button.pack(side="left", padx=10, pady=10)

#update button style
update_button = tk.Button(button_frame, text="Update Expense", command=updateexp, bg="#ff8cff", fg="black",font=("Times New Roman",12))
update_button.pack(side="left", padx=10, pady=10)

#Exit button style
exit_button = tk.Button(button_frame, text="Exit", command=exitprog, bg="gray", fg="black",font=("Times New Roman",12))
exit_button.pack(side="right", padx=10, pady=10)

# Create and style listbox
expense_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, bg="#414141",fg="white",font=("Times New Roman",14))
expense_listbox.pack(fill="both", expand=True, padx=10, pady=5)

#Total expenses label
total_label = tk.Label(button_frame, text="Total Expenses: ₹0.00", bg="#147888",font=("Times New Roman",14))
total_label.pack(padx=10, pady=10)

#Intilalize the listbox with any existing data
update_listbox("")

#Repeat the loop so that the code will execute
root.mainloop()