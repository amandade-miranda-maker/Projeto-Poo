from database.database import conectar


def cadastrar_centro_custo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        codigo = input("Código do centro de custo: ")
        nome = input("Nome do centro de custo: ")

        id_pai = input("ID do centro de custo pai (Enter para deixar vazio): ")

        if id_pai == "":
            id_pai = None
        else:
            id_pai = int(id_pai)

        status = input("Status (Ativo/Inativo): ")

        sql = """
            INSERT INTO centro_custo
            (
                id_empresa_centro_custo,
                codigo_centro_custo,
                nome_centro_custo,
                id_centro_custo_pai_centro_custo,
                status_centro_custo
            )
            VALUES
            (%s,%s,%s,%s,%s)
        """

        valores = (
            id_empresa,
            codigo,
            nome,
            id_pai,
            status
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nCentro de custo cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar centro de custo: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def listar_centro_custo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_centro_custo,
                id_empresa_centro_custo,
                codigo_centro_custo,
                nome_centro_custo,
                id_centro_custo_pai_centro_custo,
                status_centro_custo
            FROM centro_custo
            ORDER BY id_centro_custo
        """

        cursor.execute(sql)

        centros = cursor.fetchall()

        if not centros:

            print("\nNenhum centro de custo encontrado.")

        else:

            print("\n========== CENTROS DE CUSTO ==========")

            for centro in centros:

                print(f"""
ID......................: {centro[0]}
ID Empresa..............: {centro[1]}
Código..................: {centro[2]}
Nome....................: {centro[3]}
Centro Pai..............: {centro[4]}
Status..................: {centro[5]}
""")

    except Exception as erro:

        print(f"\nErro ao listar centros de custo: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_centro_custo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_centro = int(input("Informe o ID do centro de custo: "))

        sql = """
            SELECT
                id_centro_custo,
                id_empresa_centro_custo,
                codigo_centro_custo,
                nome_centro_custo,
                id_centro_custo_pai_centro_custo,
                status_centro_custo
            FROM centro_custo
            WHERE id_centro_custo = %s
        """

        cursor.execute(sql, (id_centro,))

        centro = cursor.fetchone()

        if centro:

            print(f"""
========== CENTRO DE CUSTO ==========

ID......................: {centro[0]}
ID Empresa..............: {centro[1]}
Código..................: {centro[2]}
Nome....................: {centro[3]}
Centro Pai..............: {centro[4]}
Status..................: {centro[5]}
""")

        else:

            print("\nCentro de custo não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar centro de custo: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def atualizar_centro_custo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_centro = int(input("ID do centro de custo: "))

        id_empresa = int(input("Novo ID da empresa: "))
        codigo = input("Novo código: ")
        nome = input("Novo nome: ")

        id_pai = input("Novo ID do centro de custo pai (Enter para deixar vazio): ")

        if id_pai == "":
            id_pai = None
        else:
            id_pai = int(id_pai)

        status = input("Novo status (Ativo/Inativo): ")

        sql = """
            UPDATE centro_custo
            SET
                id_empresa_centro_custo = %s,
                codigo_centro_custo = %s,
                nome_centro_custo = %s,
                id_centro_custo_pai_centro_custo = %s,
                status_centro_custo = %s
            WHERE id_centro_custo = %s
        """

        valores = (
            id_empresa,
            codigo,
            nome,
            id_pai,
            status,
            id_centro
        )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nCentro de custo atualizado com sucesso!")

        else:

            print("\nCentro de custo não encontrado.")

    except Exception as erro:

        print(f"\nErro ao atualizar centro de custo: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_centro_custo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_centro = int(input("ID do centro de custo: "))

        confirmar = input("Deseja realmente remover este centro de custo? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM centro_custo
                WHERE id_centro_custo = %s
            """

            cursor.execute(sql, (id_centro,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nCentro de custo removido com sucesso!")

            else:

                print("\nCentro de custo não encontrado.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover centro de custo: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

