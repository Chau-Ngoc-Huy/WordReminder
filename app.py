from cProfile import label
from cgitb import text
import tkinter
from tkinter import messagebox
from turtle import left
from translate import translate
from tkinter import *
import random
import time

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        with open('./words.txt') as f:
            self.words = f.read().splitlines()
        self.master = master
        master.title('Word Reminder')
        self.master.geometry('350x350')

        self.wordLabel = Label(master, text='word', font=('Helvetica', 30), pady=20)
        self.wordLabel.grid(column=0, row=0)

        self.defText = Text(master, width=45, height=5, padx=10,pady=10)
        self.defText.insert(tkinter.END, 'Defination: ')
        self.defText.grid(column=0, row=1, sticky=W)

        self.wordText = StringVar()
        self.inputEntry = Entry(master, textvariable=self.wordText, font=('Helvetica', 16))
        self.inputEntry.grid(column=0, row=2, pady=20)

        self.searchBtn = Button(text='Search', command=self.Search)
        self.searchBtn.grid(column=0, row=3, sticky=W, padx=30)

        self.addBtn = Button(text='Add', command=self.AddWord)
        self.addBtn.grid(column=0, row=3, sticky=E, padx=30)

    def Search(self):
        self.insertWord(self.wordText.get())

    def isExist(self, word):
        return word in self.words

    def AddWord(self):
        word = self.wordText.get()
        if (self.isExist(word)):
            messagebox.showinfo("Error", "This word existed")
        else:
            with open('./words.txt', 'a') as f:
                f.write(word + '\n')
            self.words.append(word)
            messagebox.showinfo("Complete", "This word added to word list")

    def insertWord(self, word):
        self.wordLabel['text'] = word
        defination = translate(word)
        self.defText.delete('1.0', END)
        self.defText.insert(tkinter.END, 'Defination: ' + defination[0])

    def resetWord(self):
        word = self.words[random.randint(0, len(self.words)-1)]
        # while(defination == []):
        #     print(word, defination)
        #     defination = translate(word)
        self.insertWord(word)
        self.master.withdraw()
        self.master.deiconify()
        self.after(60000, self.resetWord)

word = 'confident'
defination = translate(word)


root = Tk()
app = App(root)
root.after(1, app.resetWord)
app.mainloop()




