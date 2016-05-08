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
    print("A maleta vale:")
    
#    lb["text"] = "Voce quer mesmo retirar essa maleta ?

janela = Tk()

bt1= Button(janela,width = 15, text = "Maleta 1" ,command=bt_click)
bt1.place(x = 1, y =0)

bt2= Button(janela,width = 15, text = "Maleta 2" ,command=bt_click)
bt2.place(x = 1, y =30)

bt3= Button(janela,width = 15, text = "Maleta 3" ,command=bt_click)
bt3.place(x = 1, y =60)

bt4= Button(janela,width = 15, text = "Maleta 4" ,command=bt_click)
bt4.place(x = 1, y =90)

bt5= Button(janela,width = 15, text = "Maleta 5" ,command=bt_click)
bt5.place(x = 1, y =120)

bt6= Button(janela,width = 15, text = "Maleta 6" ,command=bt_click)
bt6.place(x = 1, y =150)

bt7= Button(janela,width = 15, text = "Maleta 7" ,command=bt_click)
bt7.place(x = 1, y =180)

bt8= Button(janela,width = 15, text = "Maleta 8" ,command=bt_click)
bt8.place(x = 1, y =210)

bt9= Button(janela,width = 15, text = "Maleta 9" ,command=bt_click)
bt9.place(x = 1, y =240)

bt10= Button(janela,width = 15, text = "Maleta 10" ,command=bt_click)
bt10.place(x = 1, y =270)

bt11= Button(janela,width = 15, text = "Maleta 11" ,command=bt_click)
bt11.place(x = 1, y =300)

bt12= Button(janela,width = 15, text = "Maleta 12" ,command=bt_click)
bt12.place(x = 1, y =330)

bt13= Button(janela,width = 15, text = "Maleta 13" ,command=bt_click)
bt13.place(x = 1, y =360)

bt14= Button(janela,width = 15, text = "Maleta 14" ,command=bt_click)
bt14.place(x = 150, y =0)

bt15= Button(janela,width = 15, text = "Maleta 15" ,command=bt_click)
bt15.place(x = 150, y =30)

bt16= Button(janela,width = 15, text = "Maleta 16" ,command=bt_click)
bt16.place(x = 150, y =60)

bt17= Button(janela,width = 15, text = "Maleta 17" ,command=bt_click)
bt17.place(x = 150, y =90)

bt18= Button(janela,width = 15, text = "Maleta 18" ,command=bt_click)
bt18.place(x = 150, y =120)

bt19= Button(janela,width = 15, text = "Maleta 19" ,command=bt_click)
bt19.place(x = 150, y =150)

bt20= Button(janela,width = 15, text = "Maleta 20" ,command=bt_click)
bt20.place(x = 150, y =180)

bt21= Button(janela,width = 15, text = "Maleta 21" ,command=bt_click)
bt21.place(x = 150, y =210)

bt22= Button(janela,width = 15, text = "Maleta 22" ,command=bt_click)
bt22.place(x = 150, y =240)

bt23= Button(janela,width = 15, text = "Maleta 23" ,command=bt_click)
bt23.place(x = 150, y =270)

bt24= Button(janela,width = 15, text = "Maleta 24" ,command=bt_click)
bt24.place(x = 150, y =300)

bt25= Button(janela,width = 15, text = "Maleta 25" ,command=bt_click)
bt25.place(x = 150, y =330)

bt26= Button(janela,width = 15, text = "Maleta 26" ,command=bt_click)
bt26.place(x = 150, y =360)


janela.geometry("400x600+200+200")
janela.mainloop()

    
    

