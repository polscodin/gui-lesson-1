from tkinter import*

window = Tk()
window.geometry("800x400")


button1 = Button(window,text="button1",command=window.destroy)
button2 = Button(window,text="button2",command=window.destroy)
button3 = Button(window,text="button3",command=window.destroy)
button1.pack(side="bottom")
button2.pack(side="left")
button3.pack(side="right")

window.mainloop()