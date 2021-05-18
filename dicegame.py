import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.geometry('450x200')
root.title('Python Dice Game')


l0 = tkinter.Label(root, text="")
l0.pack()

l1 = tkinter.Label(root, text="Dice Rolling Stimulator", fg = "Blue",
        bg = "yellow",
        font = "Helvetica 16 bold italic")
l1.pack()

dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image=image1)
label1.image = image1

label1.pack( expand=True)

def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1

button = tkinter.Button(root, text='Roll the Dice', fg='Blue',bg='yellow',command=rolling_dice,font = "Helvetica 16 bold italic")

button.pack( expand=True)

root.mainloop()