import time
import random
import os

# Variavis
banco_de_palavras = {
    'facil':{
        'Sentimento':'amor',
        'Materia': 'fisica',
        'Objeto': 'lapis',
    },
    'medio':{
        'Animal': 'tucano',
        'Pais': 'argentina',
        'Objeto': 'compasso',
    },
    'dificil':{
        'Animal': 'salamandra ',
        'Profisão': 'diretor-geral',
        'Objeto': 'Zarabatana',
    }
}

banco_de_palavras_copia = banco_de_palavras.copy()
palavra_sorteada = 0
dificuldade = 'facil'
palavra = ''




banco_de_palavras_copia[dificuldade].pop('amor')

print(banco_de_palavras_copia[dificuldade])