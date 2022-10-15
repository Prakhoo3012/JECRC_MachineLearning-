from gettext import npgettext
import tkinter as ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 
from PIL import ImageTk, Image
print('Location is:', os.getcwd(), '\n\n\n')

data = pd.read_csv('treadmil-users.csv')

app = ttk.Tk()
app.geometry('600x300')
app.title('Trademill Users Analysis')

## Radio Button

##rb1 = ttk.Variable(app)
#values = {'Data 1': '1', 'Data 2': '2'}
#for key, value in values.items():
 #   ttk.Radiobutton(app, text = key, variable=rb1, value= value).pack()

#def show():
 #   print(rb1.get())

#ttk.Button(app, text='show', command= show).place(x=400, y=10)

#Radio Button

graphs = ttk.Variable(app)
values = {  
    'Pair Plot': "sns.pairplot(data=data)", 
    'Joint Plot': "sns.jointplot(data=data, x='{}')", 
    'Bar Plot': "sns.barplot(data = data, x='{col1}', y='{col2}')",
    'Box Plot': "sns.boxplot(data = data, x='{col1}', y='{col2}')"
}

graphs.set(values['Pair Plot'])
y=10
for key, value in values.items():
    ttk.Radiobutton(app, text=key, variable=graphs, value=value).place(x = 10, y = y)
    y += 20

##Option Menu 1
col1 = ttk.Variable(app)
values = ['select']+list(data.columns)
col1.set(values[0])
ttk.Label(app, text='Column 1').place(x = 150, y = 10)
ttk.OptionMenu(app, col1, *values).place(x = 150, y = 40)

##Option Menu 2
col2 = ttk.Variable(app)
col2.set(values[0])
ttk.Label(app, text='Column 2').place(x = 150, y = 80)
ttk.OptionMenu(app, col2, *values).place(x = 150, y = 110)

##Option Menu 3
col3 = ttk.Variable(app)
col3.set(values[0])
ttk.Label(app, text='Column 3').place(x = 150, y = 150)
ttk.OptionMenu(app, col3, *values).place(x = 150, y = 180)

# Canvas Widget
cnv = ttk.Canvas(app, width = 250, height = 200)
cnv.place(x = 300, y = 100)

#Label 
result = ttk.Variable(app)
ttk.Label(app, textvariable=result).place(x=300,y=300)


def show():

    global img
    global cnv

     #print(graphs.get())
    #print(col1.get(), col2.get(), col3.get())
    #g = graphs.get()
    column1 = col1.get() 
    column2 = col2.get()
    column3 = col3.get()

    g = graphs.get()
    if 'col1' in g:
        if column1 == 'select':
            result.set('Column1 must be selected')
            return

    if 'col2' in g:
        if column2 == 'select':
            result.set('Column2 must be selected')
            return
    
    if 'col3' in g:
        if column3 == 'select':
            result.set('Column3 must be selected')
            return

    fig =plt.figure(figsize=(10,3))
    eval(g.format(col1 = column1, col2=column2, col3=column3))
    result.set('Sucess')
    fig.savefig("myg.png")
    img = ImageTk.PhotoImage(Image.open('myg.png').resize((250,200)))
    cnv.create_image(0, 0, anchor = ttk.NW, image = img)
        #plt.show()


ttk.Button(app, text='show', command=show).place(x = 400, y = 10)


app.mainloop()