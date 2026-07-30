def cabecalho_menu(nome_menu):

    AZUL_CLARO = '\033[94m'
    VERDE = '\033[92m'
    RESET = '\033[0m'
    NEGRITO = '\033[1m'

    print(f"\n{AZUL_CLARO}╭────────────────────────────────────────────╮{RESET}")
    print(f"{AZUL_CLARO}│{RESET} {NEGRITO}{VERDE}{nome_menu:^40}{RESET} {AZUL_CLARO}│{RESET}")
    print(f"{AZUL_CLARO}╰────────────────────────────────────────────╯{RESET}")