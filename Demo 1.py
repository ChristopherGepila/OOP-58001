from tkinter import *
window = Tk()
window.geometry("500x400+100+200")
window.title("My first GUI")

btn1 = Button(window, text = "Click Here", fg = "Red", bg = "Yellow")
btn1.place(x = 220, y = 100)
txtfld = Entry(window, border = 5)
txtfld.place(x = 100, y = 50)

lbl = Label(window, text = "My First Demo", font = "Verdana")
lbl.place(x = 50, y = 20)


window.mainloop()