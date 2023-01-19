nome=input('Digite seu nome: ')
idade=input('Digite sua idade: ')

quant_letras=len(nome)
contador=quant_letras

if not nome and not idade: 
    print('Deslcupe, você não preencheu corretamente.')
else:
    print(f'Seu nome é {nome}')
    print(f'Nome invertido: {nome[::-1]}')
    if' ' in nome: print(f'Tem espaço')
    print(f'Nº de letras: {len(nome)}')
    print(f'Primeira letra: {nome[0]}')
    print(f'Ultima letra: {nome[-1]}')