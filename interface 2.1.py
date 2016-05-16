"""Projeto final da materia de Design de Software. 
    Jogo de Topa ou nao topa, desenvolvido em python e utilizando a
    ferramenta Tkinter
    Faremos:
    as maletas no tkinter
    proposta do banqueiro
    gif de "resposta" das maletas. 
    """

from tkinter import *
from PIL import Image,ImageTk


def bt_onclick():
    
    image=Image.open("maleta.gif")
    photo=ImageTk.PhotoImage(image)
    lb28=Label(image=photo)
    lb28.image=photo
    lb28.pack()
#    maleta_img = Image.open("maleta.jpg")
#    photo = ImageTk.PhotoImage(maleta_img)
#    lb28=Label(maleta_img=photo)
#    lb28.image= photo
#    lb28.show()
    

    print(ed.get())



janela = Tk()
janela["bg"]="black"

## Entry de dados
lb27= Label(janela,width = 25,fg="black",bg="gold",text= "Digite o No da maleta a ser retirada")
lb27.place(x= 300, y = 390)
ed= Entry(janela,width = 25,fg="black",bg="gold")
ed.place(x= 300, y =420 )
bt27 = Button(janela,width= 25, text = "OK",fg="black", command = bt_onclick )
bt27.place(x= 300, y =450)


## Maletas
lb1= Label(janela,width = 15, text = "Maleta 1",bg= "black",fg= "gold")
lb1.place(x = 300, y =0)

lb2= Label(janela,width = 15, text = "Maleta 2" ,bg= "black",fg= "gold")
lb2.place(x = 300, y =30)

lb3= Label(janela,width = 15, text = "Maleta 3" ,bg= "black",fg= "gold")
lb3.place(x = 300, y =60)

lb4= Label(janela,width = 15, text = "Maleta 4" ,bg= "black",fg= "gold")
lb4.place(x = 300, y =90)

lb5= Label(janela,width = 15, text = "Maleta 5" ,bg= "black",fg= "gold")
lb5.place(x = 300, y =120)

lb6= Label(janela,width = 15, text = "Maleta 6" ,bg= "black",fg= "gold")
lb6.place(x = 300, y =150)

lb7= Label(janela,width = 15, text = "Maleta 7" ,bg= "black",fg= "gold")
lb7.place(x = 300, y =180)

lb8= Label(janela,width = 15, text = "Maleta 8" ,bg= "black",fg= "gold")
lb8.place(x = 300, y =210)

lb9= Label(janela,width = 15, text = "Maleta 9" ,bg= "black",fg= "gold")
lb9.place(x = 300, y =240)

lb10= Label(janela,width = 15, text = "Maleta 10" ,bg= "black",fg= "gold")
lb10.place(x = 300, y =270)

lb11= Label(janela,width = 15, text = "Maleta 11" ,bg= "black",fg= "gold")
lb11.place(x = 300, y =300)

lb12= Label(janela,width = 15, text = "Maleta 12" ,bg= "black",fg= "gold")
lb12.place(x = 300, y =330)

lb13= Label(janela,width = 15, text = "Maleta 13" ,bg= "black",fg= "gold")
lb13.place(x = 300, y =360)

lb14= Label(janela,width = 15, text = "Maleta 14" ,bg= "black",fg= "gold")
lb14.place(x = 450, y =0)

lb15= Label(janela,width = 15, text = "Maleta 15" ,bg= "black",fg= "gold")
lb15.place(x = 450, y =30)

lb16= Label(janela,width = 15, text = "Maleta 16" ,bg= "black",fg= "gold")
lb16.place(x = 450, y =60)

lb17= Label(janela,width = 15, text = "Maleta 17" ,bg= "black",fg= "gold")
lb17.place(x = 450, y =90)

lb18= Label(janela,width = 15, text = "Maleta 18" ,bg= "black",fg= "gold")
lb18.place(x = 450, y =120)

lb19= Label(janela,width = 15, text = "Maleta 19" ,bg= "black",fg= "gold")
lb19.place(x = 450, y =150)

lb20= Label(janela,width = 15, text = "Maleta 20" ,bg= "black",fg= "gold")
lb20.place(x = 450, y =180)

lb21= Label(janela,width = 15, text = "Maleta 21" ,bg= "black",fg= "gold")
lb21.place(x = 450, y =210)

lb22= Label(janela,width = 15, text = "Maleta 22" ,bg= "black",fg= "gold")
lb22.place(x = 450, y =240)

lb23= Label(janela,width = 15, text = "Maleta 23" ,bg= "black",fg= "gold")
lb23.place(x = 450, y =270)

lb24= Label(janela,width = 15, text = "Maleta 24" ,bg= "black",fg= "gold")
lb24.place(x = 450, y =300)

lb25= Label(janela,width = 15, text = "Maleta 25" ,bg= "black",fg= "gold")
lb25.place(x = 450, y =330)

lb26= Label(janela,width = 15, text = "Maleta 26" ,bg= "black",fg= "gold")
lb26.place(x = 450, y =360)



## Valores
lb28= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 0.5")
lb28.place(x = 1, y =0)

lb29= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 1")
lb29.place(x = 1, y =30)

lb30= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 5")
lb30.place(x = 1, y =60)

lb31= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 10")
lb31.place(x = 1, y =90)

lb32= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 25")
lb32.place(x = 1, y =120)

lb33= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 50")
lb33.place(x = 1, y =150)

lb34= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 75")
lb34.place(x = 1, y =180)

lb35= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 100")
lb35.place(x = 1, y =210)

lb36= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 200")
lb36.place(x = 1, y =240)

lb37= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 300")
lb37.place(x = 1, y =270)

lb38= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 400")
lb38.place(x = 1, y =300)

lb39= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 500")
lb39.place(x = 1, y =330)

lb40= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 750")
lb40.place(x = 1, y =360)

lb41= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 1.000")
lb41.place(x = 150, y =0)

lb42= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 5.000")
lb42.place(x = 150, y =30)

lb43= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 10.000")
lb43.place(x = 150, y =60)

lb44= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 25.000")
lb44.place(x = 150, y =90)

lb45= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 50.000")
lb45.place(x = 150, y =120)

lb46= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 75.000")
lb46.place(x = 150, y =150)

lb47= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 100.000")
lb47.place(x = 150, y =180)

lb48= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 200.000")
lb48.place(x = 150, y =210)

lb49= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 300.000")
lb49.place(x = 150, y =240)

lb50= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 400.000")
lb50.place(x = 150, y =270)

lb51= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 500.000")
lb51.place(x = 150, y =300)

lb52= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 750.000")
lb52.place(x = 150, y =330)

lb53= Label(janela,width = 15,fg="black",bg="gold", text = "R$ 1.000.000")
lb53.place(x = 150, y =360)



janela.geometry("600x800+200+200")
janela.title("interface")
janela.mainloop()

    

