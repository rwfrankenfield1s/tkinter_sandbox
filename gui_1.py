from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter

def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


def ClearBox():
    Lb1.delete(0,'end')




master = Tk()
menu = Menu(master) 
master.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New', command= ClearBox)
filemenu.add_command(label='Save')
filemenu.add_command(label='Open...', command= OpenFile) 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=master.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

#######################################################################
#######################################################################

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    name.set(('You added',e1.get(), e2.get(),"to the list!"))
    Lb1.insert(1, (e1.get(), e2.get()))



Label(master,text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
name = StringVar()        
Label(master, textvariable=name).grid(row=0,column=6)



e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


#######################################################################
#######################################################################


Lb1 = Listbox(master)
Lb1.grid(row=5,column=8)

#######################################################################
#######################################################################


Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=W, 
                                    pady=4)





Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=W, 
                                                       pady=4)




mainloop()
