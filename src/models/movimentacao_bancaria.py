from database.database import conectar


def cadastrar_movimentacao_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_bancaria = int(input("ID da conta bancária: "))
        data_movimentacao = input("Data da movimentação (AAAA-MM-DD): ")
        tipo_movimentacao = input("Tipo (D/C): ")
        valor = input("Valor: ")
        descricao = input("Descrição: ")
        documento_referencia = input("Documento de referência (Enter para nenhum): ")
        conciliado = input("Conciliado (True/False): ")
        id_lancamento = input("ID do lançamento (Enter para nenhum): ")

        if documento_referencia == "":
            documento_referencia = None

        if id_lancamento == "":
            id_lancamento = None
        else:
            id_lancamento = int(id_lancamento)

        sql = """
            SELECT
                id_conta_bancaria,
                banco_conta_bancaria,
                numero_conta_conta_bancaria
            FROM conta_bancaria
            WHERE id_conta_bancaria = %s
        """

        cursor.execute(sql, (id_conta_bancaria,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta bancária não encontrada.")
            return

        print(f"\nConta selecionada: {conta[1]} - {conta[2]}")

        if id_lancamento is not None:

            sql = """
                SELECT
                    id_lancamento
                FROM lancamento
                WHERE id_lancamento = %s
            """

            cursor.execute(sql, (id_lancamento,))

            lancamento = cursor.fetchone()

            if not lancamento:

                print("\nLançamento não encontrado.")
                return

        sql = """
            INSERT INTO movimentacao_bancaria
            (
                id_conta_bancaria_movimentacao_bancaria,
                data_movimentacao_bancaria,
                tipo_movimentacao_bancaria,
                valor_movimentacao_bancaria,
                descricao_movimentacao_bancaria,
                documento_referencia_movimentacao_bancaria,
                conciliado_movimentacao_bancaria,
                id_lancamento_movimentacao_bancaria
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, (
            id_conta_bancaria,
            data_movimentacao,
            tipo_movimentacao,
            valor,
            descricao,
            documento_referencia,
            conciliado,
            id_lancamento
        ))

        conexao.commit()

        print("\nMovimentação bancária cadastrada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar movimentação bancária: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_movimentacao_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                mb.id_movimentacao_bancaria,
                cb.banco_conta_bancaria,
                cb.numero_conta_conta_bancaria,
                mb.data_movimentacao_bancaria,
                mb.tipo_movimentacao_bancaria,
                mb.valor_movimentacao_bancaria,
                mb.descricao_movimentacao_bancaria,
                mb.documento_referencia_movimentacao_bancaria,
                mb.conciliado_movimentacao_bancaria,
                mb.id_lancamento_movimentacao_bancaria
            FROM movimentacao_bancaria mb
            INNER JOIN conta_bancaria cb
                ON cb.id_conta_bancaria = mb.id_conta_bancaria_movimentacao_bancaria
            ORDER BY
                mb.data_movimentacao_bancaria DESC,
                mb.id_movimentacao_bancaria
        """

        cursor.execute(sql)

        movimentacoes = cursor.fetchall()

        if not movimentacoes:

            print("\nNenhuma movimentação bancária encontrada.")

        else:

            print("\n========== MOVIMENTAÇÕES BANCÁRIAS ==========")

            for movimentacao in movimentacoes:

                print(f"""
========================================
ID................: {movimentacao[0]}
Banco.............: {movimentacao[1]}
Conta.............: {movimentacao[2]}
Data..............: {movimentacao[3].strftime("%d/%m/%Y")}
Tipo..............: {movimentacao[4]}
Valor.............: R$ {movimentacao[5]:.2f}
Descrição.........: {movimentacao[6]}
Documento.........: {movimentacao[7]}
Conciliado........: {movimentacao[8]}
ID Lançamento.....: {movimentacao[9]}
========================================
""")

    except Exception as erro:

        print(f"\nErro ao listar movimentações bancárias: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_movimentacao_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_movimentacao_bancaria = int(input("Informe o ID da movimentação bancária: "))

        sql = """
            SELECT
                mb.id_movimentacao_bancaria,
                cb.banco_conta_bancaria,
                cb.numero_conta_conta_bancaria,
                mb.data_movimentacao_bancaria,
                mb.tipo_movimentacao_bancaria,
                mb.valor_movimentacao_bancaria,
                mb.descricao_movimentacao_bancaria,
                mb.documento_referencia_movimentacao_bancaria,
                mb.conciliado_movimentacao_bancaria,
                mb.id_lancamento_movimentacao_bancaria
            FROM movimentacao_bancaria mb
            INNER JOIN conta_bancaria cb
                ON cb.id_conta_bancaria = mb.id_conta_bancaria_movimentacao_bancaria
            WHERE mb.id_movimentacao_bancaria = %s
        """

        cursor.execute(sql, (id_movimentacao_bancaria,))

        movimentacao = cursor.fetchone()

        if movimentacao:

            print("\n========== MOVIMENTAÇÃO BANCÁRIA ENCONTRADA ==========")

            print(f"""
========================================
ID................: {movimentacao[0]}
Banco.............: {movimentacao[1]}
Conta.............: {movimentacao[2]}
Data..............: {movimentacao[3].strftime("%d/%m/%Y")}
Tipo..............: {movimentacao[4]}
Valor.............: R$ {movimentacao[5]:.2f}
Descrição.........: {movimentacao[6]}
Documento.........: {movimentacao[7]}
Conciliado........: {movimentacao[8]}
ID Lançamento.....: {movimentacao[9]}
========================================
""")

        else:

            print("\nMovimentação bancária não encontrada.")

    except Exception as erro:

        print(f"\nErro ao buscar movimentação bancária: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_movimentacao_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_movimentacao_bancaria = int(input("Informe o ID da movimentação bancária: "))

        sql = """
            SELECT
                mb.id_movimentacao_bancaria,
                cb.banco_conta_bancaria,
                cb.numero_conta_conta_bancaria,
                mb.data_movimentacao_bancaria,
                mb.tipo_movimentacao_bancaria,
                mb.valor_movimentacao_bancaria,
                mb.descricao_movimentacao_bancaria,
                mb.documento_referencia_movimentacao_bancaria,
                mb.conciliado_movimentacao_bancaria,
                mb.id_lancamento_movimentacao_bancaria
            FROM movimentacao_bancaria mb
            INNER JOIN conta_bancaria cb
                ON cb.id_conta_bancaria = mb.id_conta_bancaria_movimentacao_bancaria
            WHERE mb.id_movimentacao_bancaria = %s
        """

        cursor.execute(sql, (id_movimentacao_bancaria,))

        movimentacao = cursor.fetchone()

        if not movimentacao:

            print("\nMovimentação bancária não encontrada.")
            return

        print("\n========== MOVIMENTAÇÃO BANCÁRIA ATUAL ==========")

        print(f"""
========================================
ID................: {movimentacao[0]}
Banco.............: {movimentacao[1]}
Conta.............: {movimentacao[2]}
Data..............: {movimentacao[3].strftime("%d/%m/%Y")}
Tipo..............: {movimentacao[4]}
Valor.............: R$ {movimentacao[5]:.2f}
Descrição.........: {movimentacao[6]}
Documento.........: {movimentacao[7]}
Conciliado........: {movimentacao[8]}
ID Lançamento.....: {movimentacao[9]}
========================================
""")

        id_conta_bancaria = int(input("Novo ID da conta bancária: "))
        data_movimentacao = input("Nova data (AAAA-MM-DD): ")
        tipo_movimentacao = input("Novo tipo (D/C): ")
        valor = input("Novo valor: ")
        descricao = input("Nova descrição: ")
        documento_referencia = input("Novo documento de referência (Enter para nenhum): ")
        conciliado = input("Conciliado (True/False): ")
        id_lancamento = input("Novo ID do lançamento (Enter para nenhum): ")

        if documento_referencia == "":
            documento_referencia = None

        if id_lancamento == "":
            id_lancamento = None
        else:
            id_lancamento = int(id_lancamento)

        sql = """
            SELECT
                id_conta_bancaria,
                banco_conta_bancaria,
                numero_conta_conta_bancaria
            FROM conta_bancaria
            WHERE id_conta_bancaria = %s
        """

        cursor.execute(sql, (id_conta_bancaria,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta bancária não encontrada.")
            return

        print(f"\nConta selecionada: {conta[1]} - {conta[2]}")

        if id_lancamento is not None:

            sql = """
                SELECT
                    id_lancamento
                FROM lancamento
                WHERE id_lancamento = %s
            """

            cursor.execute(sql, (id_lancamento,))

            lancamento = cursor.fetchone()

            if not lancamento:

                print("\nLançamento não encontrado.")
                return

        sql = """
            UPDATE movimentacao_bancaria
            SET
                id_conta_bancaria_movimentacao_bancaria = %s,
                data_movimentacao_bancaria = %s,
                tipo_movimentacao_bancaria = %s,
                valor_movimentacao_bancaria = %s,
                descricao_movimentacao_bancaria = %s,
                documento_referencia_movimentacao_bancaria = %s,
                conciliado_movimentacao_bancaria = %s,
                id_lancamento_movimentacao_bancaria = %s
            WHERE id_movimentacao_bancaria = %s
        """

        cursor.execute(sql, (
            id_conta_bancaria,
            data_movimentacao,
            tipo_movimentacao,
            valor,
            descricao,
            documento_referencia,
            conciliado,
            id_lancamento,
            id_movimentacao_bancaria
        ))

        conexao.commit()

        print("\nMovimentação bancária atualizada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao atualizar movimentação bancária: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_movimentacao_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_movimentacao_bancaria = int(input("Informe o ID da movimentação bancária: "))

        sql = """
            SELECT
                mb.id_movimentacao_bancaria,
                cb.banco_conta_bancaria,
                cb.numero_conta_conta_bancaria,
                mb.data_movimentacao_bancaria,
                mb.tipo_movimentacao_bancaria,
                mb.valor_movimentacao_bancaria,
                mb.descricao_movimentacao_bancaria,
                mb.documento_referencia_movimentacao_bancaria,
                mb.conciliado_movimentacao_bancaria,
                mb.id_lancamento_movimentacao_bancaria
            FROM movimentacao_bancaria mb
            INNER JOIN conta_bancaria cb
                ON cb.id_conta_bancaria = mb.id_conta_bancaria_movimentacao_bancaria
            WHERE mb.id_movimentacao_bancaria = %s
        """

        cursor.execute(sql, (id_movimentacao_bancaria,))

        movimentacao = cursor.fetchone()

        if not movimentacao:

            print("\nMovimentação bancária não encontrada.")
            return

        print("\n========== MOVIMENTAÇÃO BANCÁRIA A SER REMOVIDA ==========")

        print(f"""
========================================
ID................: {movimentacao[0]}
Banco.............: {movimentacao[1]}
Conta.............: {movimentacao[2]}
Data..............: {movimentacao[3].strftime("%d/%m/%Y")}
Tipo..............: {movimentacao[4]}
Valor.............: R$ {movimentacao[5]:.2f}
Descrição.........: {movimentacao[6]}
Documento.........: {movimentacao[7]}
Conciliado........: {movimentacao[8]}
ID Lançamento.....: {movimentacao[9]}
========================================
""")

        confirmar = input("Deseja realmente remover esta movimentação bancária? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM movimentacao_bancaria
                WHERE id_movimentacao_bancaria = %s
            """

            cursor.execute(sql, (id_movimentacao_bancaria,))
            conexao.commit()

            print("\nMovimentação bancária removida com sucesso!")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover movimentação bancária: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()