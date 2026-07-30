from util.cores import (
    AZUL_CLARO,
    VERDE,
    AMARELO,
    VERMELHO,
    NEGRITO,
    RESET
)

from crud.cargo import (
    cadastrar_cargo,
    listar_cargo,
    buscar_cargo,
    atualizar_cargo,
    remover_cargo
)


def menu_cargo():

    while True:

        print(f"{AZUL_CLARO}╭────────────────────────────────────────────╮{RESET}")
        print(f"{AZUL_CLARO}│{RESET} {NEGRITO}{VERDE}             MENU CARGOS{RESET}                  {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}├────────────────────────────────────────────┤{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 1 ]{RESET} - Cadastrar Cargo                 {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 2 ]{RESET} - Listar Cargos                   {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 3 ]{RESET} - Buscar Cargo                    {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 4 ]{RESET} - Atualizar Cargo                 {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 5 ]{RESET} - Remover Cargo                   {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {VERMELHO}[ 0 ]{RESET} - Voltar                          {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}╰────────────────────────────────────────────╯{RESET}")

        opcao = input(f" {NEGRITO}➤ Escolha uma opção:{RESET} ")

        if opcao == "1":
            cadastrar_cargo()

        elif opcao == "2":
            listar_cargo()

        elif opcao == "3":
            buscar_cargo()

        elif opcao == "4":
            atualizar_cargo()

        elif opcao == "5":
            remover_cargo()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida!")