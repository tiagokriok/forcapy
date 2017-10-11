import os
import sys
import random
import time
import sqlite3

# Conexão com BD SQLite
conn = sqlite3.connect('forca.db')
c = conn.cursor()

pontos = 6
acertos = 0
tam = []
erradas = []
r = True
player = ['P1', 'P2']

so = sys.platform # Verifica Sistema Operacional
if 'win' in so:
    limpa = 'cls'
else:
    limpa = 'clear'

os.system(limpa)


def check(letra):  # Função para verificar letras
    global pontos, palavra, tam, acertos, os, time, erradas

    if letra in palavra:
        if letra in tam:  # Verifica letras repitidas
            print('Letra repitida')
            time.sleep(0.5)
            os.system(limpa)

        else:   # Adiciona letra no visualizador e add pontos
            for j in range(len(palavra)):
                if letra == palavra[j]:
                    acertos += 1  # Soma aos acertos
                    tam.pop(j)  # Remove o _ do visualizador
                    tam.insert(j, letra)  # Adiciona a letra no lugar do _
                    if acertos == len(palavra):  # Verifica os acertos
                        os.system(limpa)
                        print('\n\n\t\tVocê Venceu | Palavra:', palavra)
                        time.sleep(2.5)
                        pontos = 0
                        os.system(limpa)

    else:  # Diminui a vida do player
        if letra in erradas:  # Verifica letras repitidas
            print('Letra repitida')
            time.sleep(0.5)
            os.system(limpa)

        else:
            pontos -= 1
            erradas.append(letra)  # Adiciona a letra as Erradas no HUD
            os.system(limpa)
            if pontos == 0:
                print('\n\n\t\tSuas chances acabaram, a palavra era:', palavra, '\n')
                time.sleep(2.5)
                os.system(limpa)


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
                os.system(limpa)
                print('\t\tCategorias \n')
                print('\t1 - Animais \n')
                print('\t2 - Objetos \n')
                op1 = input('Escolha uma opção: ')
                choice(op1)
            play()
            r = True

        elif op == '2':
            os.system(limpa)
            palavra = ''
            tam = []
            player_esc = player[random.randint(0, 1)]
            palavra = input('%s digite uma palavra:  ' % player_esc)
            palavra = str.lower(palavra)
            os.system(limpa)
            play()

        elif op == '3':
            time.sleep(0.6)
            c.close() # Finaliza o cursor
            conn.close() # Finaliza a conexão com o BD
            os.system(limpa)
            rep = False

        else:
            print('Opção Inválida....')
            time.sleep(0.6)
            os.system(limpa)


def play():
    global pontos, erradas, tam, palavra, acertos, os, check

    for i in range(len(palavra)):
        tam.append('_')
    while pontos > 0:
        os.system(limpa)  # HUD do Jogo
        print('Vida:', pontos, '| Total de Letras:', len(palavra),
              '| Acertos:', acertos, '| Letras erradas:', erradas)

        print('\n\t\t-->', tam, '\n')  # Visualizador da Palavra
        letra = input('Digite um letra: ')
        letra = str.lower(letra)
        check(letra)


def choice(op):
    global palavra, r

   
    if op == '1':
        
        c.execute('SELECT count(*) FROM animais') # Ver quantas palavras tem
        qtd_ani = c.fetchone()[0] # Passa a quantidade para a variável
        esc_ani = random.randint(1, qtd_ani) # Escolhe um número random
        
        c.execute('SELECT anipal FROM animais WHERE anicod=?', (esc_ani,)) # Faz a procura da palavra atraves do codigo
        palavra = c.fetchone()[0] # Retorna a palavra
        
        r = False

    elif op == '2':
        c.execute('SELECT count(*) FROM objetos') # Ver quantas palavras tem
        qtd_obj = c.fetchone()[0] # Passa a quantidade para a variável
        esc_obj = random.randint(1, qtd_obj) # Escolhe um número random

        c.execute('SELECT objpal FROM objetos WHERE objcod=?', (esc_obj,)) # Faz a procura da palavra atraves do codigo
        palavra = c.fetchone()[0] # Retorna a palavra

        r = False

    else:

        print('Opção Invalida...')
        time.sleep(0.6)


if __name__ == '__main__':
    main()

