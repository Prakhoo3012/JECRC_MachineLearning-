import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import* 
from PIL import Image,ImageTk

# Create an instance of ktinker frame
win = Tk()

#Set geometry of tkinter frame
win.geometry("750x270")

#Create a canvas 
canvas = Canvas(win, width = 600, height = 400)
canvas.pack()

#Load an image in the script
img = ImageTk.PhotoImage(Image.open("mygraph.png"))

#Add image to canvas Items
canvas.create_image(10, 10, anchor=NW, image=img)

win.mainloop()