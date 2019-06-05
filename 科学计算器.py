from tkinter import *
import tkinter.font as tkFont
import os
from functools import partial
from PIL import Image, ImageTk
import parser
import math
def get_input(entry, argu):
    entry.insert(END, argu) #输入
def backspace(entry):
    input_len = len(entry.get()) 
    entry.delete(input_len - 1)  #<-的函数
def clear(entry):
    entry.delete(0, END) #C的函数
def calc(entry):
    input = entry.get()
    output = str(eval(input.strip())) #=的函数
    clear(entry)
    entry.insert(END, output)
def factorial():
     whole_string = entry.get()
     number = int(whole_string)
     fact = 1
     counter = number
     try:
         while counter > 0:
             fact = fact*counter
             counter -= 1
         clear(entry)
         entry.insert(0, fact)
     except Exception:
         clear(entry)
         entry.insert(0, "Error")
def sqrt():
    whole_string=entry.get()
    number=float(whole_string)
    fact=math.sqrt(number)
    clear(entry)
    entry.insert(0,fact)
def sin():
    whole_string=entry.get()
    number=float(whole_string)
    fact=math.sin(number)
    clear(entry)
    entry.insert(0,fact)
def cos():
    whole_string=entry.get()
    number=float(whole_string)
    fact=math.cos(number)
    clear(entry)
    entry.insert(0,fact)
def tan():
    whole_string=entry.get()
    number=float(whole_string)
    fact=math.tan(number)
    clear(entry)
    entry.insert(0,fact)
def ln():
    whole_string=entry.get()
    number=float(whole_string)
    fact=math.log(number)
    clear(entry)
    entry.insert(0,fact)
root = Tk()
root.title("Standard calculate")
root.resizable(0,0)
entry_font = tkFont.Font(size=12)
entry = Entry(root, justify="right", font=entry_font)
entry.grid(row=0, column=0, columnspan=4, sticky=N+W+S+E, padx=5,  pady=5) #设置计算器上的输入框
button_font = tkFont.Font(size=10, weight=tkFont.BOLD)
button_bg = '#D5E0EE'
button_active_bg = '#E5E35B' #总的按钮属性
myButton = partial(Button, root, bg=button_bg, padx=10, pady=3, activebackground = button_active_bg)
button7 = myButton(text='7', command=lambda : get_input(entry, '7'))
button7.grid(row=1, column=0, pady=5)  #数字‘7’
button8 = myButton(text='8', command=lambda : get_input(entry, '8'))
button8.grid(row=1, column=1, pady=5)  #数字‘8’
button9 = myButton(text='9', command=lambda : get_input(entry, '9'))
button9.grid(row=1, column=2, pady=5)  #数字‘9’
button10 = myButton(text='+', command=lambda : get_input(entry, '+'))
button10.grid(row=1, column=3, pady=5) #‘+’
button4 = myButton(text='4', command=lambda : get_input(entry, '4'))
button4.grid(row=2, column=0, pady=5)  #数字‘4’
button5 = myButton(text='5', command=lambda : get_input(entry, '5'))
button5.grid(row=2, column=1, pady=5)  #数字‘5’
button6 = myButton(text='6', command=lambda : get_input(entry, '6'))
button6.grid(row=2, column=2, pady=5)  #数字‘6’
button11 = myButton(text='-', command=lambda : get_input(entry, '-'))
button11.grid(row=2, column=3, pady=5) #‘-’
button1 = myButton(text='1', command=lambda : get_input(entry, '1'))
button1.grid(row=3, column=0, pady=5)  #数字‘1’
button2 = myButton(text='2', command=lambda : get_input(entry, '2'))
button2.grid(row=3, column=1, pady=5)  #数字‘2’
button3 = myButton(text='3', command=lambda : get_input(entry, '3'))
button3.grid(row=3, column=2, pady=5)  #数字‘3’
button12 = myButton(text='*', command=lambda : get_input(entry, '*'))
button12.grid(row=3, column=3, pady=5) #‘*’
button0 = myButton(text='0', command=lambda : get_input(entry, '0'))
button0.grid(row=4, column=0,pady=5) #数字‘0’
button18=myButton(text='%',  command=lambda: get_input(entry,'%'))
button18.grid(row=4, column=1,pady=5) #‘%’
button13 = myButton(text='.', command=lambda : get_input(entry, '.'))
button13.grid(row=4, column=2, pady=5) #‘.’
button14 =Button(root, text='/', bg=button_bg, padx=10, pady=3,command=lambda : get_input(entry, '/'))
button14.grid(row=4, column=3, pady=5) #‘/’
button15 = Button(root, text='<-', bg=button_bg, padx=10, pady=3,command=lambda : backspace(entry), activebackground = button_active_bg)
button15.grid(row=5, column=0, pady=5) #‘<-’
button16 = Button(root, text='C', bg=button_bg, padx=10, pady=3,command=lambda : clear(entry), activebackground = button_active_bg)
button16.grid(row=5, column=1, pady=5) #‘C’
button17 = Button(root, text='=', bg=button_bg, padx=10, pady=3,command=lambda : calc(entry), activebackground = button_active_bg)
button17.grid(row=5, column=2 ,padx=3, pady=5) #‘=’
button24=myButton(text='sqrt',command=lambda:sqrt())
button24.grid(row=5, column=3,pady=5)  #开方
button18=myButton(text='n!',command=lambda : factorial()) 
button18.grid(row=6, column=0,pady=5)  #阶乘
button19= myButton(text= 'exp',command= lambda : get_input(entry,'**'))
button19.grid(row=6, column=1, pady=5) #指数
button20=myButton(text='^2', command=lambda :get_input(entry,'**2'))
button20.grid(row=6,column=2,pady=5)   #平方
button21=myButton(text='pi',command=lambda:get_input(entry,'3.14'))
button21.grid(row=6, column=3,pady=5)  #pi
button22=myButton(text='(',command=lambda:get_input(entry,'('))
button22.grid(row=7, column=0,columnspan=2,pady=5,sticky=N+S+E+W)
button23=myButton(text=')',command=lambda:get_input(entry,')'))
button23.grid(row=7, column=2,columnspan=2,pady=5,sticky=N+S+E+W) #括号
button25=myButton(text='sin',command=lambda:sin())
button25.grid(row=8, column=0,pady=5) #sin
button26=myButton(text='cos',command=lambda:cos())
button26.grid(row=8, column=1,pady=5) #cos
button27=myButton(text='tan',command=lambda:tan())
button27.grid(row=8, column=2,pady=5) #tan
button28=myButton(text='ln',command=lambda:ln())
button28.grid(row=8, column=3,pady=5) #ln
root.mainloop()
