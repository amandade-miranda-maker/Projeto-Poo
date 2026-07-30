from database.database import conectar


def cadastrar_lancamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        data_lancamento = input("Data do lançamento (AAAA-MM-DD): ")
        competencia = input("Competência (AAAA-MM): ")
        historico = input("Histórico geral: ")

        id_documento = input("ID do documento fiscal (Enter para deixar vazio): ")

        if id_documento == "":
            id_documento = None
        else:
            id_documento = int(id_documento)

        tipo_origem = input("Tipo de origem (Manual/Fiscal): ")

        id_colaborador = input("ID do colaborador responsável (Enter para deixar vazio): ")

        if id_colaborador == "":
            id_colaborador = None
        else:
            id_colaborador = int(id_colaborador)

        sql = """
            INSERT INTO lancamento
            (
                id_empresa_lancamento,
                data_lancamento,
                competencia_lancamento,
                historico_geral_lancamento,
                id_documento_fiscal_origem_lancamento,
                tipo_origem_lancamento,
                id_colaborador_resp_lancamento
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (
            id_empresa,
            data_lancamento,
            competencia,
            historico,
            id_documento,
            tipo_origem,
            id_colaborador
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nLançamento cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar lançamento: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def listar_lancamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_lancamento,
                id_empresa_lancamento,
                data_lancamento,
                competencia_lancamento,
                historico_geral_lancamento,
                id_documento_fiscal_origem_lancamento,
                tipo_origem_lancamento,
                id_colaborador_resp_lancamento
            FROM lancamento
            ORDER BY id_lancamento
        """

        cursor.execute(sql)

        lancamentos = cursor.fetchall()

        if not lancamentos:

            print("\nNenhum lançamento encontrado.")

        else:

            print("\n========== LANÇAMENTOS ==========")

            for lancamento in lancamentos:

                print(f"""
ID......................: {lancamento[0]}
ID Empresa..............: {lancamento[1]}
Data....................: {lancamento[2]}
Competência.............: {lancamento[3]}
Histórico...............: {lancamento[4]}
ID Documento............: {lancamento[5]}
Tipo de Origem..........: {lancamento[6]}
ID Colaborador..........: {lancamento[7]}
""")

    except Exception as erro:

        print(f"\nErro ao listar lançamentos: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_lancamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_lancamento = int(input("Informe o ID do lançamento: "))

        sql = """
            SELECT
                id_lancamento,
                id_empresa_lancamento,
                data_lancamento,
                competencia_lancamento,
                historico_geral_lancamento,
                id_documento_fiscal_origem_lancamento,
                tipo_origem_lancamento,
                id_colaborador_resp_lancamento
            FROM lancamento
            WHERE id_lancamento = %s
        """

        cursor.execute(sql, (id_lancamento,))

        lancamento = cursor.fetchone()

        if lancamento:

            print(f"""
========== LANÇAMENTO ==========

ID......................: {lancamento[0]}
ID Empresa..............: {lancamento[1]}
Data....................: {lancamento[2]}
Competência.............: {lancamento[3]}
Histórico...............: {lancamento[4]}
ID Documento............: {lancamento[5]}
Tipo de Origem..........: {lancamento[6]}
ID Colaborador..........: {lancamento[7]}
""")

        else:

            print("\nLançamento não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar lançamento: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def atualizar_lancamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_lancamento = int(input("ID do lançamento: "))

        id_empresa = int(input("Novo ID da empresa: "))
        data_lancamento = input("Nova data (AAAA-MM-DD): ")
        competencia = input("Nova competência (AAAA-MM): ")
        historico = input("Novo histórico: ")

        id_documento = input("Novo ID do documento fiscal (Enter para deixar vazio): ")

        if id_documento == "":
            id_documento = None
        else:
            id_documento = int(id_documento)

        tipo_origem = input("Novo tipo de origem: ")

        id_colaborador = input("Novo ID do colaborador responsável (Enter para deixar vazio): ")

        if id_colaborador == "":
            id_colaborador = None
        else:
            id_colaborador = int(id_colaborador)

        sql = """
            UPDATE lancamento
            SET
                id_empresa_lancamento = %s,
                data_lancamento = %s,
                competencia_lancamento = %s,
                historico_geral_lancamento = %s,
                id_documento_fiscal_origem_lancamento = %s,
                tipo_origem_lancamento = %s,
                id_colaborador_resp_lancamento = %s
            WHERE id_lancamento = %s
        """

        valores = (
            id_empresa,
            data_lancamento,
            competencia,
            historico,
            id_documento,
            tipo_origem,
            id_colaborador,
            id_lancamento
        )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nLançamento atualizado com sucesso!")

        else:

            print("\nLançamento não encontrado.")

    except Exception as erro:

        print(f"\nErro ao atualizar lançamento: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_lancamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_lancamento = int(input("ID do lançamento: "))

        confirmar = input("Deseja realmente remover este lançamento? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM lancamento
                WHERE id_lancamento = %s
            """

            cursor.execute(sql, (id_lancamento,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nLançamento removido com sucesso!")

            else:

                print("\nLançamento não encontrado.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover lançamento: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()