#Aula 6
#planilha.py

'''Este programa vai abrir uma planilha, ler a primeira coluna e salvar
a media, mediana e o numero de linhas em um arquivo txt'''

from tkinter import filedialog, Tk
from faz_grafico import faz_grafico
#import faz_grafico as faz_grafico

def pede_arquivo():
    '''retorna o caminho para um arquivo definido pelo usuario'''
    root = Tk()
    root.withdraw()
    nome_arquivo = filedialog.askopenfilename()
    return nome_arquivo
    
def abre_arquivo(nome_arquivo):
    '''retorna uma lista com as linhas do arquivo'''
    lista_linhas = []
    with open(nome_arquivo, 'r') as planilha:
        for linha in planilha:
            lista_linhas.append(linha.strip())
    return lista_linhas

def converte_lista_numeros(lista_linhas):
    '''recebe uma lista de palavras e retorna uma lista de numeros'''
    lista_numeros = []
    for linha in lista_linhas:
        lista_numeros.append(float(linha))
    return lista_numeros

def converte_lista_numeros_comprehension(lista_linhas):
    '''funcao exemplo de list comprehension'''
    return [float(linha) for linha in lista_linhas]

def analise_dados(lista_numeros):
    '''recebe uma lista de numeros e
    retorna uma tupla (media, mediana, quantidade de linhas) '''
    soma = sum(lista_numeros)
    tamanho = len(lista_numeros)
    media = soma/tamanho
    if not tamanho % 2 == 0:
        indice = int((tamanho-1)/2)
        mediana = lista_numeros[indice]
    else:
        mediana = (lista_numeros[int(tamanho/2)] + lista_numeros[int(tamanho/2) - 1])/2
    return media, mediana, tamanho

def salva_resultado(media, mediana, tamanho):
    '''Recebe os resultado e salva num arquivo.'''
    with open('resultados.txt', 'w') as saida:
        saida.write('a media é: {}\n a mediana é: {}\n e o tamanho é: {}.'.format(media,
                                                                               mediana,
                                                                               tamanho))   
def main():
    '''Logica principal do programa, chama todas as outras funcoes'''
    nome_arquivo = pede_arquivo()
    lista_linhas = abre_arquivo(nome_arquivo)
    lista_numeros = converte_lista_numeros(lista_linhas)
    media, mediana, tamanho = analise_dados(lista_numeros)
    salva_resultado(media, mediana, tamanho)
    faz_grafico(lista_numeros)
    
main()