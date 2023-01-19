# name = input('Qual é o seu nome? ')

# print(f'Olá {name}, espero que esteja bem!')

# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# int_numero_1 = int(numero_1)
# int_numero_2 = int(numero_2)

# print(f'a soma de {numero_1} e {numero_2} é: {int_numero_1+int_numero_2}')

name=input('Digite seu nome: ')
weight=input('Digite seu peso: ')
stature=input('Digite sua altura: ')

float_weight = float(weight)
float_stature = float(stature)
imc  = float_weight/float_stature**2

print('')
print('-------------------------------')
print('              IMC              ')
print('-------------------------------')
print('Nome   |   {nome}'.format(nome=name))
print('-------------------------------')
print('Altura |   {altura:.2f}'.format(altura=float_stature))
print('-------------------------------')
print('Peso   |   {weight:.2f}'.format(weight=float_weight))
print('-------------------------------')
print('IMC    |   {imc:.2f}'.format(imc=imc))
print('-------------------------------')
