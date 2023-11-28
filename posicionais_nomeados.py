#def exibir_preco(nome_produto, preco):
#    print(f'{nome_produto} está no valor de: {preco}')

#     # quando se coloca o * antes dos agumentos, torna-se nomeados
#     # def exibir_preco(nome_produto, preco):
#     # print(f'{nome_produto} está no valor de: {preco}')


# #Argumentos posicionais
# exibir_preco('iphone', preco=5000)


# exibir_preco(nome_produto='iphone', preco=5000)

# #Argumentos nomeados
# exibir_preco(preco=5000,nome_produto='iphone')


#desafio1
##Crie uma funcão chamado de gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato.A sua função deve apenas imprimir na tela o que foi passado
##para ela, nada mais, nada menos. Porém ela deve seguir as seguintes regras: 1 - Oprimeiro argumento deve ser posicional 2
## os argumentos altura e formato precisam OBRIGATÓRIAMENTE serem nomeados.

def gerar_objeto_personalizado(cor, *,altura, formato):
    print(cor, altura, formato )



gerar_objeto_personalizado('branco', altura=1.75, formato='redondo')
