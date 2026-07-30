from crud.imposto import (
    cadastrar_imposto,
    listar_imposto,
    buscar_imposto,
    atualizar_imposto,
    remover_imposto
)
from util.formatacao import cabecalho_menu

def menu_imposto():

    while True:

        cabecalho_menu("MENU IMPOSTOS")

        print("[ 1 ] - Cadastrar Imposto")
        print("[ 2 ] - Listar Impostos")
        print("[ 3 ] - Buscar Imposto")
        print("[ 4 ] - Atualizar Imposto")
        print("[ 5 ] - Remover Imposto")
        print("[ 0 ] - Voltar")

        opcao = input("\n➤ Escolha uma opção: ")


        if opcao == "1":

            cadastrar_imposto()


        elif opcao == "2":

            listar_imposto()


        elif opcao == "3":

            buscar_imposto()


        elif opcao == "4":

            atualizar_imposto()


        elif opcao == "5":

            remover_imposto()


        elif opcao == "0":

            print("\nVoltando ao menu fiscal...")
            break


        else:

            print("\nOpção inválida! Tente novamente.")