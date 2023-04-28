#Import the required libraries
from tkinter import *
import webbrowser

#Create an instance of tkinter frame
win = Tk()
win.geometry("750x250")

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = Label(win, text="www.tutorialspoint.com",font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("http://www.tutorialspoint.com"))

win.mainloop()