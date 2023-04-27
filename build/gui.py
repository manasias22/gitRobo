from pathlib import Path
import miniproj as mnp
from tkinter import END, Tk, Entry,Canvas, Button, PhotoImage, filedialog
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_data():
    if (entry_1.get()!=""):    
        mnp.getcmtmsg(entry_1.get())
    entry_1.delete(0,END)
def get_link():
    if (entry_1.get()!=""):    
        mnp.gitrmtadd(entry_1.get())
    entry_1.delete(0,END)
        
def set_mail():
    if (entry_1.get()!=""):
        mnp.gitsetmail(entry_1.get())
    entry_1.delete(0,END)
def set_uname():
    if (entry_1.get()!=""):
        mnp.gitsetuname(entry_1.get())
    entry_1.delete(0,END)
    
def dir__lol():
    window.directory = filedialog.askdirectory()
    print (window.directory)
    os.chdir(window.directory)
    mnp.filechange()
    mnp.chd()

window = Tk()

window.geometry("1188x700")
window.configure(bg = "#4B6893")

window.title("GitMeUp")

canvas = Canvas(
    window,
    bg = "#4B6893",
    height = 825,
    width = 1188,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    594.0,
    412.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    594.0,
    412.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    880.0,
    797.0,
    image=image_image_3
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    763.0,
    215.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)

#lol
entry_1.place(
    x=617.0,
    y=194.0,
    width=292.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_2= canvas.create_image(
    763.0,
    215.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)

#lol
entry_2.place(
    x=194.0,
    y=600.0,
    width=292.0,
    height=40.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= get_data,
    relief="flat"
)
button_1.place(
    x=33.0,
    y=239.69232177734375,
    width=380.0,
    height=56.30767822265625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=dir__lol,
    relief="flat"
)
button_2.place(
    x=33.0,
    y=75.0,
    width=378.26202392578125,
    height=56.29327392578125
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=mnp.gitpush,
    relief="flat"
)
button_3.place(
    x=33.0,
    y=323.55780029296875,
    width=381.0,
    height=56.44219970703125
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=mnp.status,
    relief="flat"
)
button_4.place(
    x=33.0,
    y=406.0,
    width=378.26202392578125,
    height=58.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=mnp.gitadd,
    relief="flat"
)
button_5.place(
    x=35.0,
    y=155.82681274414062,
    width=379.0,
    height=56.29327392578125
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=set_uname,
    relief="flat"
)
button_6.place(
    x=760.0,
    y=334.0,
    width=401.4213562011719,
    height=57.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=get_link,
    relief="flat"
)
button_7.place(
    x=762.6114501953125,
    y=586.0146484375,
    width=401.0378723144531,
    height=56.29327392578125
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=mnp.gitusmail,
    relief="flat"
)
button_8.place(
    x=762.0,
    y=417.0,
    width=402.0,
    height=58.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=set_mail,
    relief="flat"
)
button_9.place(
    x=760.0,
    y=501.9249267578125,
    width=404.0,
    height=57.0750732421875
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=mnp.gituser,
    relief="flat"
)
button_10.place(
    x=761.0,
    y=250.0,
    width=404.0,
    height=57.0
)

canvas.create_text(
    414.0,
    162.5224609375,
    anchor="nw",
    text="Adds files to staging area",
    fill="#00FF56",
    font=("MontaguSlab Regular", 20 * -1)
)

canvas.create_text(
    414.0,
    239.5224609375,
    anchor="nw",
    text="commits the file",
    fill="#00FF56",
    font=("MontaguSlab Regular", 20 * -1)
)

canvas.create_text(
    413.0,
    328.0,
    anchor="nw",
    text="Pushes the file to remote repository",
    fill="#00FF56",
    font=("MontaguSlab Regular", 20 * -1)
)

canvas.create_text(
    38.0,
    470.5224609375,
    anchor="nw",
    text="Shows the status of the changes made ",
    fill="#00FF56",
    font=("MontaguSlab Regular", 20 * -1)
)

canvas.create_text(
    550.0,
    423.0,
    anchor="nw",
    text="shows you the mail id",
    fill="#00FF56",
    font=("MontaguSlab Regular", 20 * -1)
)

canvas.create_text(
    500.0,
    506.0,
    anchor="nw",
    text="Lets you edit your mail id.",
    fill="#00FF56",
    font=("MontaguSlab Regular", 20 * -1)
)

canvas.create_text(
    550.0,
    592.0,
    anchor="nw",
    text="Add remote repo link",
    fill="#00FF56",
    font=("MontaguSlab Regular", 20 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1025.0,
    147.0,
    image=image_image_4
)

window.resizable(False, False)
window.mainloop()
