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

ttk.Label(app, text = "A Simple Text Label", font=('Arial',22)).place(x = 50, y = 50)
ttk.Label(app, textvariable=message).place(x = 50, y = 100) 
# #configration and placement
#vigit

def abc() :
    print("Wow")
    message.set("Jo tera mann kare")

ttk.Button(app, text = "Isko dabba do", font=('Arial',22), command = abc).place(x = 50, y = 150)
ttk.Button(app, text = "Isko bhi dabba de", font=('Arial',22), command = lambda:message.set("Pata Nahi")).place(x = 450, y = 150)

#a func can be assigned to an identifer
#func can be taken as input argument in another func
#func can be defined under another func
#a func can be returned from another func

ttk.Label(app, text = "Enter Two numbers below", font=('Arial',22)).place(x = 50, y = 300)
f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result = ttk.Variable(app)


ttk.Entry(app, textvariable=f1, width = 4, font=('Arial',22)).place(x = 50, y = 350)
ttk.Entry(app, textvariable=f2, font=('Arial',22)).place(x = 50, y = 450)


def cal(op):
    print("I will calculate")
    result.set(eval(f1.get()+op+f2.get()))  #eval() function of strings


ttk.Button(app, text="+", command=lambda:cal('+'), font=('Arial',22)).place(x = 50, y = 550)
ttk.Button(app, text="-", command=lambda:cal('-'), font=('Arial',22)).place(x = 450, y = 550)
ttk.Button(app, text="*", command=lambda:cal('*'), font=('Arial',22)).place(x = 50, y = 650)
ttk.Button(app, text="/", command=lambda:cal('/'), font=('Arial',22)).place(x = 450, y = 650)

ttk.Label(app, text="Result will be decalared soon", font=('Arial',22)).place(x = 50, y= 750)
ttk.Label(app, textvariable=result, font=('Arial',22)).place(x = 450, y = 750)

###List Box

box = ttk.Listbox(app, height=5, fg='red', activestyle='dotbox')
box.insert(1, 'Sample1')
box.insert(2, 'Sample2')
box.insert(3, 'Sample3')
box.place(x = 1000, y = 450)

def show():
    print(box.get(box.curselection()))

    

ttk.Button(app, text = 'show', command=show).place(x = 350, y = 350)



app.mainloop()