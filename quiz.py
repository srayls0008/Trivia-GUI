from tkinter import *
# from PIL import ImageTk,Image
from tkinter import messagebox
import sys

#questions and anwers to pull from
question= [
    "Q1. What was the first state?",
    "Q2. What is the name of Mickey Mouse's girlfriend",
    "Q3. What is the largest land mammal?",
    "Q4. Which US city is home to the Space Needle?",
    "Q5. Who was the first president of the US?"
  ]

answer= [
    4,
    2,
    3,
    2,
    1
  ]

option1= [
     "Indiana",
     "Daisy",
     "Tiger",
     "New York",
     "Washington"
    ]

option2= [
      "Kentucky",
      "Minnie",
      "Anteater",
      "Seattle",
      "Carver"
    ]

option3= [
      "California",
      "Ethel",
      "Elephant",
      "Miami",
      "Obama"
      
    ]

option4= [
      "Delaware",
      "Ruby",
      "Gorilla",
      "San Antonio",
      "Disney"
    ]



    
#start window
root = Tk()
root.title('Begin Trivia')
root.iconbitmap()

#set window size
root.geometry("300x200")

#creating the frame
frame = LabelFrame(root, padx=10, pady=10)
frame.pack(padx=15, pady=15)



#trivia window
global x
x=0
def openFunction():
    top = Toplevel()
    top.title("Trivia-to-Go")
    top.geometry("500x500")
    
    
    #creating the frame
    frame = LabelFrame(top, padx=10, pady=10)
    frame.pack(padx=15, pady=15)

    #shows the question
    LabelQuestion = Label(frame, text="") 
    LabelQuestion.pack() 
    
    

    r = IntVar()
    r.get()


    #function that shows what was clicked
    def clicked(value):
        global x
        myLabel = Label(frame, text = r.get())
        myLabel.pack()
        #messagebox.showinfo("Results", r.get())
        if r.get() == answer[x]:
            messagebox.showinfo("Results", "Correct")
        else:
            messagebox.showinfo("Results", "Incorrect")
        x+=1
        if x == 5:
            sys.exit()
            
        
        
        openFunction()

    #create radio buttons    
    radio1 = Radiobutton(frame, text = "", variable=r, value=1)
    radio2 = Radiobutton(frame, text = "", variable=r, value=2)
    radio3 = Radiobutton(frame, text = "", variable=r, value=3)
    radio4 = Radiobutton(frame, text = "", variable=r, value=4)

    radio1.pack()
    radio2.pack()
    radio3.pack()
    radio4.pack()

    #display questions and answers
    LabelQuestion.config(text = question[x])
    radio1.config(text = option1[x])
    radio2.config(text = option2[x])
    radio3.config(text = option3[x])
    radio4.config(text = option4[x])



    #submit answer and quit buttons
    myButton= Button(frame, text= "Submit Answer", command=lambda:clicked(r.get()))
    myButton.pack()
    

    button_quit = Button(frame, text="Exit Program", command=top.destroy)
    button_quit.pack()

btn = Button(root, text = "Start", padx = 50, pady = 10, command = openFunction)
btn.pack()

mainloop()



