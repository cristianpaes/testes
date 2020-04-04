op = 0
def obternum(n1,n2):
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero:'))
    return n1, n2

while op!=5:


    print('--------------------------')
    print('MENU: \n1- SOMA\n2- DIFERENÇA\n3- MULTIPLICAÇÃO\n4- DIVISÃO\n5- SAIR')
    op = int(input('DIGITE A OPÇÃO: '))
    print('--------------------------')

    if op > 5 or op == 0:
        print("Digite uma opção valida!!!")
    else:

      if op == 1:
        num1,num2 = obternum(n1=0,n2=0)
        soma=num1+num2
        print('A soma de',num1,'e',num2,'é:',soma,'\n')
      elif op == 2:
        num1, num2 = obternum(n1=0, n2=0)
        dif=num1-num2
        print('A difereça de ', num1,'e',num2,'é:',dif,'\n')
      elif op == 3:
        num1, num2 = obternum(n1=0, n2=0)
        mult = num1 * num2
        print('A multiplicação de ', num1, 'e', num2, 'é:', mult,'\n')
      elif op == 4:
        num1, num2 = obternum(n1=0, n2=0)
        div = num1/num2
        print('A divisão de ', num1, 'por', num2, 'é:', div,'\n')
      else:
        break

print('Obrigado por usar o programa!!')
