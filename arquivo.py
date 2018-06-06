r'''for arquivo in os.listdir('C:\Users\Ladetec\Desktop\projeto'):
        if os.path.isfile('C:\Users\Ladetec\Desktop\projeto' +arquivo):
            print(arquivo)'''
quantidade_nome = 0
nome = input('Digite o nome do autor a ser encontrado')
with open('documento.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha)
        if nome in linha:
            quantidade_nome+=1
    print('O autor' +nome 'possui'+ quantidade_nome 'citações no arquivo')
    
    
    #mais documentação