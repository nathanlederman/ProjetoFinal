# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:21:50 2016

@author: brunoiampolsky
"""

import random

maletas = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,1000, 5000, 10000, 25000, 50000, 75000,100000, 200000,300000, 400000, 500000, 750000, 1000000]

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
            
  
  

def	Remove(escolhido,checklist):
	
	turn = 5
	while turn != 0:

            print(escolhido) 
            print(checklist)
            print(maletas)

            removemaletas = input("Escolha uma maleta para ser removida (1,26): ")
              
		
            if int(removemaletas) > 26 or int(removemaletas) < 1:
                print ("Maleta não existente")
            if removemaletas in checklist:
                print ("Essa maleta já foi escolhida")
			
            else:
			 
                    Malas = random.choice(maletas)
                    maletas.remove(Malas)
                    checklist.append(removemaletas)
                    print(Malas)
                    
                    
                    turn = turn - 1
   

main()
