## GUI -- Graphical User Interface

#libraries
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app = ttk.Tk()


app.title('My App')
app.geometry('600x400')

ttk.Label(app, text = "A Simple Text Label").place(x = 50, y = 50)
#ttk.Label(app, text = "Prakhar Kulshrestha").place(x = 50, y = 100) 
# #configration and placement
#vigit

def abc() :
    print("Wow")

ttk.Button(app, text = "Isko dabba do", command = abc).place(x = 100, y = 100)
ttk.Button(app, text = "Isko bhi dabba de", command = lambda:print("Hey!! Buddy")).place(x = 100, y =130)

#a func can be assigned to an identifer
#func can be taken as input argument in another func
#func can be defined under another func
#a func can be returned from another func



app.mainloop()