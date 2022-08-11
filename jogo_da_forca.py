from __future__ import barry_as_FLUFL
import time
import random
import os
from tkinter.tix import Tree
from turtle import back

# Variavis
banco_de_palavras = {
    'facil': {
        1: ('Sentimento', 'amor'),
        2: ('Materia', 'fisica'),
        3: ('Objeto', 'lapis'),
    },
    'medio': {
        1: ('Animal', 'tucano'),
        2: ('Pais', 'argentina'),
        3: ('Objeto', 'compasso'),
    },
    'dificil': {
        1: ('Animal', 'salamandra '),
        2: ('Profisão', 'diretor-geral'),
        3: ('Objeto', 'Zarabatana'),
    }
}
banco_de_palavras_copia = banco_de_palavras.copy()
palavra_sorteada = 0
dificuldade = ''
opcao = 0


def sorteador_palavra():
    global palavra_sorteada, banco_de_palavras_copia
    palavra_sorteada = random.randint(
        1, len(banco_de_palavras_copia[dificuldade]))
    print(palavra_sorteada)
    palavra = banco_de_palavras_copia[dificuldade][palavra_sorteada]
    return palavra


# Escolhendo Dificuldade
while True:
    os.system('cls')
    print('='*55)
    print('Escolha a dificildade:')
    print('1-Facil')
    print('2-Medio')
    print('3-Dificil')
    print('='*55)
    opcao = input('Escolha: ')
    if opcao == '1':
        dificuldade = 'facil'
        break
    elif opcao == '2':
        dificuldade = 'medio'
        break
    elif opcao == '3':
        dificuldade = 'dificil'
        break
    else:
        os.system('cls')
        print('='*55)
        print('Digite um valor valido!!!')
        print('='*55)
        time.sleep(2)
# Loop principal
while True:

    # Variaveis game
    game_over = False
    tentativas = 6
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    palavra = ''
    acerto = False
    palavra_secreta = []

    os.system('cls')

    palavra = sorteador_palavra()

    # Criando a palavra_secreta com a palavra
    for letraP in range(0, len(palavra[1])):
        if palavra[1][letraP] == ' ':
            palavra_secreta.append(' ')
        if palavra[1][letraP] == '-':
            palavra_secreta.append('-')
        else:
            palavra_secreta.append('_')

    # Loop game
    while game_over == 0:
        os.system('cls')

        # Tela game
        print(f'Tentativas: {tentativas}')
        print(f'Tema: {palavra[0]}')
        print('='*55)
        print(str(''.join(palavra_secreta)))
        print('='*55)
        print(str(' '.join(alfabeto)))
        print('='*55)
        letra = input('Digite uma letra: ')

        # Verificação de validade do valor digitado na variavel letra
        if len(letra) == 1:
            acerto = False
            # Verificando se a letra digitada esta na palavra
            for a in range(0, len(palavra[1])):
                if palavra[1][a] == letra:
                    # Colocando a letra na palavra_secreta
                    palavra_secreta[a] = letra
                    acerto = True

            # Verificando se o usuario acertou a letra
            if acerto == False and letra in alfabeto:
                tentativas -= 1

            # Verificando se a letra esta no alfabeto dispoivel
            if letra in alfabeto:
                # Removendo letra do alfabeto
                alfabeto.remove(letra)

            # Verificando vitoria!
            if palavra[1] == str(''.join(palavra_secreta)):
                banco_de_palavras_copia[dificuldade].pop(palavra_sorteada)
                time.sleep(2)
                os.system('cls')
                print('='*55)
                print('VOCÊ GANHOU!!!')
                print('='*55)
                time.sleep(3)
                game_over = True
            # Verificando derrota
            elif tentativas <= 0:

                time.sleep(2)
                os.system('cls')
                print('='*55)
                print('VOCÊ FOI ENFORCADO!!!')
                print('='*55)
                time.sleep(3)
                game_over = True
        # Resposta caso o valor de letra não seja valido
        else:
            os.system('cls')
            print('='*55)
            print('Digite algo valido!!!')
            print('='*55)
            time.sleep(3)
