from tkinter import *
janela1 = Tk()
janela1["bg"] = "gold"

## labels de valores

lb1= Label(janela1,width = 15, text = "R$ 0.01")
lb1.place(x = 1, y =0)

lb2= Label(janela1,width = 15, text = "R$ 1")
lb2.place(x = 1, y =30)

lb3= Label(janela1,width = 15, text = "R$ 5")
lb3.place(x = 1, y =60)

lb4= Label(janela1,width = 15, text = "R$ 10")
lb4.place(x = 1, y =90)

lb5= Label(janela1,width = 15, text = "R$ 25")
lb5.place(x = 1, y =120)

lb6= Label(janela1,width = 15, text = "R$ 50")
lb6.place(x = 1, y =150)

lb7= Label(janela1,width = 15, text = "R$ 75")
lb7.place(x = 1, y =180)

lb8= Label(janela1,width = 15, text = "R$ 100")
lb8.place(x = 1, y =210)

lb9= Label(janela1,width = 15, text = "R$ 200")
lb9.place(x = 1, y =240)

lb10= Label(janela1,width = 15, text = "R$ 300")
lb10.place(x = 1, y =270)

lb11= Label(janela1,width = 15, text = "R$ 400")
lb11.place(x = 1, y =300)

lb12= Label(janela1,width = 15, text = "R$ 500")
lb12.place(x = 1, y =330)

lb13= Label(janela1,width = 15, text = "R$ 750")
lb13.place(x = 1, y =360)

lb14= Label(janela1,width = 15, text = "R$ 1.000")
lb14.place(x = 150, y =0)

lb15= Label(janela1,width = 15, text = "R$ 5.000")
lb15.place(x = 150, y =30)

lb16= Label(janela1,width = 15, text = "R$ 10.000")
lb16.place(x = 150, y =60)

lb17= Label(janela1,width = 15, text = "R$ 25.000")
lb17.place(x = 150, y =90)

lb18= Label(janela1,width = 15, text = "R$ 50.000")
lb18.place(x = 150, y =120)

lb19= Label(janela1,width = 15, text = "R$ 75.000")
lb19.place(x = 150, y =150)

lb20= Label(janela1,width = 15, text = "R$ 100.000")
lb20.place(x = 150, y =180)

lb21= Label(janela1,width = 15, text = "R$ 200.000")
lb21.place(x = 150, y =210)

lb22= Label(janela1,width = 15, text = "R$ 300.000")
lb22.place(x = 150, y =240)

lb23= Label(janela1,width = 15, text = "R$ 400.000")
lb23.place(x = 150, y =270)

lb24= Label(janela1,width = 15, text = "R$ 500.000")
lb24.place(x = 150, y =300)

lb25= Label(janela1,width = 15, text = "R$ 750.000")
lb25.place(x = 150, y =330)

lb26= Label(janela1,width = 15, text = "R$ 1.000.000")
lb26.place(x = 150, y =360)

lb= Label(janela1,width = 25, text = "Valores das maletas")
lb.place(x = 40, y = 400 )

janela1.geometry("300x450+200+200")
janela1.title("Valores")

janela1.mainloop()