print('''
Bem-vindos(as) à Calculadora!
''')
while True:
  print('Você quer somar, subtrair, multiplicar, dividir ou exponenciar?')
  choice = input()
  if choice == 'somar':
    print('Digite o primeiro número: ')
    a = int(input())
    print('Digite o segundo número: ')
    b = int(input())
    print(a + b)
  if choice == 'subtrair':
    print('Digite o primeiro número: ')
    a = int(input())
    print('Digite o segundo número: ')
    b = int(input())
    print(a - b)
  if choice == 'multiplicar':
    print('Digite o primeiro número: ')
    a = int(input())
    print('Digite o segundo número: ')
    b = int(input())
    print(a * b)
  if choice == 'dividir':
    print('Digite o primeiro número: ')
    a = int(input())
    print('Digite o segundo número: ')
    b = int(input())
    print(a / b)
  if choice == 'exponenciar':
    print('Digite o primeiro número: ')
    a = int(input())
    print('Digite o segundo número: ')
    b = int(input())
    print(a**b)