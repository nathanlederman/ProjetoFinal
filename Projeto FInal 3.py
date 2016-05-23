# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:21:50 2016

@author: brunoiampolsky
"""

import random
import numpy as np
import statistics as st

## from interface 2.1.py import Tabuleiro

class Jogo:
    def __init__(self):
        self.maletas = [.5, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,1000, 5000, 10000, 25000, 50000, 75000,100000, 200000,300000, 400000, 500000, 750000, 1000000]
        
        self.checklist = []
        
        self.escolha = []
        
        


    






    
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
                
  

    
    def Banqueiro(self,escolhido,checklist):
        
            self.media = sum(self.maletas)/float(len(self.maletas))
    
            self.desvio = st.stdev(self.maletas)
            
            self.desvio2 = (self.desvio/float(len(self.maletas)))*0.1
            
            self.normal1 = (np.random.normal(self.media, self.desvio2, 1))
            			
            self.oferta = self.normal1
            
            print(self.media)
            print(self.oferta)        
            
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
               
    def Banqueiro2(self,escolhido,checklist):
        
            self.media = sum(self.maletas)/float(len(self.maletas))
            
            print(self.media)        
            
            if len(self.maletas) == 1:
                self.Fim(self.media, self.escolha, self.escolhido)
             
    
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

    turnos = [6,3,6,3,3,2,1]  
    def Remove(self,escolhido,checklist):
        
        for i in self.turnos:
        
            turn = i
            while turn != 0:
            
                    print(self.escolhido) 
                    print(self.checklist)
                    print(self.maletas)
        
                    self.removemaletas = input("Escolha uma maleta para ser removida (1,26): ")
                      
        		
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
            
            if len(self.maletas) == 1:
              
                self.Banqueiro2(self.escolhido,self.checklist)
            self.Banqueiro(self.escolhido,self.checklist)   
    def iniciar(self):
        self.main()


