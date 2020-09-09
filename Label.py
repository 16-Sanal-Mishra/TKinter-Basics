from tkinter import *

window = Tk()
window.title("Movie Recommendation System")
window.configure(background="grey")
l1 = Label(window, text="Movie Recommendation System", bg="#FFFFAA", fg="blue", font="Times 20 bold underline")
l1.pack()
bt = Button(window, text="Login").pack()

window.mainloop()
