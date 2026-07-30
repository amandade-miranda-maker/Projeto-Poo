def menu_inove_colorido():

    AZUL_CLARO = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m'

    print(f"{AZUL_CLARO}╭────────────────────────────────────────────╮{RESET}")
    print(f"{AZUL_CLARO}│{RESET} {NEGRITO}{VERDE}          INOVE CONTABILIDADE{RESET}               {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}├────────────────────────────────────────────┤{RESET}")
    print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 1 ]{RESET} - RH                               {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 2 ]{RESET} - Empresas                        {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 3 ]{RESET} - Fiscal                          {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 4 ]{RESET} - Contábil                        {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 5 ]{RESET} - Bancário                      {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 6 ]{RESET} - Financeiro                      {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {AMARELO}[ 7 ]{RESET} - Relatórios                      {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}   {VERMELHO}[ 0 ]{RESET} - Sair                             {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}│{RESET}                                            {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}╰────────────────────────────────────────────╯{RESET}")

    opcao = input(f" {NEGRITO}➤ Escolha uma opção:{RESET} ")

    return opcao