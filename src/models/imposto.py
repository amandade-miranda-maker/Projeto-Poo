from database.database import conectar


def exibir_imposto(imposto):

    print(f"""
========================================
ID................: {imposto[0]}
Nome..............: {imposto[1]}
Esfera............: {imposto[2]}
Alíquota..........: {imposto[3]}
Status............: {imposto[4]}
========================================
""")


def cadastrar_imposto():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        nome = input("Nome do imposto: ")
        esfera = input("Esfera (Federal/Estadual/Municipal): ")
        aliquota = input("Alíquota padrão: ")
        status = input("Status (Ativo/Inativo): ")

        if aliquota == "":
            aliquota = None


        sql = """
            INSERT INTO imposto
            (
                nome_imposto,
                esfera_imposto,
                aliquota_padrao_imposto,
                status_imposto
            )
            VALUES
            (%s,%s,%s,%s)
        """


        cursor.execute(sql, (
            nome,
            esfera,
            aliquota,
            status
        ))


        conexao.commit()

        print("\nImposto cadastrado com sucesso!")


    except Exception as erro:

        print(f"\nErro ao cadastrar imposto: {erro}")


    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()



def listar_imposto():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()


        sql = """
            SELECT
                id_imposto,
                nome_imposto,
                esfera_imposto,
                aliquota_padrao_imposto,
                status_imposto
            FROM imposto
            ORDER BY nome_imposto
        """


        cursor.execute(sql)

        impostos = cursor.fetchall()


        if not impostos:

            print("\nNenhum imposto encontrado.")


        else:

            print("\n========== IMPOSTOS CADASTRADOS ==========")

            for imposto in impostos:

                exibir_imposto(imposto)



    except Exception as erro:

        print(f"\nErro ao listar impostos: {erro}")


    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()



def buscar_imposto():

    conexao = None
    cursor = None


    try:

        conexao = conectar()
        cursor = conexao.cursor()


        id_imposto = int(input("Informe o ID do imposto: "))


        sql = """
            SELECT
                id_imposto,
                nome_imposto,
                esfera_imposto,
                aliquota_padrao_imposto,
                status_imposto
            FROM imposto
            WHERE id_imposto = %s
        """


        cursor.execute(sql, (id_imposto,))


        imposto = cursor.fetchone()


        if imposto:

            print("\n========== IMPOSTO ENCONTRADO ==========")

            exibir_imposto(imposto)


        else:

            print("\nImposto não encontrado.")



    except Exception as erro:

        print(f"\nErro ao buscar imposto: {erro}")


    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()



def atualizar_imposto():

    conexao = None
    cursor = None


    try:

        conexao = conectar()
        cursor = conexao.cursor()


        id_imposto = int(input("Informe o ID do imposto: "))


        sql = """
            SELECT
                id_imposto,
                nome_imposto,
                esfera_imposto,
                aliquota_padrao_imposto,
                status_imposto
            FROM imposto
            WHERE id_imposto = %s
        """


        cursor.execute(sql, (id_imposto,))


        imposto = cursor.fetchone()


        if not imposto:

            print("\nImposto não encontrado.")
            return


        print("\n========== IMPOSTO ATUAL ==========")

        exibir_imposto(imposto)



        nome = input("Novo nome: ")
        esfera = input("Nova esfera: ")
        aliquota = input("Nova alíquota: ")
        status = input("Novo status: ")



        if aliquota == "":
            aliquota = None



        sql = """
            UPDATE imposto
            SET
                nome_imposto = %s,
                esfera_imposto = %s,
                aliquota_padrao_imposto = %s,
                status_imposto = %s
            WHERE id_imposto = %s
        """


        cursor.execute(sql, (
            nome,
            esfera,
            aliquota,
            status,
            id_imposto
        ))


        conexao.commit()


        print("\nImposto atualizado com sucesso!")



    except Exception as erro:

        print(f"\nErro ao atualizar imposto: {erro}")


    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()



def remover_imposto():

    conexao = None
    cursor = None


    try:

        conexao = conectar()
        cursor = conexao.cursor()


        id_imposto = int(input("Informe o ID do imposto: "))


        sql = """
            SELECT
                id_imposto,
                nome_imposto,
                esfera_imposto,
                aliquota_padrao_imposto,
                status_imposto
            FROM imposto
            WHERE id_imposto = %s
        """


        cursor.execute(sql, (id_imposto,))


        imposto = cursor.fetchone()


        if not imposto:

            print("\nImposto não encontrado.")
            return


        print("\n========== IMPOSTO A SER REMOVIDO ==========")

        exibir_imposto(imposto)



        confirmar = input(
            "Deseja realmente remover este imposto? (S/N): "
        ).upper()



        if confirmar == "S":


            sql = """
                DELETE FROM imposto
                WHERE id_imposto = %s
            """


            cursor.execute(sql, (id_imposto,))

            conexao.commit()


            print("\nImposto removido com sucesso!")


        else:

            print("\nOperação cancelada.")



    except Exception as erro:

        print(f"\nErro ao remover imposto: {erro}")


    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()