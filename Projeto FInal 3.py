# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:21:50 2016

@author: brunoiampolsky
"""

import random
import numpy as np
import statistics as st



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

main()
