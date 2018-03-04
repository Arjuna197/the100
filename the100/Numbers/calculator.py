import tkinter as tk
from math import *
class Application(tk.Frame):
    root = tk.Tk()
    root.title('Calculator')
    root.columnconfigure(0,uniform='a')
    expression= tk.Entry(root)
    expression.grid(row=6, columnspan=4)
    res=tk.Label(root, text='Result:', height=2)
    res.grid(row=0, column=0, columnspan=4, sticky='W')
    buttons={}
    def __init__(self, master=None):
        super().__init__(master)
        #self.create_widgets()
        self.expression.bind('<Return>', self.evaluate)
        self.buttons['1']=tk.Button(master, text='1', command= lambda:self.pushedNum(1))
        self.buttons['2']=tk.Button(master, text='2', command= lambda:self.pushedNum(2))
        self.buttons['3']=tk.Button(master, text='3', command= lambda:self.pushedNum(3))
        self.buttons['4']=tk.Button(master, text='4', command= lambda:self.pushedNum(4))
        self.buttons['5']=tk.Button(master, text='5', command= lambda:self.pushedNum(5))
        self.buttons['6']=tk.Button(master, text='6', command= lambda:self.pushedNum(6))
        self.buttons['7']=tk.Button(master, text='7', command= lambda:self.pushedNum(7))
        self.buttons['8']=tk.Button(master, text='8', command= lambda:self.pushedNum(8))
        self.buttons['9']=tk.Button(master, text='9', command= lambda:self.pushedNum(9))
        self.buttons['+']=tk.Button(master, text='+', command= lambda:self.pushedNum('+'))
        self.buttons['-']=tk.Button(master, text='-', command= lambda:self.pushedNum('-'))
        self.buttons['*']=tk.Button(master, text='*', command= lambda:self.pushedNum('*'))
        self.buttons['/']=tk.Button(master, text='/', command= lambda:self.pushedNum('/'))
        self.buttons['^x']=tk.Button(master, text='^x', command= lambda:self.pushedNum('**'))
        self.buttons['CE']=tk.Button(master, text='CE', command= lambda:self.pushedNum('CE'))
        self.buttons['<[X]']=tk.Button(master, text='<[X]', command= self.backsp)
        self.buttons['=']=tk.Button(master, text='=', command= self.evaluate)
        self.buttons['.']=tk.Button(master, text='.', command= lambda:self.pushedNum('.'))
        self.buttons['0']=tk.Button(master, text='0', command= lambda:self.pushedNum(0))
        self.buttons['1'].grid(row=4 ,column=0 )
        self.buttons['2'].grid(row=4 ,column=1 )
        self.buttons['3'].grid(row=4 ,column=2 )
        self.buttons['4'].grid(row=3 ,column=0 )
        self.buttons['5'].grid(row=3 ,column=1 )
        self.buttons['6'].grid(row=3 ,column=2 )
        self.buttons['7'].grid(row=2 ,column=0 )
        self.buttons['8'].grid(row=2 ,column=1 )
        self.buttons['9'].grid(row=2 ,column=2 )
        self.buttons['+'].grid(row=5 ,column=3 )
        self.buttons['-'].grid(row=4 ,column=3 )
        self.buttons['*'].grid(row=3, column=3)
        self.buttons['/'].grid(row=2, column=3)
        self.buttons['^x'].grid(row=1, column=0)
        self.buttons['CE'].grid(row=5, column=0)
        self.buttons['<[X]'].grid(row=1, column=1)
        self.buttons['='].grid(row=5, column=2)
        self.buttons['.'].grid(row=1, column=3)
        self.buttons['0'].grid(row=5, column=1)
        #for y in range(8):
            ##self.root.columnconfigure(index=y, minsize=145)
            #self.root.rowconfigure(index=y, minsize=145)
        for x in self.buttons.values():
            #x.grid(padx=1, pady=1, ipadx=20, ipady=10, sticky='NWES')
            x.config(fg='red', font=('times', 10, 'bold'),height=2, width=4)
    def backsp(self):
        self.expression.delete(len(self.expression.get())-1)
    def evaluate(self, event):
        self.res.configure(text=('Result:'+str(eval(self.expression.get()))))
    def evaluate(self):
        self.res.configure(text=('Result:'+str(eval(self.expression.get()))))
    def pushedNum(self, num):
        self.length= len(str(self.expression.get()))
        self.expression.insert(self.length, str(num))

app = Application()
app.mainloop()
