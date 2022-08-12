import time
import random
import os

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
        ('Objeto', 'Zarabatana'),
    ]
}

banco_de_palavras_copia = banco_de_palavras.copy()
palavra_sorteada = 0
dificuldade = 'facil'
palavra = ''


def sorteador_palavra():
    global palavra_sorteada, banco_de_palavras_copia
    palavra_sorteada = random.randint(
        0, (len(banco_de_palavras_copia[dificuldade]-1)))
    print(palavra_sorteada)
    palavra = banco_de_palavras_copia[dificuldade][palavra_sorteada]
    return palavra


print(len(banco_de_palavras_copia[dificuldade]))
print(banco_de_palavras_copia[dificuldade][2])
# for i in range(0, 5):
#palavra = sorteador_palavra()

# print(palavra)
