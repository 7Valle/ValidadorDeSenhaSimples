# Tabela IMC:
# Abaixo de 19.1: Abaixo do peso
# Entre 19.1 e 25.8: Peso normal
# Entre 25.9 e 27.3: Pouco acima do peso
# Entre 27.4 e 32.3: Acima do peso
# Acima de 32.4: Obesidade
# Fórmula do IMC: Peso / (altura * altura)

def imc(peso, altura):
    formula = peso / (altura * altura)
    return formula
print('---------Calculadora de IMC---------')
peso = float(input('\nInforme o peso em Kg: '))
altura = float(input('Informe a altura em M: '))

formula = imc(peso, altura)

if formula < 19.1:
    print(f'\nSeu IMC é: {formula:.2f}, você está abaixo do peso!')
elif formula >= 19.1 and formula <= 25.8:
    print(f'\nSeu IMC é: {formula:.2f}, você está no peso normal!')
elif formula >= 25.9 and formula <= 27.3:
    print(f'\nSeu IMC é: {formula:.2f}, você está um pouco acima do peso!')
elif formula >= 27.4 and formula <= 32.3:
    print(f'\nSeu IMC é: {formula:.2f}, você está acima do peso!')
elif formula > 32.4:
    print(f'\nSeu IMC é: {formula:.2f}, você está obeso!')