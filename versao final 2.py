# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:21:50 2016

@author: brunoiampolsky
"""

import random
import numpy as np
import statistics as st
from tkinter import *


# Comentario - cria a lista de possiveis valores das maletas, e cria duas listas onde a primeira é responsável por checar as maletas que já foram escolhidas e a segunda a escolha do usuário(se ele mantém ou nao)
class Jogo:
    def __init__(self):
        self.maletas = [.5, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,1000, 5000, 10000, 25000, 50000, 75000,100000, 200000,300000, 400000, 500000, 750000, 1000000]
        
        self.checklist = []
        
        self.escolha = []
        
    #comentário - funcao main, checa se o usuario escolheu uma maleta dentro do range e caso esteja, randomiza as maletas e os valores e as maletas escolhidas sao adicionadas na lista checklist
    def main(self):
    	self.escolhido = input("Escolha a maleta (1,26): ")
    
    	if int(self.escolhido) > 26 or int(self.escolhido) < 1:
    		print ("Maleta não existente")
    		self.main()
    		
    	else:
             
    		
                self.Malas = random.choice(self.maletas)
                self.maletas.remove(self.Malas)
                self.escolha.append(self.Malas)
                self.checklist.append(self.escolhido)	
                self.Remove(self.escolhido,self.checklist)
                
  

    # Comentário - A funcao banqueiro é responsável por fazer a média dos valores das maletas ainda possiveis para escolha levando em conta desvio padrão e o tipode distribuicao
    def Banqueiro(self,escolhido,checklist):
        
            self.media = sum(self.maletas)/float(len(self.maletas))
    
            self.desvio = st.stdev(self.maletas)
            
            self.desvio2 = (self.desvio/float(len(self.maletas)))*0.1
            
            self.normal1 = (np.random.normal(self.media, self.desvio2, 1))
            			
            self.oferta = self.normal1
            
            print(self.media)
            print(self.oferta)        

            #Comentário - Nessa secçção o usuario decide se aceita a oferta calculada pelo banqueiro, se aceitar a oferta  o jogo termina e ele recebe o valor caso recuse, o jogo retorna ao normal onde o jogador continua eliminando as maletas
            if len(self.maletas) > 1:	
    			
            		
                    print ("O Banqueiro ofereceu","R$","%.2f"%self.oferta, "Voce aceita (S)im ou (N)ao" )
                    self.decisao = input("Ma Oe?: ")
            		
                    if self.decisao == "S" or self.decisao == "s":
                        print ("Voce ganhou","R$","%.2f"%self.oferta)
                    			
                        print ("Sua maleta tinha","R$",self.escolha)
               
                    elif self.decisao == "N" or self.decisao == "n":
                        del self.turnos[0] 
                        self.Remove(self.escolhido,self.checklist)
            				
                    else:
                        print ("Opcao invalida")
                        self.Banqueiro(self.escolhido,self.checklist)

    #Comentário - funcao que quando tiver apenas 1 maleta, faz a media dos valores restantes
    def Banqueiro2(self,escolhido,checklist):
        
            self.media = sum(self.maletas)/float(len(self.maletas))
            
            print(self.media)        
            
            if len(self.maletas) == 1:
                self.Fim(self.media, self.escolha, self.escolhido)
             
    #Comentario - Funcao checa o input do usuario, caso ele queria ficar com a maleta, o jogo termina, caso não ele terá a opcao de aceitar umaultima oferta do banqueiro e se recusar terá o valor da ultima maleta restante
    def Fim(self,oferta, escolha, escolhido):
        
        self.final = input("Voce quer manter sua maleta final?  (S)im ou (N)ão: ")
        
        if self.final == "s" or self.final == "S":
                print ("Voce ganhou","R$",self.escolha)
                print ("FIM DE JOGO")
    			
        elif self.final == "N" or self.final == "n":
               print ("Voce ganhou","R$","%.2f"%self.oferta)
               self.main()
    			
        else:
           print ("Opcão invalida")
           self.Banqueiro(self.escolhido,self.checklist)    

    #Comentário - funcao que remove as maletas dentro do range estabelecido
    turnos = [6,3,6,3,3,2,1]  
    def Remove(self,escolhido,checklist):
        
        for i in self.turnos:
        
            turn = i
            while turn != 0:
            
                    print(self.escolhido) 
                    print(self.checklist)
                    print(self.maletas)
        
                    self.removemaletas = input("Escolha uma maleta para ser removida (1,26): ")
                      
        		    #Comentário - Nessa secção,checa se as maletas escolhidas para serem removidas estao no range, checa se a maleta nao foi escolhida 2 vezes e a cada oferta do banqueiro, os turnos para a escolha de maletas vao diminuiundo,começando com 6 e terminando com 3
                    while int(self.removemaletas) > 26 or int(self.removemaletas) < 1:
                        print ("Maleta não existente")
                        self.removemaletas = input("Escolha uma maleta para ser removida (1,26): ")
                    
                    if self.removemaletas in self.checklist:
                        print ("Essa maleta já foi escolhida")
        			
                    else:
        			 
                            self.Malas = random.choice(self.maletas)
                            self.maletas.remove(self.Malas)
                            self.checklist.append(self.removemaletas)
                            print(self.Malas)
                            
                            
                            turn = turn - 1


            #Comentario - Caso a uma maleta seja escolhida, o banqueiro faz sua oferta com a maleta que foiretirada das opções
            if len(self.maletas) == 1:
              
                self.Banqueiro2(self.escolhido,self.checklist)
            self.Banqueiro(self.escolhido,self.checklist)
    #Comentario - funcao que é responsavel pela a integracao do jogo principal
    def jogar(self):
        self.main()
        self.Banqueiro()
        self.Banqueiro2()
        self.Fim()
        self.Remove()



#Comentário - cria a janela da interface
class Tabuleiro(Jogo):
    def __init__(self):
        self.maletas2 = []
        self.janela = Tk()
        self.janela["bg"]="black"
        self.janela.geometry("600x800+200+200")
        self.janela.title("interface")
        self.interface()
        
        
    #Comentario - funcao que cria um botao dizendo o valor da maleta escolhida
    def bt_onclick(self):    

        valores = ["R$ 0.5", "R$ 1","R$ 5", "R$ 10", "R$ 25", "R$ 50", "R$ 75", "R$ 100", "R$ 200", "R$ 300", "R$ 400", "R$ 500", "R$ 750","R$ 1.000", "R$ 5.000", "R$ 10.000", "R$ 25.000", "R$ 50.000", "R$ 75.000","R$ 100.000", "R$ 200.000","R$ 300.000", "R$ 400.000", "R$ 500.000", "R$ 750.000", "R$ 1.000.000"]

        
        var = self.ed.get()
        print(var)
        n_random = random.choice(valores)
        novo = []
        
        for i in self.maletas2:
            
            if i["text"] == n_random and n == 0:
                i["bg"] = "black"
                
                novo.append(i)
                self.maletas2.remove(i)
                
                
                
        
    def interface(self):
        
## Entry de dados
        self.lb27= Label(self.janela,width = 25,fg="black",bg="gold",text= "Digite a Maleta:")
        self.lb27.place(x= 300, y = 390)
        self.ed= Entry(self.janela,width = 25,fg="black",bg="gold")
        self.ed.place(x= 300, y =420 )
        self.bt27 = Button(self.janela,width= 25, text = "OK",fg="black", command = self.bt_onclick)
        self.bt27.place(x= 300, y =450)


    ## Construcao dos labels da maleta(1,26)
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
        self.maletas2.append(self.lb28)

        self.lb29= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 1")
        self.lb29.place(x = 1, y =30)
        self.maletas2.append(self.lb29)

        self.lb30= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 5")
        self.lb30.place(x = 1, y =60)
        self.maletas2.append(self.lb30)

        self.lb31= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 10")
        self.lb31.place(x = 1, y =90)
        self.maletas2.append(self.lb31)

        self.lb32= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 25")
        self.lb32.place(x = 1, y =120)
        self.maletas2.append(self.lb32)
        
        self.lb33= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 50")
        self.lb33.place(x = 1, y =150)
        self.maletas2.append(self.lb33)        

        self.lb34= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 75")
        self.lb34.place(x = 1, y =180)
        self.maletas2.append(self.lb34)

        self.lb35= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 100")
        self.lb35.place(x = 1, y =210)
        self.maletas2.append(self.lb35)

        self.lb36= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 200")
        self.lb36.place(x = 1, y =240)
        self.maletas2.append(self.lb36)
        
        self.lb37= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 300")
        self.lb37.place(x = 1, y =270)
        self.maletas2.append(self.lb37)
        
        self.lb38= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 400")
        self.lb38.place(x = 1, y =300)
        self.maletas2.append(self.lb38)

        self.lb39= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 500")
        self.lb39.place(x = 1, y =330)
        self.maletas2.append(self.lb39)

        self.lb40= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 750")
        self.lb40.place(x = 1, y =360)
        self.maletas2.append(self.lb40)

        self.lb41= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 1.000")
        self.lb41.place(x = 150, y =0)
        self.maletas2.append(self.lb41)

        self.lb42= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 5.000")
        self.lb42.place(x = 150, y =30)
        self.maletas2.append(self.lb42)

        self.lb43= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 10.000")
        self.lb43.place(x = 150, y =60)
        self.maletas2.append(self.lb43)

        self.lb44= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 25.000")
        self.lb44.place(x = 150, y =90)
        self.maletas2.append(self.lb44)

        self.lb45= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 50.000")
        self.lb45.place(x = 150, y =120)
        self.maletas2.append(self.lb45)        
        
        self.lb46= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 75.000")
        self.lb46.place(x = 150, y =150)
        self.maletas2.append(self.lb46)        
        
        self.lb47= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 100.000")
        self.lb47.place(x = 150, y =180)
        self.maletas2.append(self.lb47)
        
        self.lb48= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 200.000")
        self.lb48.place(x = 150, y =210)
        self.maletas2.append(self.lb48)

        self.lb49= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 300.000")
        self.lb49.place(x = 150, y =240)
        self.maletas2.append(self.lb49)
        
        self.lb50= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 400.000")
        self.lb50.place(x = 150, y =270)
        self.maletas2.append(self.lb50)
        
        self.lb51= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 500.000")
        self.lb51.place(x = 150, y =300)
        self.maletas2.append(self.lb51)

        self.lb52= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 750.000")
        self.lb52.place(x = 150, y =330)
        self.maletas2.append(self.lb52)

        self.lb53= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 1.000.000")
        self.lb53.place(x = 150, y =360)
        self.maletas2.append(self.lb53)



# funcao que corresponde a  tela de inicio da inteface
    def iniciar(self):
        self.janela.mainloop()
    

# funcao principal que inicializa o jogo
def INICIAR():
    interface= Tabuleiro()
    interface.iniciar()
    jogo = Jogo()
    jogo.jogar()
    
    
    
INICIAR()


         
    
        
        
        


