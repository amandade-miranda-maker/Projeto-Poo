from database.database import conectar


def cadastrar_guia_pagamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_cronograma = int(input("ID do cronograma tributário: "))
        codigo_barras = input("Código de barras: ")
        linha_digitavel = input("Linha digitável: ")
        data_emissao = input("Data de emissão (AAAA-MM-DD): ")
        data_vencimento = input("Data de vencimento (AAAA-MM-DD): ")
        valor = float(input("Valor da guia: "))

        arquivo = input("Arquivo da guia (Enter para deixar vazio): ")

        if arquivo == "":
            arquivo = None

        status = input("Status (Emitida/Paga/Vencida/Cancelada): ")

        sql = """
            INSERT INTO guia_pagamento
            (
                id_cronograma_tributario_guia_pagamento,
                codigo_barras_guia_pagamento,
                linha_digitavel_guia_pagamento,
                data_emissao_guia_pagamento,
                data_vencimento_guia_pagamento,
                valor_guia_pagamento,
                arquivo_guia_pagamento,
                status_guia_pagamento
            )
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            id_cronograma,
            codigo_barras,
            linha_digitavel,
            data_emissao,
            data_vencimento,
            valor,
            arquivo,
            status
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nGuia de pagamento cadastrada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar guia de pagamento: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_guia_pagamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_guia_pagamento,
                id_cronograma_tributario_guia_pagamento,
                codigo_barras_guia_pagamento,
                data_vencimento_guia_pagamento,
                valor_guia_pagamento,
                status_guia_pagamento
            FROM guia_pagamento
            ORDER BY id_guia_pagamento
        """

        cursor.execute(sql)

        guias = cursor.fetchall()

        if not guias:

            print("\nNenhuma guia de pagamento encontrada.")

        else:

            print("\n========== GUIAS DE PAGAMENTO ==========")

            for guia in guias:

                print(f"""
ID......................: {guia[0]}
ID Cronograma...........: {guia[1]}
Código de Barras........: {guia[2]}
Data de Vencimento......: {guia[3]}
Valor...................: R$ {guia[4]:.2f}
Status..................: {guia[5]}
""")

    except Exception as erro:

        print(f"\nErro ao listar guias de pagamento: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()
def buscar_guia_pagamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_guia = int(input("Informe o ID da guia de pagamento: "))

        sql = """
            SELECT
                id_guia_pagamento,
                id_cronograma_tributario_guia_pagamento,
                codigo_barras_guia_pagamento,
                linha_digitavel_guia_pagamento,
                data_emissao_guia_pagamento,
                data_vencimento_guia_pagamento,
                valor_guia_pagamento,
                arquivo_guia_pagamento,
                status_guia_pagamento
            FROM guia_pagamento
            WHERE id_guia_pagamento = %s
        """

        cursor.execute(sql, (id_guia,))

        guia = cursor.fetchone()

        if guia:

            print(f"""
========== GUIA DE PAGAMENTO ==========

ID......................: {guia[0]}
ID Cronograma...........: {guia[1]}
Código de Barras........: {guia[2]}
Linha Digitável.........: {guia[3]}
Data de Emissão.........: {guia[4]}
Data de Vencimento......: {guia[5]}
Valor...................: R$ {guia[6]:.2f}
Arquivo.................: {guia[7]}
Status..................: {guia[8]}
""")

        else:

            print("\nGuia de pagamento não encontrada.")

    except Exception as erro:

        print(f"\nErro ao buscar guia de pagamento: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_guia_pagamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_guia = int(input("ID da guia de pagamento: "))

        id_cronograma = int(input("Novo ID do cronograma tributário: "))
        codigo_barras = input("Novo código de barras: ")
        linha_digitavel = input("Nova linha digitável: ")
        data_emissao = input("Nova data de emissão (AAAA-MM-DD): ")
        data_vencimento = input("Nova data de vencimento (AAAA-MM-DD): ")
        valor = float(input("Novo valor da guia: "))

        arquivo = input("Novo arquivo da guia (Enter para deixar vazio): ")

        if arquivo == "":
            arquivo = None

        status = input("Novo status (Emitida/Paga/Vencida/Cancelada): ")

        sql = """
            UPDATE guia_pagamento
            SET
                id_cronograma_tributario_guia_pagamento = %s,
                codigo_barras_guia_pagamento = %s,
                linha_digitavel_guia_pagamento = %s,
                data_emissao_guia_pagamento = %s,
                data_vencimento_guia_pagamento = %s,
                valor_guia_pagamento = %s,
                arquivo_guia_pagamento = %s,
                status_guia_pagamento = %s
            WHERE id_guia_pagamento = %s
        """

        valores = (
            id_cronograma,
            codigo_barras,
            linha_digitavel,
            data_emissao,
            data_vencimento,
            valor,
            arquivo,
            status,
            id_guia
        )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nGuia de pagamento atualizada com sucesso!")

        else:

            print("\nGuia de pagamento não encontrada.")

    except Exception as erro:

        print(f"\nErro ao atualizar guia de pagamento: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_guia_pagamento():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_guia = int(input("ID da guia de pagamento: "))

        confirmar = input("Deseja realmente remover esta guia de pagamento? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM guia_pagamento
                WHERE id_guia_pagamento = %s
            """

            cursor.execute(sql, (id_guia,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nGuia de pagamento removida com sucesso!")

            else:

                print("\nGuia de pagamento não encontrada.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover guia de pagamento: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()
