from __future__ import barry_as_FLUFL
import time
import random
import os
from tkinter.tix import Tree
from turtle import back

pontos = 0
nivel = 0
# Loop principal
while True:
    # Variavis
    banco_de_palavras = {
        'facil': [
            ('Sentimento', 'amor'),
            ('Materia', 'fisica'),
            ('Objeto', 'lapis'),
        ],
        'medio': [
            ('Animal', 'tucano'),
            ('Pais', 'argentina'),
            ('Objeto', 'compasso'),
        ],
        'dificil': [
            ('Animal', 'salamandra'),
            ('Profisão', 'diretor-geral'),
            ('Objeto', 'zarabatana'),
        ]
    }
    banco_de_palavras_copia = banco_de_palavras.copy()
    palavra_sorteada = 0
    dificuldade = ''
    opcao = 0

    def sorteador_palavra():
        global palavra_sorteada, banco_de_palavras_copia
        palavra_sorteada = random.randint(
            0, len(banco_de_palavras_copia[dificuldade]) - 1)
        print(palavra_sorteada)
        if len(banco_de_palavras_copia[dificuldade]) > 0:
            palavra = banco_de_palavras_copia[dificuldade][palavra_sorteada]
        else:
            palavra = 'game_over'
        return palavra

    # Escolhendo Dificuldade
    while True:
        if pontos >= 2:
            nivel += 1
        pontos = 0

        os.system('cls')
        print('='*55)
        print('-'*55)
        print('JOGO DA FORCA')

        print('-'*55)
        print('='*55)
        print('Entre em cada nivel e consiga 3 vitórias')
        print('='*55)
        print('Escolha a dificildade:')
        if nivel >= 0:
            print('1-Facil')
        if nivel >= 1:
            print('2-Medio')
        if nivel >= 2:
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

    # Loop reinicio
    while pontos < 3:

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
        if palavra == 'game_over':
            break

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
            print(f'Pontos: {pontos}')
            print(f'Tema: {palavra[0]}')
            print('='*55)
            print(str(''.join(palavra_secreta)))
            print(f'Letras: {len(palavra_secreta)}')
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
                    pontos += 1
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
                time.sleep(1.4)
