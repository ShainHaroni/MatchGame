from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random

TileMatchScreen = Tk()
TileMatchScreen.title("Tile Matching Game")
TileMatchScreen.geometry("460x450")

matches = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(matches)

myFrame = Frame(TileMatchScreen)
myFrame.pack(pady=10,padx=10)

countMatch = 0
matchWinner = 0
answerList = []
answerDict = {}

def resetGame():
    global matches, winner
    winner = 0
    response = messagebox.askquestion("Restart","Are you Sure ?")
    if response == "no":
        pass
    else:
        matches = [1,1,2,2,3,3,4,4,5,5,6,6]
        random.shuffle(matches)

        buttonList = [buttonMatch1,buttonMatch2,buttonMatch3,buttonMatch4,buttonMatch5,buttonMatch6,buttonMatch7,buttonMatch8,buttonMatch9,buttonMatch10,buttonMatch11,buttonMatch12]

        for button in buttonList:
            button.config(text=" ", bg="SystemButtonFace",state="normal")


def exit():
    response = messagebox.askquestion("Exit","Are you Sure ?")
    if response == "yes":
        TileMatchScreen.destroy()
    else:
        pass

def winnerMatch():
    
    buttonList = [buttonMatch1,buttonMatch2,buttonMatch3,buttonMatch4,buttonMatch5,buttonMatch6,buttonMatch7,buttonMatch8,buttonMatch9,buttonMatch10,buttonMatch11,buttonMatch12]

    for button in buttonList:
        button.config(bg="lightgreen")
    congratulations()

def buttonMatching(b,number):

    global countMatch, answerList, answerDict, matchWinner

    if b["text"] == " " and countMatch < 2:
        b["text"] = matches[number]
        answerList.append(number)
        answerDict[b] = matches[number]
        countMatch += 1

    if len(answerList) == 2:
        if matches[answerList[0]] == matches[answerList[1]]:
            messagebox.showinfo("Correct","Correct, Good job!")
            for key in answerDict:
                key["state"] = "disabled"
            countMatch = 0
            answerList = []
            answerDict = {}
            matchWinner +=1
            if matchWinner == 6:
                winnerMatch()
                
        else:
            countMatch = 0
            answerList = []
            messagebox.showinfo("Incorrect","Incorrect!")

            for key in answerDict:
                key["text"] = " "

            answerDict = {}

def congratulations():
    messagebox.showinfo("Congratulations", "Win! ")

global buttonMatch1, buttonMatch2, buttonMatch3, buttonMatch4, buttonMatch5, buttonMatch6, buttonMatch7, buttonMatch8, buttonMatch9, buttonMatch10, buttonMatch11, buttonMatch12, myMatchingLable  

buttonMatch1 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch1,0),relief="groove")

buttonMatch2 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch2,1),relief="groove")

buttonMatch3 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch3,2),relief="groove")

buttonMatch4 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch4,3),relief="groove")

buttonMatch5 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch5,4),relief="groove")

buttonMatch6 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch6,5),relief="groove")

buttonMatch7 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch7,6),relief="groove")

buttonMatch8 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch8,7),relief="groove")

buttonMatch9 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch9,8),relief="groove")

buttonMatch10 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch10,9),relief="groove")

buttonMatch11 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch11,10),relief="groove")

buttonMatch12 = Button(myFrame, text = " ", font=("Sans",20,'bold'),height=3, width=6,command=lambda:buttonMatching(buttonMatch12,11),relief="groove")

buttonMatch1.grid(row=0, column=0)
buttonMatch2.grid(row=0, column=1)
buttonMatch3.grid(row=0, column=2)
buttonMatch4.grid(row=0, column=3)

buttonMatch5.grid(row=1, column=0)
buttonMatch6.grid(row=1, column=1)
buttonMatch7.grid(row=1, column=2)
buttonMatch8.grid(row=1, column=3)

buttonMatch9.grid(row=2, column=0)
buttonMatch10.grid(row=2, column=1)
buttonMatch11.grid(row=2, column=2)
buttonMatch12.grid(row=2, column=3)
TileMatchScreen.config(bg="grey")

myMenuMatch = Menu(TileMatchScreen)
TileMatchScreen.config(menu=myMenuMatch)
optionMenuMatch = Menu(myMenuMatch,tearoff=False)
myMenuMatch.add_cascade(label="Options", menu=optionMenuMatch)

optionMenuMatch.add_command(label="Reset Game",command = resetGame)
optionMenuMatch.add_command(label="Exit",command = exit)

TileMatchScreen.mainloop()