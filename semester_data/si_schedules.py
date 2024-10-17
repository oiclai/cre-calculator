'''
FUNÇÕES A SEREM IMPORTADAS PARA CRECALCULATOR.PY
'''

# NOVAMENTE COM ERRO NO CODIGO - CALCULO
# ---------------------------------------------------- 1º PERÍODO
def option_first_semester(user_nome): 
    totalSum=0
    totalWorkload=0
    user_cre=0
    schedule_1semester={
        'Calculo I': int(83),
        'APE' : int(83),
        'Fund. Redes' : int(67),
        'Linguagem de Marcação' : int(67),
        'Fund. Computação' : int(50),
        'Lingua Portuguesa' : int(50)
    }

    libras=input(f'> {user_nome}, esta matriculado em libras? (s/n) : ').lower()
    if libras=='s':
        schedule_1semester['Libras'] = int(33)

    for subject in schedule_1semester:
        media=(int(input(f'> Digite a média geral de {subject} : ')))
        totalWorkload+=(schedule_1semester[subject])
        totalSum+=(media*schedule_1semester[subject])
    user_cre=(totalSum/totalWorkload)
    print(f'> CRE d/{user_nome}: {user_cre:.2f} !')

# ---------------------------------------------------- 2º PERÍODO
def option_second_semester(user_nome):
    totalSum=0
    totalWorkload=0
    user_cre=0
    schedule_2semester={
        'Sist. Operacionais': int(83),
        'Banco de Dados I' : int(67),
        'Estruturas de Dados' : int(67),
        'Linguagens de Script ' : int(67),
        'Protocolos de Interconexao de Redes de Computadores' : int(67),
        'Fundamentos da Metodologia ' : int(33),
        'Ciencia, Tecnologia e Meio Ambiente': int(33)
    }

    libras=input(f'> {user_nome}, esta matriculado em libras? (s/n) : ').lower()
    if libras=='s':
        schedule_2semester['Libras'] = int(33)

    for subject in schedule_2semester:
        media=(int(input(f'> Digite a média geral de {subject} : ')))
        totalWorkload+=(schedule_2semester[subject])
        totalSum+=(media*schedule_2semester[subject])
    user_cre=(totalSum/totalWorkload)
    print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
# ---------------------------------------------------- 3º PERÍODO
def option_third_semester(user_nome):
    totalSum=0
    totalWorkload=0
    user_cre=0
    schedule_3semester={
        'Programação Orientada a Objetos': int(100),
        'Banco de Dados II' : int(83),
        'Probabilidade e Estatística' : int(67),
        'Interacao Humano-Computador' : int(67),
        'Psicologia do Trabalho' : int(50),
        'Lingua Inglesa' : int(50)
    }

    libras=input(f'> {user_nome}, esta matriculado em libras? (s/n) : ')
    if libras=='s':
        schedule_3semester['Libras'] = int(33)

    for subject in schedule_3semester:
        media=(int(input(f'> Digite a média geral de {subject} : ')))
        totalWorkload+=(schedule_3semester[subject])
        totalSum+=(media*schedule_3semester[subject])
    user_cre=(totalSum/totalWorkload)
    print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
# ---------------------------------------------------- 4º PERÍODO
def option_fourth_semester(user_nome):
    totalSum=0
    totalWorkload=0
    schedule_4semester={
        'Analise e Projeto de Sistemas': int(67),
        'Legislacao Social' : int(67),
        'Persistencia de Objetos' : int(67),
        'Programacao para Web I' : int(67),
        'Seguranca de Dados' : int(50),
        'Metodos e Tecnicas de Pesquisa SI' : int(50),
        'Etica e Direitos Humanos' : int(33)
    }

    libras=input(f'> {user_nome}, esta matriculado em libras? (s/n) : ')
    if libras=='s':
        schedule_4semester['Libras'] = int(33)

    for subject in schedule_4semester:
        media=(int(input(f'> Digite a média geral de {subject} : ')))
        totalWorkload+=(schedule_4semester[subject])
        totalSum+=(media*schedule_4semester[subject])
    user_cre=(totalSum/totalWorkload)
    print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
# ---------------------------------------------------- 5º PERÍODO
def option_fifth_semester(user_nome):
    totalSum=0
    totalWorkload=0
    user_cre=0
    schedule_5semester={
        'Programação para Web II': int(100),
        'Programacao de Dispositivos Móveis' : int(67),
        'Padrões de Projetos de Software' : int(67),
        'Gerencia de Projetos de Software' : int(67),
        'Empreendedorismo' : int(67),
        'Comercio Eletronico' : int(50)
    }

    libras=input(f'> {user_nome}, esta matriculado em libras? (s/n) : ')
    if libras=='s':
        schedule_5semester['Libras'] = int(33)

    for subject in schedule_5semester:
        media=(int(input(f'> Digite a média geral de {subject} : ')))
        totalWorkload+=(schedule_5semester[subject])
        totalSum+=(media*schedule_5semester[subject])
    user_cre=(totalSum/totalWorkload)
    print(f'> CRE d/{user_nome}: {user_cre:.2f} !')
# ---------------------------------------------------- 6º PERÍODO
def option_sixth_semester(user_nome):
    user_cre=0
    totalSum=0
    totalWorkload=0
    schedule_6semester={
        'Desenvolvimento e Execucao de Projetos de Software': int(67),
        'Inteligencia Empresarial' : int(67),
        'Programação Distribuída' : int(67),
        'Desenvolvimento Agil com Ferramenta RAD' : int(50),
        'Topicos Especiais' : int(50)
    }

    libras=input(f'> {user_nome}, esta matriculado em libras? (s/n) : ')
    if libras=='s':
        schedule_6semester['Libras'] = int(33)

    for subject in schedule_6semester:
        media=(int(input(f'> Digite a média geral de {subject} : ')))
        totalWorkload+=(schedule_6semester[subject])
        totalSum+=(media*schedule_6semester[subject])
    user_cre=(totalSum/totalWorkload)
    print(f'> CRE d/{user_nome}: {user_cre:.2f} !')