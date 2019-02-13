'''
__author__ = Aditya Singh
__title__  = paint app
__date__   = 24 November 2018

'''
import tkinter
from tkinter.colorchooser import askcolor

root=tkinter.Tk()
root.resizable(False,False)
root.configure(bg='black')
root.geometry("1000x650")

frame=tkinter.Frame(master=root,bg='black',width=1000,height=40,bd=2)
frame.pack(side='top')

color='white'
size=1

def getcolor():
    global color
    color=askcolor()
    color=color[1]

def back():
    global c
    c=askcolor()
    frame.configure(bg=c[1])
    canvas.configure(bg=c[1])

def plus():
    global size
    size=size+1

def minus():
    global size
    if size==1:
        size=1
    else:
        size=size-1
        
def erase(event):
    global color
    global size
    global c
    color=c
    x,y=event.x,event.y
    if canva.old_coords:
        x1,y1=canvas.old_coords
        canvas.create_line(x,y,x1,y1,fill=color,width=size)
    canvas.old_coords=x,y

button1=tkinter.Button(master=frame,text='pen color',padx=20,command=getcolor)
button1.place(x=10,y=8)

button2=tkinter.Button(master=frame,text='background',padx=20,command=back)
button2.place(x=200,y=8)

button3=tkinter.Button(master=frame,text='   erase  ',padx=20,command=erase)
button3.place(x=400,y=8)

button4=tkinter.Button(master=frame,text='pen size +',padx=20,command=plus)
button4.place(x=800,y=8)

button5=tkinter.Button(master=frame,text='pen size -',padx=20,command=minus)
button5.place(x=900,y=8)

def motion(event):
    x,y=event.x,event.y
    if canvas.old_coords:
        x1,y1=canvas.old_coords
        canvas.create_line(x,y,x1,y1,fill=color,width=size)
    canvas.old_coords=x,y
    
def release(event):
    canvas.old_coords=None
canvas=tkinter.Canvas(master=root,width=1000,height=650,bg='black')
canvas.pack()
canvas.old_coords=None
canvas.bind('<B1-Motion>',motion)
canvas.bind('<ButtonRelease-1>',release)
canvas.bind('<B2-Motion>',erase)

root.mainloop()
