from tkinter import *
import module1
def All_Button():
    button1=Button(window,text='1',font='Comic',width=8,height=2,command=clik_1)
    button2=Button(window,text='2',font='Comic',width=8,height=2,command=clik_2) 
    button3=Button(window,text='3',font='Comic',width=8,height=2,command=clik_3)
    button4=Button(window,text='4',font='Comic',width=8,height=2,command=clik_4)
    button5=Button(window,text='5',font='Comic',width=8,height=2,command=clik_5)
    button6=Button(window,text='6',font='Comic',width=8,height=2,command=clik_6)
    button7=Button(window,text='7',font='Comic',width=8,height=2,command=clik_7)
    button8=Button(window,text='8',font='Comic',width=8,height=2,command=clik_8)
    button9=Button(window,text='9',font='Comic',width=8,height=2,command=clik_9)
    button0=Button(window,text='0',font='Comic',width=8,height=2,command=clik_0)
    button_point=Button(window,text='.',font='Comic',width=8,height=2,command=clik_point)
    button_plus_or_minus=Button(window,text='+/-',font='Comic',width=8,height=2,command=clik_plus_or_minus)
    button_plus=Button(window,text='+',font='Comic',width=8,height=2,command=clik_plus)
    button_minus=Button(window,text='-',font='Comic',width=8,height=2,command=clik_minus)
    button_multiplication=Button(window,text='*',font='Comic',width=8,height=2,command=clik_multiplication)
    button_division=Button(window,text='/',font='Comic',width=8,height=2,command=clik_division)
    button_degree=Button(window,text='^',font='Comic',width=8,height=2,command=clik_degree)
    button_equally=Button(window,text='C',font='Comic',width=8,height=2,command=clik_equally)
    button_staples=Button(window,text='CE',font='Comic',width=8,height=2,command=clik_staples)
    button=Button(text='=', bg='black',fg='white',command=clik,width=8,height=2,font=14)
    button.grid(column=3,row=7)
    button1.grid(column=0,row=6)
    button2.grid(column=1,row=6)
    button3.grid(column=2,row=6)
    button4.grid(column=0,row=5)
    button5.grid(column=1,row=5)
    button6.grid(column=2,row=5)
    button7.grid(column=0,row=4)
    button8.grid(column=1,row=4)
    button9.grid(column=2,row=4)
    button0.grid(column=1,row=7)
    button_point.grid(column=2,row=7)
    button_plus_or_minus.grid(column=0,row=7)
    button_plus.grid(column=3,row=6)
    button_minus.grid(column=3,row=5)
    button_multiplication.grid(column=3,row=4)
    button_division.grid(column=3,row=3)
    button_degree.grid(column=2,row=3)
    button_equally.grid(column=0,row=3)
    button_staples.grid(column=1,row=3)
def clik_1():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'1')
def clik_2():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'2')
def clik_3():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'3')
def clik_4():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'4')
def clik_5():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'5')
def clik_6():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'6')
def clik_7():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'7')
def clik_8():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'8')
def clik_9():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'9')
def clik_0():
    txt=entry.get()
    if len(txt)==1 and txt[0]=='0':
        pass
    else:
        entry.insert(END,'0')
def clik_point():
    entry.insert(END,'.')
def clik_plus_or_minus():
    txt=entry.get()
    if len(txt)>0:
        if txt[0]in('1','2','3','4','5','6','7','8','9','0'):
            entry.insert(0,'-')
        else:
            entry.delete(0)
def clik_plus():
    txt=entry.get()
    if len(txt)>=2:
        if txt[-2]in('+','-','*','/','^'):
            pass
        else: entry.insert(END,' + ')
    elif len(txt)==1 and txt[0]not in('+','-','*','/','^'):
        entry.insert(END,' + ')
def clik_minus():
    txt=entry.get()
    if len(txt)>=2:
        if txt[-2]in('+','-','*','/','^'):
            pass
        else: entry.insert(END,' - ')
    elif len(txt)==1 and txt[0]not in('+','-','*','/','^'):
        entry.insert(END,' + ')
def clik_multiplication():
    txt=entry.get()
    if len(txt)>=2:
        if txt[-2]in('+','-','*','/','^'):
            pass
        else: entry.insert(END,' * ')
    elif len(txt)==1 and txt[0]not in('+','-','*','/','^'):
        entry.insert(END,' * ')
def clik_division():
    txt=entry.get()
    if len(txt)>=2:
        if txt[-2]in('+','-','*','/','^'):
            pass
        else: entry.insert(END,' / ')
    elif len(txt)==1 and txt[0]not in('+','-','*','/','^'):
        entry.insert(END,' / ')
def clik_degree():
    txt=entry.get()
    if len(txt)>=2:
        if txt[-2]in('+','-','*','/','^'):
            pass
        else: entry.insert(END,' ^ ')
    elif len(txt)==1 and txt[0]not in('+','-','*','/','^'):
        entry.insert(END,' ^ ')
def clik_equally():
    entry.delete(0,END)
def clik_staples():
    txt=entry.get()
    entry.delete(len(txt)-1)

def clik():
    txt=entry.get()
    a=[i for i in txt.strip().split()]
    print(a)
    lbl['text']= module1.Calculations(a)
window=Tk()
window.title('My Nigga')
window.geometry('390x350')
window.resizable(False,False)
entry=Entry(window,relief=GROOVE,width=20,selectforeground='black',selectbackground='aquamarine',font='arial 19')
entry.grid(column=0,row=0,columnspan=3)
entry.focus()
All_Button()
lbl=Label(text='Answer',fg='black')
lbl.grid(column=3,row=0)
window['bg']='black'
window.mainloop() 