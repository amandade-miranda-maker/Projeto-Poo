from util.cores import (
    AZUL_CLARO,
    VERDE,
    AMARELO,
    VERMELHO,
    NEGRITO,
    RESET
)

from menus.menu_conta import menu_conta
from menus.menu_centro_custo import menu_centro_custo
from menus.menu_lancamento import menu_lancamento
from menus.menu_lancamento_item import menu_lancamento_item
from menus.menu_saldo_contmensal import menu_saldo_contmensal

def menu_contabil():

    while True:

        print(f"{AZUL_CLARO}╭────────────────────────────────────────────╮{RESET}")
        print(f"{AZUL_CLARO}│{RESET} {NEGRITO}{VERDE}          MÓDULO CONTÁBIL{RESET}                {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}├────────────────────────────────────────────┤{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 1 ]{RESET} - Contas                        {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 2 ]{RESET} - Centro de Custos                        {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 3 ]{RESET} - Lançamentos                          {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 4 ]{RESET} - Itens de Lançamento           {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 5 ]{RESET} - Saldos Contábeis Mensais          {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {VERMELHO}[ 0 ]{RESET} - Voltar                          {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}╰────────────────────────────────────────────╯{RESET}")

        opcao = input(f" {NEGRITO}➤ Escolha uma opção:{RESET} ")

        if opcao == "1":

            menu_conta()

        elif opcao == "2":

            menu_centro_custo()

        elif opcao == "3":

            menu_lancamento()

        elif opcao == "4":

            menu_lancamento_item()

        elif opcao == "5":

            menu_saldo_contmensal()

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida!")