from tkinter import *

window = Tk()
window.title("login page")
window.geometry("450x300")
window.config(background="light green")

username = Label(window,text="Username",bg="light blue",fg="blue",bd=2)
password = Label(window,text="Password ",bg="light blue",fg="blue",bd=2)

user_entry = Entry(window,width=30,bg="dark blue",fg="blue",bd=2).place(x=100,y=30)
password_entry = Entry(window,width=30,bg="dark blue",fg="blue",bd=2,show="*").place(x=100,y=90,)

submit_button = Button(window,text="Submit credentials",command=window.destroy).place(x=175,y=120)


username.place(x=30,y=30)
password.place(x=30,y=90)

user_val = user_entry.get()
password_val = password_entry.get()

print(user_entry,password_entry)


window.mainloop()