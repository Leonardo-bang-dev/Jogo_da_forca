import time
import random
import os
from tkinter.tix import Tree

while True:
    game_over = False 
    tentativas = 6
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    palavra = ''
    acerto = False
    palavra_secreta = []

    os.system('cls')

    palavra = input('Digite uma palavra:')

    for letraP in range(0,len(palavra)):
        palavra_secreta.append('_')

    print(str(''.join(palavra_secreta)))

    while game_over == 0:
        os.system('cls')

        print(f'Tentativas: {tentativas}')
        print('='*55)
        print(str(''.join(palavra_secreta)))
        print('='*55)
        print (str(' '.join(alfabeto)))
        print('='*55)
        letra = input('Digite uma letra: ')


        if len(letra) == 1:
            acerto = False
            for a in range(0, len(palavra)):
                if palavra[a] == letra:
                    palavra_secreta[a] = letra
                    acerto = True
            
            if acerto == False and letra in alfabeto:
                tentativas -= 1
                
            if letra in alfabeto:
                alfabeto.remove(letra)
            
            if palavra == str(''.join(palavra_secreta)):
                time.sleep(2)
                os.system('cls')
                print('='*55)
                print('VOCÊ GANHOU!!!')
                print('='*55)
                time.sleep(3)
                game_over = True
            elif tentativas <= 0: 
                time.sleep(2)
                os.system('cls')
                print('='*55)
                print('VOCÊ FOI ENFORCADO!!!')
                print('='*55)
                time.sleep(3)
                game_over = True
        else: 
            os.system('cls')
            print('='*55)
            print('Digite algo valido!!!')
            print('='*55)
            time.sleep(3)



    

        