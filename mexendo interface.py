__author__ = 'LuizJR'
from tkinter import *

#master = Tk()

#e = Entry(master)
#e.pack()

#e.focus_set()

#def callback():
#    print (e.get())

#b = Button(master, text="get", width=10, command=callback)
#b.pack()

#mainloop()
#e = Entry(master, width=50)
#e.pack()

#text = e.get()
#def makeentry(parent, caption, width=None, **options):
 #   Label(parent, text=caption).pack(side=LEFT)
#   entry = Entry(parent, **options)
#    if width:
#        entry.config(width=width)
#    entry.pack(side=LEFT)
#    return entry

#user = makeentry(parent, "User name:", 10)
#password = makeentry(parent, "Password:", 10, show="*")
#content = StringVar()
#entry = Entry(parent, text=caption, textvariable=content)

#text = content.get()
#content.set(text)

class Griding:
    def __init__(self,raiz):
        self.raiz = raiz
        self.raiz.title('Tchau!')
        Label(self.raiz,text='Nome:').grid(row=1, column=1,
        sticky=W, pady=3)
        Label(self.raiz,text='Senha:').grid(row=2, column=1,
        sticky=W, pady=3)
        self.msg=Label(self.raiz,text='Descubra a senha!')
        self.msg.grid(row=3, column=1, columnspan=2)
        self.nome=Entry(self.raiz, width=10)
        self.nome.grid(row=1, column=2, sticky=E+W, pady=3)
        self.nome.focus_force()
        self.senha=Entry(self.raiz, width=5, fg='darkgray',
        show='l',font=('Wingdings','10'))
        self.senha.grid(row=2,column=2, sticky=E+W, pady=3)
        self.ok=Button(self.raiz, width=8, command=self.testar,
        text='OK')
        self.ok.grid(row=4, column=1, padx=2, pady=3)
        self.close=Button(self.raiz, width=8, command=self.fechar,
        text='Fechar')
        self.close.grid(row=4, column=2, padx=2, pady=3)
    def testar(self):
        if self.nome.get()==self.senha.get()[::-1]:
            self.msg['text']='Senha correta!'
        else:
            self.msg['text']='Senha incorreta!'
    def fechar(self): self.raiz.destroy()
inst1=Tk()
Griding(inst1)
inst1.mainloop()
