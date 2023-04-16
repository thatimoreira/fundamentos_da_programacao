nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))

if idade < 18:
    print(f'{nome}, você é menor de idade.')
else:
    print(f'{nome}, você é maior de idade.')