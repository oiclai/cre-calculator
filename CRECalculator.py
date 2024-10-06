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
def calculo (media,carga):
    global totalSoma, cargaGeral  # declarando variáveis globais
    materia= media*carga
    totalSoma+=materia
    cargaGeral+=carga
    calculoCRE=totalSoma/cargaGeral
    return calculoCRE
# programa principal 
for i in range (1,qtdMaterias+1):
    media, carga=map(float, input(f'> Digite a média geral seguida pela carga horaria da {i}ª matéria: ').split())
calculoCRE=calculo(media,carga) 
print('-------------------------------------------------------------------------------')
print(f'CRE d/{nome}: {calculoCRE:.1f} !')
print('-------------------------------------------------------------------------------')