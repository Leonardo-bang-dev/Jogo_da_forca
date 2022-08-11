import time
import random
import os
from tkinter.tix import Tree

# Variavis
banco_de_palavras = {
    'facil':{
        'Sentimento':'amor',
        'Sentimento': 'medo',
        'Alimento': 'bala',
        'Materia': 'artes',
        'Materia': 'fisica',
        'Objeto': 'lapis',
        'Objeto': ''
    },
    'medio':{
        'Animal': 'tucano',
        'Animal': 'lemore',
        'Pais': 'argentina',
        'Pais': 'uruguai',
        'Objeto': 'luneta',
        'Objeto': 'compasso',
    },
    'dificil':{
        'Animal': 'beija-flor',
        'Animal': 'salamandra ',
        'Profisão': 'diretor-geral',
        'Profissão': 'costureira',
        'Objeto': 'bola de gude',
        'Objeto': 'Zarabatana',
    }
}
banco_de_palavras_copia = banco_de_palavras.copy()
palavra_sorteada = 0
dificuldade = 'facil'
palavra = ''


def sorteador_palavra():
    global palavra_sorteada, palavra_sorteada, palavra
    palavra_sorteada = random.randint(0, len(banco_de_palavras_copia[dificuldade]))
    palavra = banco_de_palavras_copia[dificuldade][palavra_sorteada]

sorteador_palavra()
print(palavra)