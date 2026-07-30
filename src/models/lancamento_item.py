from database.database import conectar


def cadastrar_lancamento_item():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_lancamento = int(input("ID do lançamento: "))
        id_conta = int(input("ID da conta: "))

        centro = input("ID do centro de custo (Enter para nenhum): ")

        if centro == "":
            id_centro_custo = None
        else:
            id_centro_custo = int(centro)

        tipo = input("Tipo do movimento (D/C): ").upper()
        valor = input("Valor: ")

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
            SELECT
                id_conta,
                nome_conta
            FROM conta
            WHERE id_conta = %s
        """

        cursor.execute(sql, (id_conta,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta não encontrada.")
            return

        print(f"\nConta selecionada: {conta[1]}")

        if id_centro_custo:

            sql = """
                SELECT
                    id_centro_custo,
                    nome_centro_custo
                FROM centro_custo
                WHERE id_centro_custo = %s
            """

            cursor.execute(sql, (id_centro_custo,))

            centro_custo = cursor.fetchone()

            if not centro_custo:

                print("\nCentro de custo não encontrado.")
                return

            print(f"Centro de custo: {centro_custo[1]}")

        sql = """
            INSERT INTO lancamento_item
            (
                id_lancamento_lancamento_item,
                id_conta_lancamento_item,
                id_centro_custo_lancamento_item,
                tipo_movimento_lancamento_item,
                valor_lancamento_item
            )
            VALUES
            (%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, (
            id_lancamento,
            id_conta,
            id_centro_custo,
            tipo,
            valor
        ))

        conexao.commit()

        print("\nLançamento Item cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar lançamento item: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_lancamento_item():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                li.id_lancamento_item,
                l.id_lancamento,
                c.nome_conta,
                cc.nome_centro_custo,
                li.tipo_movimento_lancamento_item,
                li.valor_lancamento_item
            FROM lancamento_item li
            INNER JOIN lancamento l
                ON l.id_lancamento = li.id_lancamento_lancamento_item
            INNER JOIN conta c
                ON c.id_conta = li.id_conta_lancamento_item
            LEFT JOIN centro_custo cc
                ON cc.id_centro_custo = li.id_centro_custo_lancamento_item
            ORDER BY li.id_lancamento_item
        """

        cursor.execute(sql)

        lancamentos_item = cursor.fetchall()

        if not lancamentos_item:

            print("\nNenhum lançamento item encontrado.")

        else:

            print("\n========== LANÇAMENTOS ITEM CADASTRADOS ==========")

            for item in lancamentos_item:

                print(f"""
========================================
ID................: {item[0]}
Lançamento........: {item[1]}
Conta.............: {item[2]}
Centro de Custo...: {item[3] if item[3] else "Não informado"}
Tipo..............: {"Débito" if item[4] == "D" else "Crédito"}
Valor.............: R$ {item[5]:.2f}
========================================
""")

    except Exception as erro:

        print(f"\nErro ao listar lançamento item: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_lancamento_item():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_lancamento_item = int(input("Informe o ID do lançamento item: "))

        sql = """
            SELECT
                li.id_lancamento_item,
                l.id_lancamento,
                c.nome_conta,
                cc.nome_centro_custo,
                li.tipo_movimento_lancamento_item,
                li.valor_lancamento_item
            FROM lancamento_item li
            INNER JOIN lancamento l
                ON l.id_lancamento = li.id_lancamento_lancamento_item
            INNER JOIN conta c
                ON c.id_conta = li.id_conta_lancamento_item
            LEFT JOIN centro_custo cc
                ON cc.id_centro_custo = li.id_centro_custo_lancamento_item
            WHERE li.id_lancamento_item = %s
        """

        cursor.execute(sql, (id_lancamento_item,))

        item = cursor.fetchone()

        if item:

            print("\n========== LANÇAMENTO ITEM ENCONTRADO ==========")

            print(f"""
========================================
ID................: {item[0]}
Lançamento........: {item[1]}
Conta.............: {item[2]}
Centro de Custo...: {item[3] if item[3] else "Não informado"}
Tipo..............: {"Débito" if item[4] == "D" else "Crédito"}
Valor.............: R$ {item[5]:.2f}
========================================
""")

        else:

            print("\nLançamento Item não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar lançamento item: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_lancamento_item():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_lancamento_item = int(input("Informe o ID do lançamento item: "))

        sql = """
            SELECT
                li.id_lancamento_item,
                l.id_lancamento,
                c.nome_conta,
                cc.nome_centro_custo,
                li.tipo_movimento_lancamento_item,
                li.valor_lancamento_item
            FROM lancamento_item li
            INNER JOIN lancamento l
                ON l.id_lancamento = li.id_lancamento_lancamento_item
            INNER JOIN conta c
                ON c.id_conta = li.id_conta_lancamento_item
            LEFT JOIN centro_custo cc
                ON cc.id_centro_custo = li.id_centro_custo_lancamento_item
            WHERE li.id_lancamento_item = %s
        """

        cursor.execute(sql, (id_lancamento_item,))

        item = cursor.fetchone()

        if not item:

            print("\nLançamento Item não encontrado.")
            return

        print("\n========== LANÇAMENTO ITEM ATUAL ==========")

        print(f"""
========================================
ID................: {item[0]}
Lançamento........: {item[1]}
Conta.............: {item[2]}
Centro de Custo...: {item[3] if item[3] else "Não informado"}
Tipo..............: {"Débito" if item[4] == "D" else "Crédito"}
Valor.............: R$ {item[5]:.2f}
========================================
""")

        id_lancamento = int(input("Novo ID do lançamento: "))
        id_conta = int(input("Novo ID da conta: "))

        centro = input("Novo ID do centro de custo (Enter para nenhum): ")

        if centro == "":
            id_centro_custo = None
        else:
            id_centro_custo = int(centro)

        tipo = input("Novo tipo (D/C): ").upper()
        valor = input("Novo valor: ")

        sql = """
            SELECT
                id_lancamento
            FROM lancamento
            WHERE id_lancamento = %s
        """

        cursor.execute(sql, (id_lancamento,))

        if not cursor.fetchone():

            print("\nLançamento não encontrado.")
            return

        sql = """
            SELECT
                id_conta,
                nome_conta
            FROM conta
            WHERE id_conta = %s
        """

        cursor.execute(sql, (id_conta,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta não encontrada.")
            return

        print(f"\nConta selecionada: {conta[1]}")

        if id_centro_custo:

            sql = """
                SELECT
                    id_centro_custo,
                    nome_centro_custo
                FROM centro_custo
                WHERE id_centro_custo = %s
            """

            cursor.execute(sql, (id_centro_custo,))

            centro_custo = cursor.fetchone()

            if not centro_custo:

                print("\nCentro de custo não encontrado.")
                return

            print(f"Centro de custo: {centro_custo[1]}")

        sql = """
            UPDATE lancamento_item
            SET
                id_lancamento_lancamento_item = %s,
                id_conta_lancamento_item = %s,
                id_centro_custo_lancamento_item = %s,
                tipo_movimento_lancamento_item = %s,
                valor_lancamento_item = %s
            WHERE id_lancamento_item = %s
        """

        cursor.execute(sql, (
            id_lancamento,
            id_conta,
            id_centro_custo,
            tipo,
            valor,
            id_lancamento_item
        ))

        conexao.commit()

        print("\nLançamento Item atualizado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao atualizar lançamento item: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_lancamento_item():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_lancamento_item = int(input("Informe o ID do lançamento item: "))

        sql = """
            SELECT
                li.id_lancamento_item,
                l.id_lancamento,
                c.nome_conta,
                cc.nome_centro_custo,
                li.tipo_movimento_lancamento_item,
                li.valor_lancamento_item
            FROM lancamento_item li
            INNER JOIN lancamento l
                ON l.id_lancamento = li.id_lancamento_lancamento_item
            INNER JOIN conta c
                ON c.id_conta = li.id_conta_lancamento_item
            LEFT JOIN centro_custo cc
                ON cc.id_centro_custo = li.id_centro_custo_lancamento_item
            WHERE li.id_lancamento_item = %s
        """

        cursor.execute(sql, (id_lancamento_item,))

        item = cursor.fetchone()

        if not item:

            print("\nLançamento Item não encontrado.")
            return

        print("\n========== LANÇAMENTO ITEM A SER REMOVIDO ==========")

        print(f"""
========================================
ID................: {item[0]}
Lançamento........: {item[1]}
Conta.............: {item[2]}
Centro de Custo...: {item[3] if item[3] else "Não informado"}
Tipo..............: {"Débito" if item[4] == "D" else "Crédito"}
Valor.............: R$ {item[5]:.2f}
========================================
""")

        confirmar = input(
            "Deseja realmente remover este lançamento item? (S/N): "
        ).upper()

        if confirmar == "S":

            sql = """
                DELETE FROM lancamento_item
                WHERE id_lancamento_item = %s
            """

            cursor.execute(sql, (id_lancamento_item,))
            conexao.commit()

            print("\nLançamento Item removido com sucesso!")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover lançamento item: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()