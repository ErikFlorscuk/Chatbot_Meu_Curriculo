import os

def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep} {nome}, deve me contratar porque sou competitivo, focado, ambicioso e sempre dou o meu melhor para ser o melhor. Meu maior motivo de ingressar em um estágio é adiquirir conhecimento e aprendizado para me tornar o melhor profissional nessa área.{os.linesep}')   
    elif resposta == '2':
        print(f'{os.linesep} {nome}, tenho conhecimentos em linguagem C, Python, domínio na área de montagem de hardware, formatação e instalação de sistemas operacionais como Windows, MAC OS, Linux e montagem de Hackintosh.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep} {nome}, de junho de 2021 até o presente momento, trabalho como atendente de telemarketing. Trabalhei com telefone, chat e atualmente respondo e-mails para uma instituição bancária. {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep} {nome}, concluí meu Ensino Médio em 2019 no Colégio SESI - FESP, atualmente curso TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS na Universidade Cruzeiro do Sul. Parte do meu estudo é concluído com o material disponibilizado pela universidade e estudos feitos através da internet.{os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep} Olá {nome}, meu nome é Erik, tenho 20 anos, sou natural e moro em Curitiba - PR. Atualmente trabalho com telemarketing e sou graduando em Tecnologia em Análise e Desenvolvimento de Sistemas. Sou uma pessoa muito sossegada, gosto de ficar no meu quarto estudando, jogando, ou com a minha família e rodeado das pessoas que eu gosto.{os.linesep}')
    elif resposta == '6':
        print(f'{os.linesep} {nome}, meu maior passatempo tem sido criar projetos como esse em Python, ver outros projetos na internet e me divertir com isso. Também amo sair com a minha namorada e sou atleta de Futebol Americano pela equipe Brown Spiders de Curitiba - PR.{os.linesep}')
    else:
        print('{}Erro: Digite apenas 1, 2, 3, 4, 5, 6 OU 7!{}'.format('\033[31m', '\033[m'))


def start():
    
    # Apresentar o chatbot
    print("Olá, meu nome é Erik. Bem vindo ao Erik Florscuk Chat\n")

    # Pedir nome
    nome = input("\nDigite seu nome: ")

    # Pedir e-mail
    email = input("Digite seu e-mail:")
    
    while True: 
        # Oferecer o menu de opções
        
        resposta = input(f'\nPERGUNTAS FREQUENTES{os.linesep}\n[1] - Por que deve me contratar como seu estagiário?{os.linesep}[2] - Quais são minhas habilidades relacionadas ao trabalho:{os.linesep}[3] - Qual minha experiência profissional?{os.linesep}[4] - Qual minha experiência educacional?{os.linesep}[5] - Sobre mim{os.linesep}[6] - Passatempos{os.linesep}[7] - FECHAR PROGRAMA{os.linesep}\n')
        if resposta == '7':
            break 
        
        else:
            os.system("cls")

        # Processar resposta enviada
        
        processar_resposta(resposta,nome)
        


if __name__ == '__main__':
    start()
    
    