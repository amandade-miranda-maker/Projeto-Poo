from util.cores import (
        AZUL_CLARO,
        VERDE,
        AMARELO,
        VERMELHO,
        NEGRITO,
        RESET
    )

from crud.lancamento_item import (
        cadastrar_lancamento_item,
        listar_lancamento_item,
        buscar_lancamento_item,
        atualizar_lancamento_item,
        remover_lancamento_item
    )


def menu_lancamento_item():

        while True:

            print(f"{AZUL_CLARO}╭────────────────────────────────────────────╮{RESET}")
            print(f"{AZUL_CLARO}│{RESET} {NEGRITO}{VERDE}      MENU LANÇAMENTO ITEM{RESET}          {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}├────────────────────────────────────────────┤{RESET}")
            print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 1 ]{RESET} - Cadastrar Lançamento Item     {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 2 ]{RESET} - Listar Lançamentos Item       {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 3 ]{RESET} - Buscar Lançamento Item        {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 4 ]{RESET} - Atualizar Lançamento Item     {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 5 ]{RESET} - Remover Lançamento Item       {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}│{RESET}   {VERMELHO}[ 0 ]{RESET} - Voltar                        {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
            print(f"{AZUL_CLARO}╰────────────────────────────────────────────╯{RESET}")

            opcao = input(f" {NEGRITO}➤ Escolha uma opção:{RESET} ")

            if opcao == "1":

                cadastrar_lancamento_item()

            elif opcao == "2":

                listar_lancamento_item()

            elif opcao == "3":

                buscar_lancamento_item()

            elif opcao == "4":

                atualizar_lancamento_item()

            elif opcao == "5":

                remover_lancamento_item()

            elif opcao == "0":

                break

            else:

                print("\nOpção inválida!")