#to attempt to rave type in "_rave_" into the Entry box (with underscores) and click "Apply"
from random import *
from tkinter import *
from time import *
import colorsys

h = open("haikus.txt","r")
haikus = h.readlines()

def haiku_temp(i):
    haiku = haikus[i*4]+haikus[i*4+1]+haikus[i*4+2]
    return haiku

def rewrite(words,haikut):
    haiku_rewritten = ""
    j = 0
    k = 0
    print(len(words))
    if words[0]=="" or words[0][0]==" ":
        haiku_rewritten=haikut
    else:
        while j< len(haikut):
            if haikut[j] == "{":
                haiku_rewritten+= words[k].strip(",")
                if len(words)>k+1:
                    k+=1
                j+=2
            else:
                haiku_rewritten+=haikut[j]
                j+=1
    return haiku_rewritten


class App(Frame):
    def __init__(self,win):
        self.win = win
        self.win.title("Haiku Generator")
        super().__init__(self.win)
        self.grid(rows=300,columns=5,padx=100,pady=1)
        self.place()
        
        self.win.geometry("380x230")
        self.Sucelje()
        
    def Sucelje(self):
        self.h=Label(self,text="")
        self.h.grid(row=1,column = 38)
        self.i = randint(0,len(haikus)/4-1)
        
        self.haikut = haiku_temp(self.i)
        self.htemp=Label(self,text=self.haikut,width=25)
        self.htemp.grid(row=2,column = 3)
        self.box = Entry(self,width=23)
        self.box.grid(row=3,column=3)
        
        self.button = Button(self,text="Apply",command=self.ApplyWords,width=12)
        self.button.grid(row=5,column=3,pady=5)

        self.left = Button(self,text="<",command = self.GoLeft)
        #self.left.grid(row=4,column=2)
        self.left.place(x=20,y=111)
        
        self.right = Button(self,text=">",command = self.GoRight)
        #self.right.grid(row=4,column=4)
        self.right.place(x=140,y=111)

        self.button = Button(self,text="Color",command=self.color,width=12)
        self.button.grid(row=6,column=3,pady=5)

        self.rave = False
        self.raveButton = Button(self,text="RAVE",command=self.toggleRave,width=12)
        self.raveButton.grid(row=7,column=3,pady=5)
        
      
    def ApplyWords(self):
        self.words = self.box.get().split(" ")
        print(self.words)
        if self.words[0]!="_rave_":
            self.haikut_new = rewrite(self.words,self.haikut)
            self.htemp.config(text=self.haikut_new)
        else:
            self.t0 = time()
            self.t1 = time()
            while self.t1-self.t0<3:
                if time()!=self.t1:
                    self.color()
                    self.t1=time()

    def GoLeft(self):
        self.change_i(-1)
        self.haikut = haiku_temp(self.i)
        self.htemp.config(text=self.haikut)

    def GoRight(self):
        self.change_i(1)
        self.haikut = haiku_temp(self.i)
        self.htemp.config(text=self.haikut)    

    def change_i(self,j):        
        self.i+=j
        if (self.i<0):
            self.i=int(len(haikus)/4-1)
        if (self.i>len(haikus)/4-1):
            self.i=0         
        print(self.i)

    def color(self):
        self.r=randint(220,255)
        self.g=randint(220,255)
        self.b=randint(220,255)

        color = (self.r, self.g, self.b)
        self.win.config(bg="#%02x%02x%02x"%color)
        self.h.config(bg="#%02x%02x%02x"%color)
        self.htemp.config(bg="#%02x%02x%02x"%color)
        self.config(bg="#%02x%02x%02x"%color)

    def toggleRave(self):
        self.rave = not(self.rave)
    
    def doRave(self): 
        color = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(time()*0.3,1,1))
        self.win.config(bg="#%02x%02x%02x"%color)
        self.h.config(bg="#%02x%02x%02x"%color)
        self.htemp.config(bg="#%02x%02x%02x"%color)
        self.config(bg="#%02x%02x%02x"%color)
        




a=App(Tk())

#same as a.mainloop() but now you can add a.color() to run every 'frame'
while True:
    a.update_idletasks()
    a.update()
    if(a.rave):
        a.doRave()
