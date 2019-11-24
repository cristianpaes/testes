from datetime import datetime
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
x = peso/(altura**2)
imc = round(x, 1)
nascimento = datetime.now().year - idade

if imc >= 18.0 and imc <= 24.9:
    resultado = 'Peso normal'
else:
      if imc >= 25.0 and imc <= 29.9:
           resultado = 'Sobrepeso'
      else:
            if imc >= 30.0 and imc<= 34.9:
                resultado = 'Obesidade Grau 1'
            else:
                if imc >= 35.0 and imc <= 39.9:
                  resultado = 'Obesidade Grau 2'
                else:
                   resultado = 'Obesidade Morbida'
print()
print(f'{nome} tem {idade} anos')
print(f'seu IMC é {imc} e você está com {resultado}')
print(f'você nasceu em {nascimento}')
print()
if resultado != 'Peso normal':
    print('Precisa fazer exercicios')