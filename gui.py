import tkinter as tk
from tkinter import StringVar, OptionMenu
from task3a import Customer
from task3b import Visit
from tkinter import messagebox


window = tk.Tk()


window.title("Class Calculator - 22225745")
# window.iconbitmap("changeicon.png")
window.configure(background='green')
window.geometry("1000x500")

# rCoins = set()
def exitApp():
    print("Ending App...")
    window.destroy()



def get_info():
    """ This function instantiates the various classs"""
    # get customer name
    customer_name = name_entry.get()
    # get customer member type
    member_type = member_dropdown.get()
    
    try:
        # get service expense
        service_expense = float(service_entry.get())
        # get product expense
        product_expense = float(product_entry.get())
    except ValueError:
        messagebox.showerror('Python Error', 'Error: Please Enter a number!')
    
    
    date_visited = date_visit_entry.get()

    
    # creatte an instance of the class customer
    customer1 = Customer(name=customer_name, memberType=member_type)

    # create instance of class visitor
    visitor1 = Visit(name = customer_name,date=date_visited)

    visitor1.setName(customer_name)
    visitor1.setMemberType(member_type)
    visitor1.setServiceExpense(float(service_expense))
    visitor1.setProductExpense(float(product_expense))

    disc_service_exp = visitor1.getServiceExpense()
    disc_prod_exp = visitor1.getProductExpense()


    # display the discounted prices and the total
    original_result.configure(text= f""" £{service_expense}\n
 £{product_expense} \n
 Total Expense :  £{float(service_expense) + float(product_expense) : .2f} \n
""")
                              
    # display the discounted prices and the total
    discount_result.configure(text= f""" £{disc_service_exp}\n
 £{disc_prod_exp}\n
  Total Expense: {visitor1.getTotalExpense()}\n
""")
                              
    
    
    
# Text Title
text_title =tk.Label(text="Discount Machine...", 
                   font=('Time New Roman', 24,'bold'),
                   bg ='black',
                   fg='white') 
text_title.grid(row=0,column=0,columnspan=3,pady=(3,10))

#Name Entry
text_name =tk.Label(text="Enter Your Name : ", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
text_name.grid(row=1,column=0, sticky=tk.E, padx=(5,5))

name_entry = tk.Entry(text="", 
                   font=('Time New Roman', 12,'bold') ) 
name_entry.grid(row=1,column=1, columnspan=6,pady=(5,5) )


#Member Entry
text_member =tk.Label(text="Enter Your Memeber Type : ", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
text_member.grid(row=2,column=0, sticky=tk.E, padx=(5,5))

# create dropdown menu for memership type
member_dropdown = StringVar()
member_dropdown.set("Member Type")

# create dropdown
dropdown = OptionMenu(window, member_dropdown, "Premium", "Gold", "Silver")
# member_dropdown.pack()
dropdown.grid(row=2,column=1, columnspan=6,pady=(5,5) )


#Ervice Expense
service_expense =tk.Label(text="Service Expense : ", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
service_expense.grid(row=3,column=0, sticky=tk.E, padx=(5,5))

service_entry = tk.Entry(text="", 
                   font=('Time New Roman', 12,'bold') ) 
service_entry.grid(row=3,column=1, columnspan=6,pady=(5,5) )

#Product Entry
product_expense =tk.Label(text="Product Expense : ", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
product_expense.grid(row=4,column=0, sticky=tk.E, padx=(5,5))

product_entry = tk.Entry(text="", 
                   font=('Time New Roman', 12,'bold') ) 
product_entry.grid(row=4,column=1, columnspan=6,pady=(5,5) )

#Date Visited
date_visit =tk.Label(text="Date Visited : ", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
date_visit.grid(row=5,column=0, sticky=tk.E, padx=(5,5))

date_visit_entry = tk.Entry(text="", 
                   font=('Time New Roman', 12,'bold') ) 
date_visit_entry.grid(row=5,column=1, columnspan=6,pady=(5,5) )


# Breakdown of Expense
original_expense =tk.Label(text="Original Expense  ", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
original_expense.grid(row=1,column=30, sticky=tk.E, padx=(5,5))

# display Original prices
original_result = tk.Label(text='', 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
original_result.grid(row=2,column=30, pady=(10,2))


discounted_expense =tk.Label(text="Discounted Expense ", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
discounted_expense.grid(row=1,column=40, sticky=tk.E, padx=(5,5))

# display discounted prices
discount_result = tk.Label(text='', 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
discount_result.grid(row=2,column=40, pady=(10,2))


# Exec button
btnExe = tk.Button(text="Calculate", command=get_info, width=10,height=2)
btnExe.grid(row=7,column=1)

btnQuit = tk.Button(text="Quit", command=exitApp, width=10,height=2)
btnQuit.grid(row=7,column=2)


window.mainloop()


