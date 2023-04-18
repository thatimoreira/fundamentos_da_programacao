# Lista de exercícios - Introdução ao Python  |  Desafio da Let's Code

# Questão 2) Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
# dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
# esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

# Entrada: 25.01 | Saída: (25,50]
# Entrada: 25.00 | Saída: [0,25]
# Entrada: 100.00 | Saída: (75,100]
# Entrada: -25.02 | Saída: Fora de intervalo

numero = float( input('Informe um número: '))


if numero > 0 and numero <= 25:
    print(f'{numero} está no intervalo [0,25]')
elif numero > 25 and numero <= 50:
    print(f'{numero} está no intervalo (25,50]')
elif numero > 50 and numero <= 75:
    print(f'{numero} está no intervalo (50,75]')
elif numero > 75 and numero <= 100:
    print(f'{numero} está no intervalo (75,100]')
else:
    print(f'{numero} está no fora do intervalo')