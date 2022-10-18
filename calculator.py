import tkinter as ttk
app = ttk.Tk()


app.title('My App')
app.geometry('600x400')


ttk.Label(app, text="Calculator", font=('Arial',24)).place(x = 300, y = 50)
ttk.Label(app, text = "Enter Two numbers ", font=('Arial',22)).place(x = 50, y = 100)
f1 = ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result = ttk.Variable(app)


ttk.Entry(app, textvariable=f1, font=('Arial',22)).place(x = 50, y = 150)
ttk.Entry(app, textvariable=f2, font=('Arial',22)).place(x = 450, y = 150)


def cal(op):
    print("I will calculate")
    result.set(eval(f1.get()+op+f2.get()))  #eval() function of strings


ttk.Button(app, text="+", command=lambda:cal('+'), font=('Arial',22)).place(x = 50, y = 250)
ttk.Button(app, text="-", command=lambda:cal('-'), font=('Arial',22)).place(x = 450, y = 250)
ttk.Button(app, text="*", command=lambda:cal('*'), font=('Arial',22)).place(x = 50, y = 350)
ttk.Button(app, text="/", command=lambda:cal('/'), font=('Arial',22)).place(x = 450, y = 350)

ttk.Label(app, text="Result will be decalared soon", font=('Arial',22)).place(x = 50, y= 450)
ttk.Label(app, textvariable=result, font=('Arial',22)).place(x = 450, y = 450)


app.mainloop()