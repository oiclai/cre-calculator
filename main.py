'''
Programa para Calculo do CRE
'''
from semester_data.si_schedules import ( 
      option_first_semester, option_second_semester,
      option_third_semester, option_fourth_semester,
      option_fifth_semester, option_sixth_semester,
)
from semester_data.imp_functions import (
        clear, twoSecondsPause, LessThanOneSecondPause, FiveSecondsPause
)
user_cre=0  # Para armazenar o CRE
while True:
    clear()
    print('''
       ----------------------------------------------------------------------------------
      | Olá, esse programa tem a funcionalidade de calcular o CRE dos alunos de CSTSI ^^ |
       ----------------------------------------------------------------------------------
                   Digite '0' em qualquer momento do programa para encerrar
      ''')
    
    user_nome=input('> Digite seu nome: ') # -> str
        
    if user_nome == '0': # -> str
        break
    clear()
    print(f'''
                Digite o semestre que concluiu dentre as possíveis opções:\n
                            (1) - 1º Período (Semestre)
                            (2) - 2º Período (Semestre)
                            (3) - 3º Período (Semestre)
                            (4) - 4º Período (Semestre)
                            (5) - 5º Período (Semestre)
                            (6) - 6º Período (Semestre)
      ''')
        
    user_semester=int(input('> ')) # -> int
    clear()
    match user_semester:
            
        case 1: # -> int
                option_first_semester(user_cre, user_nome)
                print('-------------------------------------------------------------------------------')
                print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
                FiveSecondsPause()
                print('-------------------------------------------------------------------------------')
        case 2: # -> int
                option_second_semester(user_cre, user_nome)
                print('-------------------------------------------------------------------------------')
                user_cre = (option_second_semester(user_cre))
                print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
                FiveSecondsPause()
                print('-------------------------------------------------------------------------------')
        case 3: # -> int
                option_third_semester(user_cre, user_nome)
                print('-------------------------------------------------------------------------------')
                user_cre = (option_third_semester(user_cre))
                print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
                FiveSecondsPause()
                print('-------------------------------------------------------------------------------')
        case 4: # -> int
                option_fourth_semester()
                print('-------------------------------------------------------------------------------')
                user_cre = (option_fourth_semester(user_cre))
                print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
                FiveSecondsPause()
                print('-------------------------------------------------------------------------------')
        case 5: # -> int
                option_fifth_semester(user_cre, user_nome)
                print('-------------------------------------------------------------------------------')
                user_cre = (option_fifth_semester(user_cre))
                print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
                FiveSecondsPause()

                print('-------------------------------------------------------------------------------')
        case 6: # -> int
                option_sixth_semester(user_cre, user_nome)
                print('-------------------------------------------------------------------------------')
                user_cre = (option_sixth_semester(user_cre))
                print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
                FiveSecondsPause()
                print('-------------------------------------------------------------------------------')
        case 0: # -> int
            break
        case _:
            print("Opcao invalida, tente de novo...")
            twoSecondsPause()
            clear()
            continue
