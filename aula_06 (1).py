# -*- coding: utf-8 -*-
"""aula_06

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SkdQZTqhLQfRUb0UbkedKQfAneDebRTw

Aula 6
"""

nome = input('Digite a palavra')

if nome == type(str):
  print('É um texto')
else:
  print('Não é um texto')

  print(type(nome))


# numero = int(input('Digite a palavra>> '))

# if numero == type(int):
#   print('É um nº')
# else:
#   print('Não é um nº')

#   print(type(numero))

# a = 5
# type(a)

a = 10
b = 'A'
c = type(a)
d = type(b)

print(c, d)

numero_inteiro = 10
print(type(numero_inteiro))
real = float(numero_inteiro)
print(real)
print(type(real))

# numero_inteiro = 10.00
# print(type(numero_inteiro))
# real = str(numero_inteiro)
# print(real)
# print(type(real))

text = 'isso é um texto'
lista = list(text)
print(lista)
caractere = lista[8]
print(caractere)

for n in range(1,11):
    print(n, end=',')

lista = [1,2,3,4,5,6,7,8,9,10,11,12]

minimo_da_minha_lista = min(lista)
maximo_da_minha_lista = max(lista)
organizar= sorted(lista)
soma = sum(lista)

print('Minimo - ', minimo_da_minha_lista)
print('Maxim - ', maximo_da_minha_lista)
print('Lista organizada', organizar)
print('Soma da minha lista', soma)

# 1 Imprima uma mensagem de boas-vindas na tela.

print('Bem vindo!')

# 2 Declare uma variável booleana verdadeiro com o valor True e imprima seu tipo

n1 = 10
var = bool(n1)
print(var)
print(type(var))

# 3 Imprima o resultado da multiplicação de dois números decimais de sua escolha

n1 = 20.5
n2 = 5.1

print(n1*n2)

# 4 Imprima o resultado da divisão de dois números inteiros de sua escolha.

n1 = 50
n2 = 7
calc = n1/n2
print(calc)

# 5 Imprima o resultado da subtração de dois números inteiros de sua escolha

calc = 85-25

print(calc)

# 8 Declare uma variável numero e atribua um número inteiro. Em seguida, imprima o dobro desse número

n1 = 80

print(n1*2)

# 9 Crie uma calculadora de soma com as ferramentas que vc já conhece(Use apenas input, print e variavel)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('A some é: ',n1+n2)
print('A multiplicação é: ',n1*n2)
print('A subitração é: ',n1-n2)
print('A divisão é: ',n1/n2)

# 10 Crie um sistema de cadastro com as estruturas que vc já conhece(Use apenas input, print e variavel)

print('Olá, bem vindo! Faça já o seu cadatro!')

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
data_nascimento = input('Digite a data em que nasceu: ')

print(f'Que bom ter você aqui {nome}, sua data de nascimento é: {data_nascimento}, e você está com {idade} anos.')