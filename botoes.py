"""Projeto final da materia de Design de Software. 
    Jogo de Topa ou nao topa, desenvolvido em python e utilizando a
    ferramenta Tkinter
    Faremos:
    as maletas no tkinter
    proposta do banqueiro
    gif de "resposta" das maletas. 
    """

from tkinter import *
def bt_click():
    print("A maleta vale",  "reais")


janela = Tk()
janela["bg"] = "black"

## Botoes
bt1= Button(janela,width = 15, text = "Maleta 1",fg= "gold",command=bt_click)
bt1.place(x = 300, y =0)

bt2= Button(janela,width = 15, text = "Maleta 2" ,fg="gold",command=bt_click)
bt2.place(x = 300, y =30)

bt3= Button(janela,width = 15, text = "Maleta 3" ,fg="gold",command=bt_click)
bt3.place(x = 300, y =60)

bt4= Button(janela,width = 15, text = "Maleta 4" ,fg="gold",command=bt_click)
bt4.place(x = 300, y =90)

bt5= Button(janela,width = 15, text = "Maleta 5" ,fg="gold",command=bt_click)
bt5.place(x = 300, y =120)

bt6= Button(janela,width = 15, text = "Maleta 6" ,fg="gold",command=bt_click)
bt6.place(x = 300, y =150)

bt7= Button(janela,width = 15, text = "Maleta 7" ,fg="gold",command=bt_click)
bt7.place(x = 300, y =180)

bt8= Button(janela,width = 15, text = "Maleta 8" ,fg="gold",command=bt_click)
bt8.place(x = 300, y =210)

bt9= Button(janela,width = 15, text = "Maleta 9" ,fg="gold",command=bt_click)
bt9.place(x = 300, y =240)

bt10= Button(janela,width = 15, text = "Maleta 10" ,fg="gold",command=bt_click)
bt10.place(x = 300, y =270)

bt11= Button(janela,width = 15, text = "Maleta 11" ,fg="gold",command=bt_click)
bt11.place(x = 300, y =300)

bt12= Button(janela,width = 15, text = "Maleta 12" ,fg="gold",command=bt_click)
bt12.place(x = 300, y =330)

bt13= Button(janela,width = 15, text = "Maleta 13" ,fg="gold",command=bt_click)
bt13.place(x = 300, y =360)

bt14= Button(janela,width = 15, text = "Maleta 14" ,fg="gold",command=bt_click)
bt14.place(x = 450, y =0)

bt15= Button(janela,width = 15, text = "Maleta 15" ,fg="gold",command=bt_click)
bt15.place(x = 450, y =30)

bt16= Button(janela,width = 15, text = "Maleta 16" ,fg="gold",command=bt_click)
bt16.place(x = 450, y =60)

bt17= Button(janela,width = 15, text = "Maleta 17" ,fg="gold",command=bt_click)
bt17.place(x = 450, y =90)

bt18= Button(janela,width = 15, text = "Maleta 18" ,fg="gold",command=bt_click)
bt18.place(x = 450, y =120)

bt19= Button(janela,width = 15, text = "Maleta 19" ,fg="gold",command=bt_click)
bt19.place(x = 450, y =150)

bt20= Button(janela,width = 15, text = "Maleta 20" ,fg="gold",command=bt_click)
bt20.place(x = 450, y =180)

bt21= Button(janela,width = 15, text = "Maleta 21" ,fg="gold",command=bt_click)
bt21.place(x = 450, y =210)

bt22= Button(janela,width = 15, text = "Maleta 22" ,fg="gold",command=bt_click)
bt22.place(x = 450, y =240)

bt23= Button(janela,width = 15, text = "Maleta 23" ,fg="gold",command=bt_click)
bt23.place(x = 450, y =270)

bt24= Button(janela,width = 15, text = "Maleta 24" ,fg="gold",command=bt_click)
bt24.place(x = 450, y =300)

bt25= Button(janela,width = 15, text = "Maleta 25" ,fg="gold",command=bt_click)
bt25.place(x = 450, y =330)

bt26= Button(janela,width = 15, text = "Maleta 26" ,fg="gold",command=bt_click)
bt26.place(x = 450, y =360)

bt27 = Button(janela,width= 25, text = "Confirmar proposta do banqueiro",fg="red", command = bt_click )
bt27.place(x= 300, y =400)
## Valores
lb1= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 0.5")
lb1.place(x = 1, y =0)

lb2= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 1")
lb2.place(x = 1, y =30)

lb3= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 5")
lb3.place(x = 1, y =60)

lb4= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 10")
lb4.place(x = 1, y =90)

lb5= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 25")
lb5.place(x = 1, y =120)

lb6= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 50")
lb6.place(x = 1, y =150)

lb7= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 75")
lb7.place(x = 1, y =180)

lb8= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 100")
lb8.place(x = 1, y =210)

lb9= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 200")
lb9.place(x = 1, y =240)

lb10= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 300")
lb10.place(x = 1, y =270)

lb11= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 400")
lb11.place(x = 1, y =300)

lb12= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 500")
lb12.place(x = 1, y =330)

lb13= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 750")
lb13.place(x = 1, y =360)

lb14= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 1.000")
lb14.place(x = 150, y =0)

lb15= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 5.000")
lb15.place(x = 150, y =30)

lb16= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 10.000")
lb16.place(x = 150, y =60)

lb17= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 25.000")
lb17.place(x = 150, y =90)

lb18= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 50.000")
lb18.place(x = 150, y =120)

lb19= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 75.000")
lb19.place(x = 150, y =150)

lb20= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 100.000")
lb20.place(x = 150, y =180)

lb21= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 200.000")
lb21.place(x = 150, y =210)

lb22= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 300.000")
lb22.place(x = 150, y =240)

lb23= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 400.000")
lb23.place(x = 150, y =270)

lb24= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 500.000")
lb24.place(x = 150, y =300)

lb25= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 750.000")
lb25.place(x = 150, y =330)

lb26= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 1.000.000")
lb26.place(x = 150, y =360)



janela.geometry("600x800+200+200")
janela.title("Maletas")
janela.mainloop()

    

