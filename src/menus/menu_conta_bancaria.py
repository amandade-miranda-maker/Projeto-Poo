from util.cores import (
    AZUL_CLARO,
    VERDE,
    AMARELO,
    VERMELHO,
    NEGRITO,
    RESET
)

from crud.conta_bancaria import (
    cadastrar_conta_bancaria,
    listar_conta_bancaria,
    buscar_conta_bancaria,
    atualizar_conta_bancaria,
    remover_conta_bancaria
)

def menu_conta_bancaria():

    while True:

        print(f"{AZUL_CLARO}╭────────────────────────────────────────────╮{RESET}")
        print(f"{AZUL_CLARO}│{RESET} {NEGRITO}{VERDE}      MENU CONTA BANCÁRIA{RESET}          {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}├────────────────────────────────────────────┤{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 1 ]{RESET} - Cadastrar Conta Bancária      {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 2 ]{RESET} - Listar Contas Bancárias       {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 3 ]{RESET} - Buscar Conta Bancária         {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 4 ]{RESET} - Atualizar Conta Bancária      {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 5 ]{RESET} - Remover Conta Bancária        {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {VERMELHO}[ 0 ]{RESET} - Voltar                        {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}╰────────────────────────────────────────────╯{RESET}")

        opcao = input(f" {NEGRITO}➤ Escolha uma opção:{RESET} ")

        if opcao == "1":

            cadastrar_conta_bancaria()

        elif opcao == "2":

            listar_conta_bancaria()

        elif opcao == "3":

            buscar_conta_bancaria()

        elif opcao == "4":

            atualizar_conta_bancaria()

        elif opcao == "5":

            remover_conta_bancaria()

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida!")