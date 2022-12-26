import tkinter as tk
from pygame import mixer
import random
import keyboard
mixer.init()
window = tk.Tk()
window.title("Colour game")
window.resizable(0,0)
window.geometry("500x500")
colours = ["red","yellow","orange","green","blue","purple","grey"]
words = ["red","yellow","orange","green","blue","purple","grey"]
worrd = words[random.randint(0,len(words)-1)]
currentcolour = ""
recieved = ""
cs=0
started=False
def enter():
        return get()

def get():
    global currentcolour
    global recieved
    global cs
    global started
    currentcolour = str(opt.cget("fg"))
    recieved = str(ent.get())
    
    if currentcolour == recieved:
        print("correct")
        print(recieved)
        ent.delete(0, tk.END)
        opt.config(text=words[random.randint(0,len(words)-1)],fg=words[random.randint(0,len(words)-1)])
        if str(opt.cget("fg")) == str(opt.cget("text")):
            redo()
        cs=cs+1
        hsc.config(text="Score: "+str(cs))
               
 
    else:
        ent.pack_forget()
        opt.pack_forget()
        acc.pack_forget()   
        ent.delete(0, tk.END) 
        lab.pack(padx=5)
        sta.pack(padx=5,pady=7)
        currentcolour=""
        recieved=""
        hsc.config(text="Score: 0")
        started=False
        cs=cs-cs
        
           
def redo():
    opt.config(opt.config(text=words[random.randint(0,len(words)-1)],fg=words[random.randint(0,len(words)-1)]))               
    if str(opt.cget("fg")) == str(opt.cget("text")):
            redo()
    

def start():
    
    global started
    started=True
    print("started")
    lab.pack_forget()
    sta.pack_forget()
    opt.pack(padx=5,pady=4)
    ent.pack(padx=5,pady=9)
    acc.pack(padx=7,pady=9)
    newword()
    

def newword():
    opt.config(text=words[random.randint(0,len(words)-1)],fg=words[random.randint(0,len(words)-1)])
window.bind('f',enter())
lab= tk.Label(text="What colour is the text?",height=5,width=100,font=('Times', 24))
sta= tk.Button(bg="green",text="Begin",command=start,height=5,width=25,font=('Bold', 14))
hsc= tk.Label(text="Score: 0")

ent = tk.Entry(bg="dark grey")
opt = tk.Label(text="aaaaaaa",fg="black",font=('Bold',24),height=10,width=20,bg="black")
acc = tk.Button(command=get,height=3,width=5,bg="green",text="✔")

hsc.pack()
lab.pack(padx=5)
sta.pack(padx=5,pady=7)
mixer.music.load('E:/Pythonprojects/Projects/lobby-classic-game (1).mp3')
mixer.music.play(100)

window.mainloop()