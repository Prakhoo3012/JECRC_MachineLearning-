## GUI -- Graphical User Interface

#libraries
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app = ttk.Tk()


app.title('My App')
app.geometry('600x400')

message = ttk.Variable(app)

ttk.Label(app, text = "A Simple Text Label").place(x = 50, y = 50)
ttk.Label(app, textvariable=message).place(x = 50, y = 100) 
# #configration and placement
#vigit

def abc() :
    print("Wow")
    message.set("Jo tera mann kare")

ttk.Button(app, text = "Isko dabba do", command = abc).place(x = 50, y = 150)
ttk.Button(app, text = "Isko bhi dabba de", command = lambda:message.set("Pata Nahi")).place(x = 450, y = 150)

#a func can be assigned to an identifer
#func can be taken as input argument in another func
#func can be defined under another func
#a func can be returned from another func



app.mainloop()