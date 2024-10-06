'''
Programa para Calculo do CRE
'''
cargaGeral=0
totalSoma=0
print('''
       -------------------------------------------------------------------------------
      | Olá, esse é um programa bem simples com a funcionalidade de calcular o CRE ^^ |
       -------------------------------------------------------------------------------
      ''')
nome=input('> Digite seu nome: ')
qtdMaterias=int(input('> Quantas matérias foram cursadas: '))
for i in range (1,qtdMaterias+1):
    media, carga=map(float, input(f'> Digite a média geral seguida pela carga horaria da {i}ª matéria: ').split())
    materia= media*carga
    totalSoma+=materia
    cargaGeral+=carga
calculoCRE=totalSoma/cargaGeral
print('-------------------------------------------------------------------------------')
print(f'CRE d/{nome}: {calculoCRE:.1f} !')
print('-------------------------------------------------------------------------------')