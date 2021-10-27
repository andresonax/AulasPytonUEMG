#Comentários de uma linha
"""
COMENTÁRIOS DE VÁRIAS LINHAS
"""
#gerar saída
print("Alo Mundo!")

#Declaração de variáveis
nome = "Andre Rabelo"
numero = 10
condicao = True

# print(nome + str(1))

# nome = 9

# print(nome + 1)

"""
OPERADORES ARITMÉTICOS
+ - * / ** %

O OPERADOR + EM CASO DE STRINGS CONCATENA
"""
#print(10**2)

"""
OPERADORES RELACIONAIS
== != > < >= <=
"""
# print(numero > 10)
"""
OPERADORES LÓGICOS
and or not
"""
# print((8>9) and (9>5))



# print(vetor[3])
# print(nome[0 : 3])
# print(nome.upper())
# print(nome.find("Ra"))
# print(nome[6:8])
# print(nome.replace("A", "Bao"))


# if numero > 5:
#     print("Maior que 5")
# elif numero == 5:
#     print("Igual a 5")
# else:
#     if vetor[0] > 10 :
#         print("outras informações")
#     print("Menor a 5")

# print('x')
# print('y')
# print('oi')

#Iterações ou Repetições ou Loops
x = 0
# while x < 10:
#     #escopo do while
#     x += 1
#     print(x)
vetor = [9, 10, 15, "Andre", False, "Pedro", 21]

# for v in vetor:
#     print(v)

# for letra in nome:
#     print(letra)

# for indice, valor in enumerate(vetor):
#     print("Vetor[" + str(indice) + '] = ' + str(valor))

# novoVetor = [1, 2, 3, 4, 5, 6]
# vetorParQuadrado = [n**2 for n in novoVetor if n%2==0]
# print(vetorParQuadrado)

#DECLARAÇÕES DE FUNÇÕES
# def soma(numUm, numDois):
#     #escopo da função
#     return numUm + numDois
# #chamada de função
# print(soma(9,9))

#Dicionários - JSON

pessoa = {
    'nome' : "Andre",
    'sobrenome' : 'Rabelo',
    'idade' : 35,
    'dependentes' : [
        {
            'nome' : 'Caio',
            'sobrenome' : "Rabelo",
            "idade" : 14
        },
        {
            'nome' : 'Aline',
            'sobrenome' : "Gabriela",
            "idade" : 22
        }
    ]
}
vetorPessoas=[pessoa]

print(pessoa['dependentes'][1]['nome'])
print(pessoa['dependentes'][1]['idade'])
print(vetorPessoas[0]['nome'])
