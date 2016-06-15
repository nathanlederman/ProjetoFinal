# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:21:50 2016

@author: brunoiampolsky
"""

import random
import numpy as np
import statistics as st
from tkinter import *

#Comentário - cria a janela da interface
class Tabuleiro:

    def __init__(self):
        self.maletas2 = []
        self.nomaletas = []
        self.janela = Tk()
        self.janela["bg"]="black"
        self.janela.geometry("600x800+200+200")
        self.janela.title("TOPA OU NÃO TOPA")
        self.interface()
        
    def bt6_onclick(self):
        self.lby.destroy()
        self.lbx.destroy()
        self.lbx1.destroy()
        self.lbx2.destroy()
        
    def bt5_onclick(self):
        self.lbc.destroy()
        self.lbd.destroy()
        self.lbe.destroy()
        self.lbf = Label(self.janela, width = 25,fg = "black" , bg = "red", text = "Voce ganhou: %d"%self.valoresvalidos[0][1] )
        self.lbf.place(x = 300 , y = 500)
        
        
    def bt4_onclick(self):    
        self.lbc.destroy()
        self.lbd.destroy()
        self.lbe.destroy()
        self.lbg = Label(self.janela, width = 25,fg = "black" , bg = "red", text = "Voce ganhou: %d"%self.valorini )
        self.lbg.place(x = 300 , y = 500)
    
    def bt3_onclick(self):
        self.lba = Label(self.janela, width = 25,fg = "black" , bg = "red", text = "Voce ganhou: %d"%self.oferta )
        self.lba.place(x = 300 , y = 500)
        
        self.lbb = Label(self.janela, width = 30 ,fg = "black" , bg = "red", text = "Sua Maleta Tinha: %d"%self.valorini)        
        self.lbb.place(x=300,y=580)
    def bt2_onclick(self):
        
        inteiros = 0
        for elementos in self.valoresvalidos:
            inteiros += elementos[1]
            
        self.oferta = inteiros /(len(self.valoresvalidos) + 1)
        
        self.lby = Label(self.janela,width = 15, fg = "black" , bg = "gold", text = self.oferta)
        self.lby.place(x = 150, y = 540)
        
        self.lbx2 = Button(self.janela,width = 15 , fg = "black" , bg = "gold", text = "Sim",command=lambda: self.bt3_onclick())
        self.lbx2.place(x = 60 , y = 600)
        
        self.lbx1 = Button(self.janela,width = 15 , fg = "black" , bg = "gold", text = "Não",command=lambda: self.bt6_onclick())
        self.lbx1.place(x = 200 , y = 600)

 #Comentario - função que ecolhe maleta inicial e seu valor randomico
    def bt0_onclick(self):

        var=self.ed.get()
        print(var)
        
        elem_random = random.choice(self.valoresvalidos) #Isso vai pegar uma lista randomica dentro da self.valoresvalidos (ex: vai pegar ["R$ 100", 100])
        if int(var) > 0 and int(var) < 27: #Essa linha significa: se o que a pessoa escreveu for maior que 0 menor que 27
            n_maleta = "Maleta " + var
            str_random = elem_random[0]
            int_random = elem_random[1]
            print(n_maleta)
            self.maletasvalidas.remove(int(var))
            self.valoresvalidos.remove(elem_random)
            self.maletaini=n_maleta
            vini=str_random.replace("R$ ","")
            self.valorini=float(vini.replace(".", ""))
            print(self.valorini)

            #for i in self.maletas2:
                
                #if i["text"] == str_random:
                    #i["bg"] = "black"
                    #self.maletas2.remove(i)
                    
            for k in self.nomaletas:
                if k["text"] == n_maleta:
                    print(k["text"])
                    k["bg"] = "gold"
                    self.nomaletas.remove(k)
                    
                    
            self.bt0.destroy()
            self.ed.destroy()
            self.lb0.destroy()
            self.lb1= Label(self.janela,width = 37,fg="black",bg="gold",text= "Escolha Maletas para Remover (Click na Maleta)")
            self.lb1.place(x= 300, y = 450)
                        
        else:
            print("Maleta Inexistente")


    #Comentario - função que remove uma maleta e um valor randomico
    def bt_onclick(self, var):

        print(var)        
        mval='False'
        
        for j in self.maletasvalidas: 
            if j == int(var):
                mval='True'
        
        print(mval)
        
        elem_random = random.choice(self.valoresvalidos)
        if int(var) > 0 and int(var) < 27 and mval=='True':
            str_random = elem_random[0]
            int_random = elem_random[1]
            n_maleta = "Maleta "+str(var)
            print(n_maleta)
            self.maletasvalidas.remove(int(var))
            self.valoresvalidos.remove(elem_random)
            print(self.maletasvalidas)
            novo = []

            for i in self.maletas2:
                
                if i["text"] == str_random:
                    i["bg"] = "black"
                    novo.append(i)
                    self.maletas2.remove(i)
                    
            for k in self.nomaletas:
                if k["text"] == n_maleta:
                    print(k["text"])
                    k["bg"] = "gold"
                    self.nomaletas.remove(k)
        
        if len(self.valoresvalidos) == 19:
            self.lbx = Button(self.janela,width = 15 , fg = "black" , bg = "gold", text = "Oferta do Banqueiro",command=lambda: self.bt2_onclick())
            self.lbx.place(x = 0 , y = 540)
            
        if len(self.valoresvalidos) == 13:
            self.lbx = Button(self.janela,width = 15 , fg = "black" , bg = "gold", text = "Oferta do Banqueiro",command=lambda: self.bt2_onclick())
            self.lbx.place(x = 0 , y = 540)
            
        if len(self.valoresvalidos) == 9:
            self.lbx = Button(self.janela,width = 15 , fg = "black" , bg = "gold", text = "Oferta do Banqueiro",command=lambda: self.bt2_onclick())
            self.lbx.place(x = 0 , y = 540)
            
        if len(self.valoresvalidos) == 4:
            self.lbx = Button(self.janela,width = 15 , fg = "black" , bg = "gold", text = "Oferta do Banqueiro",command=lambda: self.bt2_onclick())
            self.lbx.place(x = 0 , y = 540)
        
        if len(self.valoresvalidos) == 1:
                 self.lbc = Label(self.janela, width = 25,fg = "black" , bg = "red", text = "Você quer Trocar sua Maleta?" )
                 self.lbc.place(x = 350 , y = 480)
                 
                 self.lbd = Button(self.janela,width = 15 , fg = "black" , bg = "gold", text = "Sim",command=lambda: self.bt4_onclick())
                 self.lbd.place(x = 310 , y = 550)
                 self.lbe = Button(self.janela,width = 15 , fg = "black" , bg = "gold", text = "Não",command=lambda: self.bt5_onclick())
                 self.lbe.place(x = 450 , y = 550)
            
        else:
            print("Maleta Inexistente")
        
        

    def interface(self):
        
        self.maletasvalidas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
                               20,21,22,23,24,25,26]
                               
        self.valoresvalidos = [["R$ 0.5", 0.5 ], ["R$ 1",1],["R$ 5",5], ["R$ 10",10], ["R$ 25",25], ["R$ 50",50],
                               ["R$ 75",75], ["R$ 100",100], ["R$ 200",200], ["R$ 300",300], ["R$ 400",400], ["R$ 500",500], 
                               ["R$ 750",750],["R$ 1.000",1000], ["R$ 5.000",5000], ["R$ 10.000",10000], ["R$ 25.000",25000], 
                               ["R$ 50.000",50000], ["R$ 75.000",75000],["R$ 100.000",100000], ["R$ 200.000",200000],["R$ 300.000",300000], 
                               ["R$ 400.000",400000], ["R$ 500.000",500000], ["R$ 750.000",750000], ["R$ 1.000.000",1000000]]
        
        
                       
    ## Entry de dados iniciais
        self.lb0= Label(self.janela, width = 15,fg="black",bg="gold",text= "Digite Maleta Inicial")
        self.lb0.place(x= 0, y = 450)
        self.ed= Entry(self.janela, width = 18,fg="black",bg="gold")
        self.ed.place(x= 150, y = 450 )
        self.bt0 = Button(self.janela, width= 15, text = "OK",fg="black", command = self.bt0_onclick)
        self.bt0.place(x= 150, y =480)
        

        
    ## Construcao dos labels da maleta(1,26)
        self.lb28= Label(self.janela,width = 20, text = "MALETAS DISPONÍVEIS",bg= "black",fg= "gold")
        self.lb28.place(x = 300, y =0)               

        self.bt1= Button(self.janela, width = 15, text = "Maleta 1", fg= "black", command=lambda i=1: self.bt_onclick(i))
        self.bt1.place(x = 300, y =30)
        self.nomaletas.append(self.bt1)

        self.bt2= Button(self.janela, width = 15, text = "Maleta 2", fg= "black", command=lambda i=2: self.bt_onclick(i))
        self.bt2.place(x = 300, y =60)
        self.nomaletas.append(self.bt2)

        self.bt3= Button(self.janela, width = 15, text = "Maleta 3", fg= "black", command=lambda i=3: self.bt_onclick(i))
        self.bt3.place(x = 300, y =90)
        self.nomaletas.append(self.bt3)

        self.bt4= Button(self.janela, width = 15, text = "Maleta 4", fg= "black", command=lambda i=4: self.bt_onclick(i))
        self.bt4.place(x = 300, y =120)
        self.nomaletas.append(self.bt4)

        self.bt5= Button(self.janela, width = 15, text = "Maleta 5", fg= "black", command=lambda i=5: self.bt_onclick(i))
        self.bt5.place(x = 300, y =150)
        self.nomaletas.append(self.bt5)

        self.bt6= Button(self.janela, width = 15, text = "Maleta 6", fg= "black", command=lambda i=6: self.bt_onclick(i))
        self.bt6.place(x = 300, y =180)
        self.nomaletas.append(self.bt6)

        self.bt7= Button(self.janela, width = 15, text = "Maleta 7", fg= "black", command=lambda i=7: self.bt_onclick(i))
        self.bt7.place(x = 300, y =210)
        self.nomaletas.append(self.bt7)

        self.bt8= Button(self.janela, width = 15, text = "Maleta 8", fg= "black", command=lambda i=8: self.bt_onclick(i))
        self.bt8.place(x = 300, y =240)
        self.nomaletas.append(self.bt8)

        self.bt9= Button(self.janela, width = 15, text = "Maleta 9", fg= "black", command=lambda i=9: self.bt_onclick(i))
        self.bt9.place(x = 300, y =270)
        self.nomaletas.append(self.bt9)

        self.bt10= Button(self.janela, width = 15, text = "Maleta 10", fg= "black", command=lambda i=10: self.bt_onclick(i))
        self.bt10.place(x = 300, y =300)
        self.nomaletas.append(self.bt10)

        self.bt11= Button(self.janela, width = 15, text = "Maleta 11", fg= "black", command=lambda i=11: self.bt_onclick(i))
        self.bt11.place(x = 300, y =330)
        self.nomaletas.append(self.bt11)

        self.bt12= Button(self.janela, width = 15, text = "Maleta 12", fg= "black", command=lambda i=12: self.bt_onclick(i))
        self.bt12.place(x = 300, y =360)
        self.nomaletas.append(self.bt12)

        self.bt13= Button(self.janela, width = 15, text = "Maleta 13", fg= "black", command=lambda i=13: self.bt_onclick(i))
        self.bt13.place(x = 300, y =390)
        self.nomaletas.append(self.bt13)

        self.bt14= Button(self.janela, width = 15, text = "Maleta 14", fg= "black", command=lambda i=14: self.bt_onclick(i))
        self.bt14.place(x = 450, y =30)
        self.nomaletas.append(self.bt14)

        self.bt15= Button(self.janela, width = 15, text = "Maleta 15", fg= "black", command=lambda i=15: self.bt_onclick(i))
        self.bt15.place(x = 450, y =60)
        self.nomaletas.append(self.bt15)

        self.bt16= Button(self.janela, width = 15, text = "Maleta 16", fg= "black", command=lambda i=16: self.bt_onclick(i))
        self.bt16.place(x = 450, y =90)
        self.nomaletas.append(self.bt16)

        self.bt17= Button(self.janela, width = 15, text = "Maleta 17", fg= "black", command=lambda i=17: self.bt_onclick(i))
        self.bt17.place(x = 450, y =120)
        self.nomaletas.append(self.bt17)

        self.bt18= Button(self.janela, width = 15, text = "Maleta 18", fg= "black", command=lambda i=18: self.bt_onclick(i))
        self.bt18.place(x = 450, y =150)
        self.nomaletas.append(self.bt18)

        self.bt19= Button(self.janela, width = 15, text = "Maleta 19", fg= "black", command=lambda i=19: self.bt_onclick(i))
        self.bt19.place(x = 450, y =180)
        self.nomaletas.append(self.bt19)

        self.bt20= Button(self.janela, width = 15, text = "Maleta 20", fg= "black", command=lambda i=20: self.bt_onclick(i))
        self.bt20.place(x = 450, y =210)
        self.nomaletas.append(self.bt20)

        self.bt21= Button(self.janela, width = 15, text = "Maleta 21", fg= "black", command=lambda i=21: self.bt_onclick(i))
        self.bt21.place(x = 450, y =240)
        self.nomaletas.append(self.bt21)

        self.bt22= Button(self.janela, width = 15, text = "Maleta 22", fg= "black", command=lambda i=22: self.bt_onclick(i))
        self.bt22.place(x = 450, y =270)
        self.nomaletas.append(self.bt22)

        self.bt23= Button(self.janela, width = 15, text = "Maleta 23", fg= "black", command=lambda i=23: self.bt_onclick(i))
        self.bt23.place(x = 450, y =300)
        self.nomaletas.append(self.bt23)

        self.bt24= Button(self.janela, width = 15, text = "Maleta 24", fg= "black", command=lambda i=24: self.bt_onclick(i))
        self.bt24.place(x = 450, y =330)
        self.nomaletas.append(self.bt24)

        self.bt25= Button(self.janela, width = 15, text = "Maleta 25", fg= "black", command=lambda i=25: self.bt_onclick(i))
        self.bt25.place(x = 450, y =360)
        self.nomaletas.append(self.bt25)

        self.bt26= Button(self.janela, width = 15, text = "Maleta 26", fg= "black", command=lambda i=26: self.bt_onclick(i))
        self.bt26.place(x = 450, y =390)
        self.nomaletas.append(self.bt26)

    ## Valores
        self.lb1= Label(self.janela,width = 20,fg="gold",bg="black", text = "VALORES DISPONÍVEIS")
        self.lb1.place(x = 1, y =0) 

        self.lb28= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 0.5")
        self.lb28.place(x = 1, y =30)
        self.maletas2.append(self.lb28)

        self.lb29= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 1")
        self.lb29.place(x = 1, y =60)
        self.maletas2.append(self.lb29)

        self.lb30= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 5")
        self.lb30.place(x = 1, y =90)
        self.maletas2.append(self.lb30)

        self.lb31= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 10")
        self.lb31.place(x = 1, y =120)
        self.maletas2.append(self.lb31)

        self.lb32= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 25")
        self.lb32.place(x = 1, y =150)
        self.maletas2.append(self.lb32)

        self.lb33= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 50")
        self.lb33.place(x = 1, y =180)
        self.maletas2.append(self.lb33)

        self.lb34= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 75")
        self.lb34.place(x = 1, y =210)
        self.maletas2.append(self.lb34)

        self.lb35= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 100")
        self.lb35.place(x = 1, y =240)
        self.maletas2.append(self.lb35)

        self.lb36= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 200")
        self.lb36.place(x = 1, y =270)
        self.maletas2.append(self.lb36)

        self.lb37= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 300")
        self.lb37.place(x = 1, y =300)
        self.maletas2.append(self.lb37)

        self.lb38= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 400")
        self.lb38.place(x = 1, y =330)
        self.maletas2.append(self.lb38)

        self.lb39= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 500")
        self.lb39.place(x = 1, y =360)
        self.maletas2.append(self.lb39)

        self.lb40= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 750")
        self.lb40.place(x = 1, y =390)
        self.maletas2.append(self.lb40)

        self.lb41= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 1.000")
        self.lb41.place(x = 150, y =30)
        self.maletas2.append(self.lb41)

        self.lb42= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 5.000")
        self.lb42.place(x = 150, y =60)
        self.maletas2.append(self.lb42)

        self.lb43= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 10.000")
        self.lb43.place(x = 150, y =90)
        self.maletas2.append(self.lb43)

        self.lb44= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 25.000")
        self.lb44.place(x = 150, y =120)
        self.maletas2.append(self.lb44)

        self.lb45= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 50.000")
        self.lb45.place(x = 150, y =150)
        self.maletas2.append(self.lb45)

        self.lb46= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 75.000")
        self.lb46.place(x = 150, y =180)
        self.maletas2.append(self.lb46)

        self.lb47= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 100.000")
        self.lb47.place(x = 150, y =210)
        self.maletas2.append(self.lb47)

        self.lb48= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 200.000")
        self.lb48.place(x = 150, y =240)
        self.maletas2.append(self.lb48)

        self.lb49= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 300.000")
        self.lb49.place(x = 150, y =270)
        self.maletas2.append(self.lb49)

        self.lb50= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 400.000")
        self.lb50.place(x = 150, y =300)
        self.maletas2.append(self.lb50)

        self.lb51= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 500.000")
        self.lb51.place(x = 150, y =330)
        self.maletas2.append(self.lb51)

        self.lb52= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 750.000")
        self.lb52.place(x = 150, y =360)
        self.maletas2.append(self.lb52)

        self.lb53= Label(self.janela,width = 15,fg="black",bg="gold", text = "R$ 1.000.000")
        self.lb53.place(x = 150, y =390)
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


# Comentario - cria a lista de possiveis valores das maletas, e cria duas listas onde a primeira é responsável por checar as maletas que já foram escolhidas e a segunda a escolha do usuário(se ele mantém ou nao)
class Jogo(Tabuleiro):
    def __init__(self):
        
        self.maletas = [.5, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000,100000, 200000,300000, 400000, 500000, 750000, 1000000]

        self.checklist = []

        self.escolha = []

    #comentário - funcao main, checa se o usuario escolheu uma maleta dentro do range e caso esteja, randomiza as maletas e os valores e as maletas escolhidas sao adicionadas na lista checklist
    def main(self):
        #self.escolhido = Tabuleiro.getVar() #escolhido = input("Escolha a maleta (1,26): ")
        
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
    turnos = [6,3,6,3,3,2,2]
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
        
class Começo():
     def __init__(self):
        self.janela1 = Tk()
        self.janela1["bg"]="black"
        self.janela1.geometry("400x550+200+200")
        
        
        self.lbx3 = Button(self.janela1,width = 15 , fg = "black" , bg = "gold", text = "Vamos Começar?",command=lambda: self.bt7_onclick())
        self.lbx3.place(x = 140 , y = 500)
        
        foto = PhotoImage(file = "ssantos.gif")
        label = Label(image = foto)
        label.image = foto
        label.pack()
        
        title = Label(self.janela1, fg = "gold" , bg = "black" , text="TOPA OU NÃO TOPA", font=("Helvetica", 18))
        title.place(x = 90 ,y = 300)
        
        title = Label(self.janela1, fg = "gold" , bg = "black" , text="Um Jogo Para Você se Divertir Muito!", font=("Helvetica", 14))
        title.place(x = 50 ,y = 350)        
        
        
        
     def bt7_onclick(self):
         INICIAR()
         self.janela1.destroy()

     def start(self):
         self.janela1.mainloop()
        
x = Começo()
x.start()



         
    
        
        
        


