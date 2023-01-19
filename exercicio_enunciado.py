""" Exercicio 01 Enuciado
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
""" Exercicio 01

value_input = input('Digite um numero inteiro: ')

try:
    number_int = int(value_input)
    is_even_number = number_int % 2 == 0
    
    if is_even_number:
        print('O número é par')
    else:
        print('O número é impar')
except:
    print('O valor digitado não é um número inteiro')
"""

""" Exercicio 02 Enuciado
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
""" Exercicio 02
value_input = input('Digite a hora do dia (Ex: 10): ')

try:
    time_of_day = int(value_input) 
    
    if time_of_day >= 0 and time_of_day <12:
        print('Bom dia')
    elif time_of_day >= 12 and time_of_day <18:
        print('Boa tarde')
    elif time_of_day >= 18 and time_of_day <24:
        print('Boa noite')
    else: 
        print('O dia varia entre 0 e 23 horas, horário inválido')
except:
    print(f'Valor valor {value_input} não pode ser aceito, mas independete do horário que o dia seja bom HAHAHA')
"""

"""Exercicio 03 Enuciado
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""Exercicio 03
value_input = input('Digite seu primeiro nome: ')
len_name = len(value_input)

if value_input.isalpha():
    print(f'Nome: {value_input}')
    print(f'Tamanho: {len_name}')

    if len_name <5:
        print('Classificação: Nome curto')
    elif len_name >= 5 and len_name <=6:
        print('Classificação: Nome normal')
    else:
        print('Classificação: Nome grande')
else:
        print('Valor inválido.')
"""
value_input = input('Digite seu primeiro nome: ')
len_name = len(value_input)

if value_input.isalpha():
    print(f'Nome: {value_input}')
    print(f'Tamanho: {len_name}')

    if len_name <5:
        print('Classificação: Nome curto')
    elif len_name >= 5 and len_name <=6:
        print('Classificação: Nome normal')
    else:
        print('Classificação: Nome grande')
else:
        print('Valor inválido.')


