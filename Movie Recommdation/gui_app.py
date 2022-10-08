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
ttk.Label(app, text = "Prakhar Kulshrestha").place(x = 50, y = 100)



app.mainloop()