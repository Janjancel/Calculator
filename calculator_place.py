
import tkinter as tk


r = tk.Tk()
r.geometry('350x600')
r.config(bg='DarkKhaki')

def Allclear():
    num.delete(0, tk.END)
  
def clear():
    huli = len(num.get())
    num.delete(huli-1, tk.END)

def add():
    
    first = num.get()
    global first_num
    global math
    math = "addition"
    first_num = eval(first)
    num.delete(0, tk.END)

def substraction():
    first = num.get()
    global first_num
    global math
    math = "substraction"
    first_num = eval(first)
    num.delete(0, tk.END)

def multiplication():
    first = num.get()
    global first_num
    global math
    math = "multiplication"
    first_num = eval(first)
    num.delete(0, tk.END)

def division():
    first = num.get()
    global first_num
    global math
    math = "division"
    first_num = eval(first)
    num.delete(0, tk.END)

def percent():
    first = num.get()
    global first_num
    global math
    math = "percent"
    first_num = eval(first)
    num.delete(0, tk.END)

def equals():
    
    second = num.get() 
    num.delete(0, tk.END) 
    try:
        if math == "addition":
            num.insert(0, first_num + eval(second))
            
        elif math == "substraction":
            num.insert(0, first_num - eval(second))
        
        elif math == "multiplication":
            num.insert(0, first_num * eval(second))
        
        elif math == "division":
            num.insert(0, first_num / eval(second))
        
        elif math == "percent":
            num.insert(0, first_num % eval(second))
    except ValueError:
        num.insert(0, 'invalid')



def show(number):   
        current = num.get()
        num.delete(0, tk.END)
        num.insert(0,  str(current) + str(number))
    



num = tk.Entry(r, width=14, font=('Arial Black',25), borderwidth=7, bg='silver', justify='right')
num.place(x=13, y=30)

#row1
btnC = tk.Button(r, width=8, height=4, text="C", font=('Arial Black',10), bg='PaleGoldenrod' , command=clear)
btnC.place(x=12, y=115)

btnDiv = tk.Button(r, width=8, height=4, text="÷", font=('Arial Black',10), bg='PaleGoldenrod', command=division )
btnDiv.place(x=93, y=115)

btnMul = tk.Button(r, width=8, height=4, text="X", font=('Arial Black',10), bg='PaleGoldenrod', command=multiplication  )
btnMul.place(x=174, y=115)

btnAC = tk.Button(r, width=8, height=4, text="AC", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:Allclear()  )
btnAC.place(x=255, y=115)



#row2
btn7 = tk.Button(r, width=8, height=4, text="7", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:show(7))
btn7.place(x=12, y=205)

btn8 = tk.Button(r, width=8, height=4, text="8", font=('Arial Black',10), bg='PaleGoldenrod' , command=lambda:show(8) )
btn8.place(x=93, y=205)

btn9 = tk.Button(r, width=8, height=4, text="9", font=('Arial Black',10), bg='PaleGoldenrod' , command=lambda:show(9) )
btn9.place(x=174, y=205)

btnMin = tk.Button(r, width=8, height=4, text="-", font=('Arial Black',10), bg='PaleGoldenrod', command=substraction  )
btnMin.place(x=255, y=205)



#row3
btn4 = tk.Button(r, width=8, height=4, text="4", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:show(4)  )
btn4.place(x=12, y=295)

btn5 = tk.Button(r, width=8, height=4, text="5", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:show(5)  )
btn5.place(x=93, y=295)

btn6 = tk.Button(r, width=8, height=4, text="6", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:show(6)  )
btn6.place(x=174, y=295)

btnPlus = tk.Button(r, width=8, height=4, text="+", font=('Arial Black',10), bg='PaleGoldenrod', command=add  )
btnPlus.place(x=255, y=295)



#row4
btn1 = tk.Button(r, width=8, height=4, text="1", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:show(1)  )
btn1.place(x=12, y=385)

btn2 = tk.Button(r, width=8, height=4, text="2", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:show(2)  )
btn2.place(x=93, y=385)

btn3 = tk.Button(r, width=8, height=4, text="3", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:show(3)  )
btn3.place(x=174, y=385)

btnE = tk.Button(r, width=8, height=9, text="=", font=('Arial Black',10),fg='white' ,bg='DarkSlateGray' , command=equals )
btnE.place(x=255, y=385)


#row5
btnPer = tk.Button(r, width=8, height=4, text="%", font=('Arial Black',10), bg='PaleGoldenrod', command=percent  )
btnPer.place(x=12, y=475)

btn0 = tk.Button(r, width=8, height=4, text="0", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:show(0)  )
btn0.place(x=93, y=475)

btnTuldok = tk.Button(r, width=8, height=4, text=".", font=('Arial Black',10), bg='PaleGoldenrod', command=lambda:show('.')  )
btnTuldok.place(x=174, y=475)


r.mainloop()
