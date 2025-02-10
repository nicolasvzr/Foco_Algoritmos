"""def pesquisa_binaria(lista, item):
    nome = 0
    ultimo_nome = len(lista) -1

    while nome <= ultimo_nome:
        meio = (nome + ultimo_nome) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            ultimo_nome = meio - 1
        else:
            nome = meio + 1
    return None
    

minha_lista = [2,4,8,32,128]
print (pesquisa_binaria(minha_lista, 128))
print (pesquisa_binaria(minha_lista, -1))"""


#1.2 Suponha que você duplique o tamanho da lista. Qual seria o número
#máximo de etapas agora?

def pesquisa_binaria(lista, item):
    nome = 0
    ultimo_nome = len(lista) -1
    passos = 0
    
    while nome <= ultimo_nome:
        meio = (nome + ultimo_nome) // 2
        chute = lista[meio]
        passos += 1
        if chute == item:
            return meio, passos
        if chute > item:
            ultimo_nome = meio - 1
        else:
            nome = meio + 1 
    return None, passos
 
minha_lista = [2,4,8,32,128, 256 ]
print (pesquisa_binaria(minha_lista, 4))
print (pesquisa_binaria(minha_lista, -1))
