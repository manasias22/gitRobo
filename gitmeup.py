from tkinter import *
from tkinter import filedialog
from tkinter import font

root=Tk()
root.title('Git Me Up!')
#root.iconbitmap('c:/gui/codem.ico')
root.geometry("1200x660")
#create new file funtion 
def new_file():
    #delete previous text
    my_text.delete('1.0',END)
    #update ststus bars
    root.title('New File - Git Me Up!')
    status_bar.config(text='new file      ')
#open files
def open_file():
    #delete previous text
    my_text.delete('1.0',END)
    #grab file name
    text_file=filedialog.askopenfilename(initialdir='c:/gui/',title='open file',filetypes=(('text files','*.txt'),('html files','*.html'),('python files','*.py'),('all files','*.*'),('word files','*.word')))
    #check to see if there is filename
    if text_file:
        #make filename global so we can access it later
        global open_status_name
        open_status_name = text_file

    #update status bars
    name=text_file
    status_bar.config(text=f'{name}        ')
    name=name.replace('c:/gui/',"")
    root.title(f'{name} - Git Me Up!')
    #open file
    text_file=open(text_file,'r')
    stuff=text_file.read()
    #add file to textbox
    my_text.insert(END,stuff)
    #close the opened file
    text_file.close()
#save as files
def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension='.*',initialdir='c:/gui/',title='save file',filetypes=(("text files","*.txt"),('HTML files','*.html'),('python files','*.py'),('all files','*.*'),('pdf files','*.pdf'),('word file','*.word')))
    if text_file:
        #update status bars
        name=text_file
        status_bar.config(text=f'saved:{name}        ')
        name=name.replace('c:/gui/',"")
        root.title(f'{name} - Git Me Up!')
        #save the file
        text_file=open(text_file,'w')
        text_file.write(my_text.get(1.0,END))
        #close the file
        text_file.close()


#create main frame
my_frame= Frame(root)
my_frame.pack()

#create our scroll bar for text box
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#create text box
my_text = Text(my_frame,width=97,height=25,font=("calibari",16),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll.set)
my_text.pack()
#configure scroll bar
text_scroll.config(command=my_text.yview)
#create menu
my_menu= Menu(root)
root.config(menu=my_menu)
#add file menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
#add edit menu
edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Paste")

#add status bar
status_bar = Label(root,text='Ready',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)


root.mainloop()




