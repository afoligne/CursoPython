import os 

def busca_autor(arquivo, nome):
    quantidade_nome = 0
    with open(arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            if nome in linha:
                quantidade_nome+=1
    print('O autor',nome,' possui ', str(quantidade_nome) , 'citações no arquivo')

def busca_arquivos():
     nome = input('Digite o nome do autor a ser encontrado: ')
     for arquivo in os.listdir(os.getcwd()):
        print(arquivo)
        if os.path.isfile(os.getcwd() +arquivo):
            arquivo = os.getcwd() +arquivo
            busca_autor(arquivo, nome)
    
busca_arquivos()