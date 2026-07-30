from util.cores import (
    AZUL_CLARO,
    VERDE,
    AMARELO,
    VERMELHO,
    NEGRITO,
    RESET
)

from crud.guia_pagamento import (
    cadastrar_guia_pagamento,
    listar_guia_pagamento,
    buscar_guia_pagamento,
    atualizar_guia_pagamento,
    remover_guia_pagamento
)


def menu_guia_pagamento():

    while True:

        print(f"{AZUL_CLARO}╭────────────────────────────────────────────╮{RESET}")
        print(f"{AZUL_CLARO}│{RESET} {NEGRITO}{VERDE}      MENU GUIA DE PAGAMENTO{RESET}          {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}├────────────────────────────────────────────┤{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 1 ]{RESET} - Cadastrar Guia                  {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 2 ]{RESET} - Listar Guias                    {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 3 ]{RESET} - Buscar Guia                     {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 4 ]{RESET} - Atualizar Guia                  {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 5 ]{RESET} - Remover Guia                    {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}   {VERMELHO}[ 0 ]{RESET} - Voltar                         {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
        print(f"{AZUL_CLARO}╰────────────────────────────────────────────╯{RESET}")

        opcao = input(f" {NEGRITO}➤ Escolha uma opção:{RESET} ")

        if opcao == "1":

            cadastrar_guia_pagamento()

        elif opcao == "2":

            listar_guia_pagamento()

        elif opcao == "3":

            buscar_guia_pagamento()

        elif opcao == "4":

            atualizar_guia_pagamento()

        elif opcao == "5":

            remover_guia_pagamento()

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida!")