#Comentário de uma linha
"""
comentário de várias linhas opcional

"""
#Gerar Saída
print("Alo Mundo!")

#declaração de variáveis dinâmicas
nome = "Andre Rabelo"
numero = 10

""""
OPERADORES ARITMETICOS
+ - * / ** %
"""
print((numero**2)) #POTENCIA

""""
OPERADORES RELACIONAIS
== != > < >= <=
"""
print(numero == 11)

""""
OPERADORES LÓGICOS
and or not
"""
# print(numero < 10 and numero == 10)

vetor = [9 , 3, 5, 6, '"Matheus"', "'Gustavo'", True]

# print(vetor[0] + vetor[2])

# print(vetor[4])

#Condicionais
# if numero < 4:
#     print("Menor que 4")
# else:
#     print("Maior ou igual a 4")
# if numero < 4:
#     print("Menor que 4")
# elif numero == 4:
#     print("Igual a 4")
# else:
#     print("Maior que 4")

#Iterações
x = 0
# while x <= 10:
#     x += 1
#     print(x)

# for v in vetor:
#     print(v) 
#     print("oi")
#     print("oi de novo")

# for letra in "acabou" :
#     print(letra)

# print(nome[3])
# print(nome[0:5])

# print(nome.find("dre"))
# print(nome.replace("A", "B"))

x = [55, 22 ,35 , 11, 5]

# y = [i**2 for i in x if i%2==0]
# print(x)
# print(y)

# for indice, valor in enumerate(x):
#     print("x[" + str(indice) + "] =" + str(valor))


def soma(num01, num02):
    #corpo da função
    return num01 + num02

print(soma(3,8))

#Dicionários - JSON

dicionario = {
    'nome' : 'Andre',
    'sobrenome' : "Rabelo",
    'idade' : 40,
    'dependentes' : [
        {
            'nome' : 'Caio',
            'idade' : 14
        },
        {
            'nome' : 'Gustavo',
            'idade' : 22
        }
    ]
}

print(dicionario['dependentes'][0]['nome'])


















   










