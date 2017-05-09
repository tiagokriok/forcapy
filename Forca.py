import os
import sys
import random
import time

pontos = 6
acertos = 0
tam = []
erradas = []
r = True
player = ['P1', 'P2']
os.system('clear')


def check(letra):  # Funcao para verificar letras
    global pontos, palavra, tam, acertos, os, time, erradas

    if letra in palavra:
        if letra in tam:  # Verifica letras repitidas
            print('Letra repitida')
            time.sleep(0.5)
            os.system('clear')

        else:   # Adiciona letra no visualizador e add pontos
            for j in range(len(palavra)):
                if letra == palavra[j]:
                    acertos += 1  # Soma aos acertos
                    tam.pop(j)  # Remove o _ do visualizador
                    tam.insert(j, letra)  # Adiciona a letra no lugar do _
                    if acertos == len(palavra):  # Verifica os acertos
                        os.system('clear')
                        print('\n\n\t\tYou Win | Palavra:', palavra)
                        time.sleep(2.5)
                        pontos = 0
                        os.system('clear')

    else:  # Diminui a vida do player
        if letra in erradas:  # Verifica letras repitidas
            print('Letra repitida')
            time.sleep(0.5)
            os.system('clear')

        else:
            pontos -= 1
            erradas.append(letra)  # Adiciona a letra as Erradas no HUD
            os.system('clear')
            if pontos == 0:
                print('\n\n\t\tGame Over, a palavra era:', palavra, '\n')
                time.sleep(2.5)
                os.system('clear')


def main():
    global os, tam, pontos, erradas, player, random, acertos, time, sys
    global check, letra, palavra, r
    rep = True

    while rep == True:

        pontos = 6
        acertos = 0
        tam = []
        erradas = []

        print('\n\t\tMenu \n')
        print('\t 1 - P1 vs IA \n')
        print('\t 2 - P1 vs P2 \n')
        print('\t 3 - QUIT \n')
        op = input('Escolha uma opção: ')

        if op == '1':
            while r == True:
                os.system('clear')
                print('\t\tCategorias \n')
                print('\t1 - Animais \n')
                print('\t2 - Objetos \n')
                op1 = input('Escolha uma opção: ')
                choice(op1)
            play()
            r = True

        elif op == '2':
            os.system('clear')
            palavra = ''
            tam = []
            player_esc = player[random.randint(0, 1)]
            palavra = input('%s digite uma palavra:  ' % player_esc)
            palavra = str.lower(palavra)
            os.system('clear')
            play()

        elif op == '3':
            time.sleep(0.6)
            os.system('clear')
            rep = False

        else:
            print('Opção Invalida....')
            time.sleep(0.6)
            os.system('clear')


def play():
    global pontos, erradas, tam, palavra, acertos, os, check

    for i in range(len(palavra)):
        tam.append('_')
    while pontos > 0:
        os.system('clear')  # HUD do Jogo
        print('Vida:', pontos, '| Total de Letras:', len(palavra),
              '| Acertos:', acertos, '| Letras erradas:', erradas)

        print('\n\t\t-->', tam, '\n')  # Visualizador da Palavra
        letra = input('Digite um letra: ')
        letra = str.lower(letra)
        check(letra)


def choice(op):
    global palavra, r

    animais = ['cachorro', 'leao', 'tigre', 'gato', 'foca', 'elefante',
               'girafa', 'zebra', 'tartaruga', 'onca', 'vaca', 'boi',
               'carneiro', 'bode', 'iena', 'urso', 'cobra', 'macaco',
               'galinha', 'galo', 'esquilo', 'hipopotamo', 'coelho', 'baleia',
               'gazela', 'golfinho', 'peixe', 'orca', 'pinguim', 'rato',
               'gamba', 'cervo', 'alce', 'panda', 'passaro', 'aguia',
               'avestruz', 'bufalo', 'cabra', 'camelo', 'capivara', 'cavalo',
               'pato', 'coala', 'corvo', 'crocodilo', 'gaviao', 'gorila',
               'jacare', 'leopardo', 'lobo', 'lula', 'papagaio', 'polvo',
               'pombo', 'porco', 'puma', 'raposa', 'rinoceronte', 'sapo',
               'tatu', 'touro', 'tucano', 'urubu']

    objetos = ['faca', 'garfo', 'colher', 'computador', 'mesa', 'cadeira',
               'ventilador', 'abajur', 'escova', 'televisao', 'tv', 'sofa',
               'celular', 'fogao', 'geladeira', 'cama', 'armario', 'porta',
               'bola', 'escada', 'lapis', 'caneta', 'borracha', 'mochila',
               'mala', 'chuveiro', 'copo', 'panela', 'roupa', 'cabide',
               'martelo', 'chave']

    if op == '1':

        palavra = animais[random.randint(0, len(animais))]
        r = False

    elif op == '2':

        palavra = objetos[random.randint(0, len(objetos))]
        r = False

    else:

        print('Opção Invalida...')
        time.sleep(0.6)


if __name__ == '__main__':
    main()
