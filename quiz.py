from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Trivia-to-Go')
#root.iconbitmap()

frame = Frame(root, padx=20, pady=20)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

r = IntVar()
r.get()

def clicked(value):
    myLabel = Label(root, text = r.get())
    myLabel.pack()
    
Radiobutton(root, text = "", variable=r, value=1).pack()
Radiobutton(root, text = "", variable=r, value=2).pack()
Radiobutton(root, text = "", variable=r, value=3).pack()
Radiobutton(root, text = "", variable=r, value=4).pack()



myButton= Button(root, text= "Submit Answer", command=lambda:clicked(r.get()))
myButton.pack()                

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()



