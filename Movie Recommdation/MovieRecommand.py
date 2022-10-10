import tkinter as ttk
#Importing the Libraries
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


app = ttk.Tk()

app.title("Movie Recommender")
app.geometry("900x600")

#Reading the Data Files
cols = ['user_id', 'movie_id', 'rating', 'ts']
df = pd.read_table('D:\Machine Learning\Movie Recommdation\u.data', sep = '\t', names = cols).drop('ts', axis = 1)
item_cols = ['movie_id', 'titles'] + [str(i) for i in range(22)]
df1 = pd.read_csv('u.item', sep = '|', names = item_cols, encoding = "ISO-8859-1")[['movie_id', 'titles']]
    
#Merging the two Data Frames
movie = pd.merge(df, df1, on = 'movie_id')


result = ttk.Variable(app)
box = ttk.Listbox(app, height=10, fg='red', activestyle='dotbox')
for row, val in movie.iterrows() :
    box.insert(row+1, val('title'))


box.place(x = 10, y = 10)

def getMovie():
    pass

ttk.Button(app, text = "Find Recommandation" , command = getMovie, font = ("Arial",22)).place(x = 300 , y = 10)
ttk.Label(app, textvariable=result, font=('Arial',22)).place(x = 300 , y = 100)

app.mainloop()