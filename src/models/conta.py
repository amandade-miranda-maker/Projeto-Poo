from database.database import conectar


def cadastrar_conta():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        codigo = input("Código da conta: ")
        nome = input("Nome da conta: ")
        tipo = input("Tipo (Sintética/Analítica): ")

        id_conta_pai = input("ID da conta pai (Enter para deixar vazio): ")

        if id_conta_pai == "":
            id_conta_pai = None
        else:
            id_conta_pai = int(id_conta_pai)

        natureza = input("Natureza (D/C): ")

        sql = """
            INSERT INTO conta
            (
                id_empresa_conta,
                codigo_conta,
                nome_conta,
                tipo_conta,
                id_conta_pai_conta,
                natureza_conta
            )
            VALUES
            (%s,%s,%s,%s,%s,%s)
        """

        valores = (
            id_empresa,
            codigo,
            nome,
            tipo,
            id_conta_pai,
            natureza
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nConta cadastrada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar conta: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def listar_conta():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_conta,
                id_empresa_conta,
                codigo_conta,
                nome_conta,
                tipo_conta,
                id_conta_pai_conta,
                natureza_conta
            FROM conta
            ORDER BY id_conta
        """

        cursor.execute(sql)

        contas = cursor.fetchall()

        if not contas:

            print("\nNenhuma conta encontrada.")

        else:

            print("\n========== CONTAS ==========")

            for conta in contas:

                print(f"""
ID......................: {conta[0]}
ID Empresa..............: {conta[1]}
Código..................: {conta[2]}
Nome....................: {conta[3]}
Tipo....................: {conta[4]}
Conta Pai...............: {conta[5]}
Natureza................: {conta[6]}
""")

    except Exception as erro:

        print(f"\nErro ao listar contas: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_conta():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta = int(input("Informe o ID da conta: "))

        sql = """
            SELECT
                id_conta,
                id_empresa_conta,
                codigo_conta,
                nome_conta,
                tipo_conta,
                id_conta_pai_conta,
                natureza_conta
            FROM conta
            WHERE id_conta = %s
        """

        cursor.execute(sql, (id_conta,))

        conta = cursor.fetchone()

        if conta:

            print(f"""
========== CONTA ==========

ID......................: {conta[0]}
ID Empresa..............: {conta[1]}
Código..................: {conta[2]}
Nome....................: {conta[3]}
Tipo....................: {conta[4]}
Conta Pai...............: {conta[5]}
Natureza................: {conta[6]}
""")

        else:

            print("\nConta não encontrada.")

    except Exception as erro:

        print(f"\nErro ao buscar conta: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def atualizar_conta():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta = int(input("ID da conta: "))

        id_empresa = int(input("Novo ID da empresa: "))
        codigo = input("Novo código: ")
        nome = input("Novo nome: ")
        tipo = input("Novo tipo (Sintética/Analítica): ")

        id_conta_pai = input("Novo ID da conta pai (Enter para deixar vazio): ")

        if id_conta_pai == "":
            id_conta_pai = None
        else:
            id_conta_pai = int(id_conta_pai)

        natureza = input("Nova natureza (D/C): ")

        sql = """
            UPDATE conta
            SET
                id_empresa_conta = %s,
                codigo_conta = %s,
                nome_conta = %s,
                tipo_conta = %s,
                id_conta_pai_conta = %s,
                natureza_conta = %s
            WHERE id_conta = %s
        """

        valores = (
            id_empresa,
            codigo,
            nome,
            tipo,
            id_conta_pai,
            natureza,
            id_conta
        )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nConta atualizada com sucesso!")

        else:

            print("\nConta não encontrada.")

    except Exception as erro:

        print(f"\nErro ao atualizar conta: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_conta():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta = int(input("ID da conta: "))

        confirmar = input("Deseja realmente remover esta conta? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM conta
                WHERE id_conta = %s
            """

            cursor.execute(sql, (id_conta,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nConta removida com sucesso!")

            else:

                print("\nConta não encontrada.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover conta: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()