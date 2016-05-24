# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:36:16 2016

@author: usuario
"""

import random
import numpy as np
import statistics as st
from tkinter import *


maletas = [.5, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,1000, 5000, 10000, 25000, 50000, 75000,100000, 200000,300000, 400000, 500000, 750000, 1000000]

checklist = [] 

escolha = []


def main():
	escolhido = input("Escolha a maleta (1,26): ")

	if int(escolhido) > 26 or int(escolhido) < 1:
		print ("Maleta não existente")
		main()
		
	else:
         
		
            Malas = random.choice(maletas)
            maletas.remove(Malas)
            escolha.append(Malas)
            checklist.append(escolhido)	
            Remove(escolhido,checklist)
            
  


def Banqueiro(escolhido,checklist):
    
        media = sum(maletas)/float(len(maletas))

        desvio = st.stdev(maletas)
        
        desvio2 = (desvio/float(len(maletas)))*0.1
        
        normal1 = (np.random.normal(media, desvio2, 1))
        			
        oferta = normal1
        
        print(media)
        print(oferta)        
        
        if len(maletas) > 1:	
			
        		
                print ("O Banqueiro ofereceu","R$","%.2f"%oferta, "Voce aceita (S)im ou (N)ao" )
                decisao = input("Ma Oe?: ")
        		
                if decisao == "S" or decisao == "s":
                    print ("Voce ganhou","R$","%.2f"%oferta)
                			
                    print ("Sua maleta tinha","R$",escolha)
           
                elif decisao == "N" or decisao == "n":
                    del turnos[0] 
                    Remove(escolhido,checklist)
        				
                else:
                    print ("Opcao invalida")
                    Banqueiro(escolhido,checklist)
           
def Banqueiro2(escolhido,checklist):
    
        media = sum(maletas)/float(len(maletas))
        
        print(media)        
        
        if len(maletas) == 1:
            Fim(media, escolha, escolhido)
             

def Fim(oferta, escolha, escolhido):
    
    final = input("Voce quer manter sua maleta final?  (S)im ou (N)ão: ")
    
    if final == "s" or final == "S":
            print ("Voce ganhou","R$",escolha)
            print ("FIM DE JOGO")
			
    elif final == "N" or final == "n":
           print ("Voce ganhou","R$","%.2f"%oferta)
           main()
			
    else:
       print ("Opcão invalida")
       Banqueiro(escolhido,checklist)    


turnos = [6,3,6,3,3,2,1]  
def Remove(escolhido,checklist):
    
    for i in turnos:
    
        turn = i
        while turn != 0:
        
                print(escolhido) 
                print(checklist)
                print(maletas)
    
                removemaletas = input("Escolha uma maleta para ser removida (1,26): ")
                  
    		
                while int(removemaletas) > 26 or int(removemaletas) < 1:
                    print ("Maleta não existente")
                    removemaletas = input("Escolha uma maleta para ser removida (1,26): ")
                
                if removemaletas in checklist:
                    print ("Essa maleta já foi escolhida")
    			
                else:
    			 
                        Malas = random.choice(maletas)
                        maletas.remove(Malas)
                        checklist.append(removemaletas)
                        print(Malas)
                        
                        
                        turn = turn - 1
        
        if len(maletas) == 1:
          
            Banqueiro2(escolhido,checklist)
        Banqueiro(escolhido,checklist)             



class Tabuleiro:
    
    
    def __init__(self):
        self.janela = Tk()
        self.janela["bg"]="black"
        self.janela.geometry("600x800+200+200")
        self.janela.title("interface")
        self.interface()
        
        

    def bt_onclick(self):
        
        maletas2 = [self.lb28,lb29,lb30,lb31,lb32,lb33,lb34,lb35,lb36,lb37,lb38,lb39,lb40,lb41,lb42,lb43,lb44,lb45,lb46,lb47,lb48,lb49,lb50,lb51,lb52,lb53]

        
        self.l1 = random.choice(maletas2)
        
       


    def interface(self):
        
    ## Entry de dados
        self.lb27= Label(self.janela,width = 25,fg="black",bg="gold",text= "Digite a Maleta:")
        self.lb27.place(x= 300, y = 390)
        self.ed= Entry(self.janela,width = 25,fg="black",bg="gold")
        self.ed.place(x= 300, y =420 )
        self.bt27 = Button(self.janela,width= 25, text = "OK",fg="black", command = lambda: Tabuleiro.bt_onclick(self.ed) )
        self.bt27.place(x= 300, y =450)


    ## Maletas
        self.lb1= Label(self.janela,width = 15, text = "Maleta 1",bg= "black",fg= "gold")
        self.lb1.place(x = 300, y =0)

        self.lb2= Label(self.janela,width = 15, text = "Maleta 2" ,bg= "black",fg= "gold")
        self.lb2.place(x = 300, y =30)

        self.lb3= Label(self.janela,width = 15, text = "Maleta 3" ,bg= "black",fg= "gold")
        self.lb3.place(x = 300, y =60)

        self.lb4= Label(self.janela,width = 15, text = "Maleta 4" ,bg= "black",fg= "gold")
        self.lb4.place(x = 300, y =90)

        self.lb5= Label(self.janela,width = 15, text = "Maleta 5" ,bg= "black",fg= "gold")
        self.lb5.place(x = 300, y =120)

        self.lb6= Label(self.janela,width = 15, text = "Maleta 6" ,bg= "black",fg= "gold")
        self.lb6.place(x = 300, y =150)

        self.lb7= Label(self.janela,width = 15, text = "Maleta 7" ,bg= "black",fg= "gold")
        self.lb7.place(x = 300, y =180)

        self.lb8= Label(self.janela,width = 15, text = "Maleta 8" ,bg= "black",fg= "gold")
        self.lb8.place(x = 300, y =210)

        self.lb9= Label(self.janela,width = 15, text = "Maleta 9" ,bg= "black",fg= "gold")
        self.lb9.place(x = 300, y =240)

        self.lb10= Label(self.janela,width = 15, text = "Maleta 10" ,bg= "black",fg= "gold")
        self.lb10.place(x = 300, y =270)

        self.lb11= Label(self.janela,width = 15, text = "Maleta 11" ,bg= "black",fg= "gold")
        self.lb11.place(x = 300, y =300)

        self.lb12= Label(self.janela,width = 15, text = "Maleta 12" ,bg= "black",fg= "gold")
        self.lb12.place(x = 300, y =330)

        self.lb13= Label(self.janela,width = 15, text = "Maleta 13" ,bg= "black",fg= "gold")
        self.lb13.place(x = 300, y =360)

        self.lb14= Label(self.janela,width = 15, text = "Maleta 14" ,bg= "black",fg= "gold")
        self.lb14.place(x = 450, y =0)

        self.lb15= Label(self.janela,width = 15, text = "Maleta 15" ,bg= "black",fg= "gold")
        self.lb15.place(x = 450, y =30)

        self.lb16= Label(self.janela,width = 15, text = "Maleta 16" ,bg= "black",fg= "gold")
        self.lb16.place(x = 450, y =60)

        self.lb17= Label(self.janela,width = 15, text = "Maleta 17" ,bg= "black",fg= "gold")
        self.lb17.place(x = 450, y =90)

        self.lb18= Label(self.janela,width = 15, text = "Maleta 18" ,bg= "black",fg= "gold")
        self.lb18.place(x = 450, y =120)

        self.lb19= Label(self.janela,width = 15, text = "Maleta 19" ,bg= "black",fg= "gold")
        self.lb19.place(x = 450, y =150)

        self.lb20= Label(self.janela,width = 15, text = "Maleta 20" ,bg= "black",fg= "gold")
        self.lb20.place(x = 450, y =180)

        self.lb21= Label(self.janela,width = 15, text = "Maleta 21" ,bg= "black",fg= "gold")
        self.lb21.place(x = 450, y =210)

        self.lb22= Label(self.janela,width = 15, text = "Maleta 22" ,bg= "black",fg= "gold")
        self.lb22.place(x = 450, y =240)

        self.lb23= Label(self.janela,width = 15, text = "Maleta 23" ,bg= "black",fg= "gold")
        self.lb23.place(x = 450, y =270)

        self.lb24= Label(self.janela,width = 15, text = "Maleta 24" ,bg= "black",fg= "gold")
        self.lb24.place(x = 450, y =300)

        self.lb25= Label(self.janela,width = 15, text = "Maleta 25" ,bg= "black",fg= "gold")
        self.lb25.place(x = 450, y =330)

        self.lb26= Label(self.janela,width = 15, text = "Maleta 26" ,bg= "black",fg= "gold")
        self.lb26.place(x = 450, y =360)



    ## Valores
        self.lb28= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 0.5")
        self.lb28.place(x = 1, y =0)

        self.lb29= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 1")
        self.lb29.place(x = 1, y =30)

        self.lb30= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 5")
        self.lb30.place(x = 1, y =60)

        self.lb31= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 10")
        self.lb31.place(x = 1, y =90)

        self.lb32= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 25")
        self.lb32.place(x = 1, y =120)

        self.lb33= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 50")
        self.lb33.place(x = 1, y =150)

        self.lb34= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 75")
        self.lb34.place(x = 1, y =180)

        self.lb35= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 100")
        self.lb35.place(x = 1, y =210)

        self.lb36= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 200")
        self.lb36.place(x = 1, y =240)

        self.lb37= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 300")
        self.lb37.place(x = 1, y =270)

        self.lb38= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 400")
        self.lb38.place(x = 1, y =300)

        self.lb39= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 500")
        self.lb39.place(x = 1, y =330)

        self.lb40= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 750")
        self.lb40.place(x = 1, y =360)

        self.lb41= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 1.000")
        self.lb41.place(x = 150, y =0)

        self.lb42= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 5.000")
        self.lb42.place(x = 150, y =30)

        self.lb43= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 10.000")
        self.lb43.place(x = 150, y =60)

        self.lb44= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 25.000")
        self.lb44.place(x = 150, y =90)

        self.lb45= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 50.000")
        self.lb45.place(x = 150, y =120)

        self.lb46= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 75.000")
        self.lb46.place(x = 150, y =150)

        self.lb47= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 100.000")
        self.lb47.place(x = 150, y =180)

        self.lb48= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 200.000")
        self.lb48.place(x = 150, y =210)

        self.lb49= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 300.000")
        self.lb49.place(x = 150, y =240)

        self.lb50= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 400.000")
        self.lb50.place(x = 150, y =270)

        self.lb51= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 500.000")
        self.lb51.place(x = 150, y =300)

        self.lb52= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 750.000")
        self.lb52.place(x = 150, y =330)

        self.lb53= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 1.000.000")
        self.lb53.place(x = 150, y =360)



    def iniciar(self):
        self.janela.mainloop()
    
interface= Tabuleiro()
interface.iniciar()
main()
