from database.database import conectar


def cadastrar_saldo_contabil_mensal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        id_conta = int(input("ID da conta: "))
        competencia = input("Competência (AAAA-MM): ")
        saldo_inicial = input("Saldo inicial: ")
        total_debitos = input("Total de débitos: ")
        total_creditos = input("Total de créditos: ")
        saldo_final = input("Saldo final: ")

        sql = """
            SELECT
                id_empresa,
                razao_social_empresa
            FROM empresa
            WHERE id_empresa = %s
        """

        cursor.execute(sql, (id_empresa,))

        empresa = cursor.fetchone()

        if not empresa:

            print("\nEmpresa não encontrada.")
            return

        print(f"\nEmpresa selecionada: {empresa[1]}")

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

        print(f"Conta selecionada: {conta[1]}")

        sql = """
            INSERT INTO saldo_contabil_mensal
            (
                id_empresa_saldo_contabil_mensal,
                id_conta_saldo_contabil_mensal,
                competencia_saldo_contabil_mensal,
                saldo_inicial_saldo_contabil_mensal,
                total_debitos_saldo_contabil_mensal,
                total_creditos_saldo_contabil_mensal,
                saldo_final_saldo_contabil_mensal
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, (
            id_empresa,
            id_conta,
            competencia,
            saldo_inicial,
            total_debitos,
            total_creditos,
            saldo_final
        ))

        conexao.commit()

        print("\nSaldo Contábil Mensal cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar saldo contábil mensal: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_saldo_contabil_mensal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                scm.id_saldo_contabil_mensal,
                e.razao_social_empresa,
                c.nome_conta,
                scm.competencia_saldo_contabil_mensal,
                scm.saldo_inicial_saldo_contabil_mensal,
                scm.total_debitos_saldo_contabil_mensal,
                scm.total_creditos_saldo_contabil_mensal,
                scm.saldo_final_saldo_contabil_mensal
            FROM saldo_contabil_mensal scm
            INNER JOIN empresa e
                ON e.id_empresa = scm.id_empresa_saldo_contabil_mensal
            INNER JOIN conta c
                ON c.id_conta = scm.id_conta_saldo_contabil_mensal
            ORDER BY
                scm.competencia_saldo_contabil_mensal,
                e.razao_social_empresa
        """

        cursor.execute(sql)

        saldos = cursor.fetchall()

        if not saldos:

            print("\nNenhum saldo contábil mensal encontrado.")

        else:

            print("\n========== SALDOS CONTÁBEIS MENSAIS ==========")

            for saldo in saldos:

                print(f"""
========================================
ID................: {saldo[0]}
Empresa...........: {saldo[1]}
Conta.............: {saldo[2]}
Competência.......: {saldo[3]}
Saldo Inicial.....: R$ {saldo[4]:.2f}
Total Débitos.....: R$ {saldo[5]:.2f}
Total Créditos....: R$ {saldo[6]:.2f}
Saldo Final.......: R$ {saldo[7]:.2f}
========================================
""")

    except Exception as erro:

        print(f"\nErro ao listar saldos contábeis mensais: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_saldo_contabil_mensal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_saldo_contabil_mensal = int(input("Informe o ID do saldo contábil mensal: "))

        sql = """
            SELECT
                scm.id_saldo_contabil_mensal,
                e.razao_social_empresa,
                c.nome_conta,
                scm.competencia_saldo_contabil_mensal,
                scm.saldo_inicial_saldo_contabil_mensal,
                scm.total_debitos_saldo_contabil_mensal,
                scm.total_creditos_saldo_contabil_mensal,
                scm.saldo_final_saldo_contabil_mensal
            FROM saldo_contabil_mensal scm
            INNER JOIN empresa e
                ON e.id_empresa = scm.id_empresa_saldo_contabil_mensal
            INNER JOIN conta c
                ON c.id_conta = scm.id_conta_saldo_contabil_mensal
            WHERE scm.id_saldo_contabil_mensal = %s
        """

        cursor.execute(sql, (id_saldo_contabil_mensal,))

        saldo = cursor.fetchone()

        if saldo:

            print("\n========== SALDO CONTÁBIL MENSAL ENCONTRADO ==========")

            print(f"""
========================================
ID................: {saldo[0]}
Empresa...........: {saldo[1]}
Conta.............: {saldo[2]}
Competência.......: {saldo[3]}
Saldo Inicial.....: R$ {saldo[4]:.2f}
Total Débitos.....: R$ {saldo[5]:.2f}
Total Créditos....: R$ {saldo[6]:.2f}
Saldo Final.......: R$ {saldo[7]:.2f}
========================================
""")

        else:

            print("\nSaldo contábil mensal não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar saldo contábil mensal: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_saldo_contabil_mensal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_saldo_contabil_mensal = int(input("Informe o ID do saldo contábil mensal: "))

        sql = """
            SELECT
                scm.id_saldo_contabil_mensal,
                e.razao_social_empresa,
                c.nome_conta,
                scm.competencia_saldo_contabil_mensal,
                scm.saldo_inicial_saldo_contabil_mensal,
                scm.total_debitos_saldo_contabil_mensal,
                scm.total_creditos_saldo_contabil_mensal,
                scm.saldo_final_saldo_contabil_mensal
            FROM saldo_contabil_mensal scm
            INNER JOIN empresa e
                ON e.id_empresa = scm.id_empresa_saldo_contabil_mensal
            INNER JOIN conta c
                ON c.id_conta = scm.id_conta_saldo_contabil_mensal
            WHERE scm.id_saldo_contabil_mensal = %s
        """

        cursor.execute(sql, (id_saldo_contabil_mensal,))

        saldo = cursor.fetchone()

        if not saldo:

            print("\nSaldo contábil mensal não encontrado.")
            return

        print("\n========== SALDO CONTÁBIL MENSAL ATUAL ==========")

        print(f"""
========================================
ID................: {saldo[0]}
Empresa...........: {saldo[1]}
Conta.............: {saldo[2]}
Competência.......: {saldo[3]}
Saldo Inicial.....: R$ {saldo[4]:.2f}
Total Débitos.....: R$ {saldo[5]:.2f}
Total Créditos....: R$ {saldo[6]:.2f}
Saldo Final.......: R$ {saldo[7]:.2f}
========================================
""")

        id_empresa = int(input("Novo ID da empresa: "))
        id_conta = int(input("Novo ID da conta: "))
        competencia = input("Nova competência (AAAA-MM): ")
        saldo_inicial = input("Novo saldo inicial: ")
        total_debitos = input("Novo total de débitos: ")
        total_creditos = input("Novo total de créditos: ")
        saldo_final = input("Novo saldo final: ")

        sql = """
            SELECT
                id_empresa,
                razao_social_empresa
            FROM empresa
            WHERE id_empresa = %s
        """

        cursor.execute(sql, (id_empresa,))

        empresa = cursor.fetchone()

        if not empresa:

            print("\nEmpresa não encontrada.")
            return

        print(f"\nEmpresa selecionada: {empresa[1]}")

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

        print(f"Conta selecionada: {conta[1]}")

        sql = """
            UPDATE saldo_contabil_mensal
            SET
                id_empresa_saldo_contabil_mensal = %s,
                id_conta_saldo_contabil_mensal = %s,
                competencia_saldo_contabil_mensal = %s,
                saldo_inicial_saldo_contabil_mensal = %s,
                total_debitos_saldo_contabil_mensal = %s,
                total_creditos_saldo_contabil_mensal = %s,
                saldo_final_saldo_contabil_mensal = %s
            WHERE id_saldo_contabil_mensal = %s
        """

        cursor.execute(sql, (
            id_empresa,
            id_conta,
            competencia,
            saldo_inicial,
            total_debitos,
            total_creditos,
            saldo_final,
            id_saldo_contabil_mensal
        ))

        conexao.commit()

        print("\nSaldo contábil mensal atualizado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao atualizar saldo contábil mensal: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_saldo_contabil_mensal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_saldo_contabil_mensal = int(input("Informe o ID do saldo contábil mensal: "))

        sql = """
            SELECT
                scm.id_saldo_contabil_mensal,
                e.razao_social_empresa,
                c.nome_conta,
                scm.competencia_saldo_contabil_mensal,
                scm.saldo_inicial_saldo_contabil_mensal,
                scm.total_debitos_saldo_contabil_mensal,
                scm.total_creditos_saldo_contabil_mensal,
                scm.saldo_final_saldo_contabil_mensal
            FROM saldo_contabil_mensal scm
            INNER JOIN empresa e
                ON e.id_empresa = scm.id_empresa_saldo_contabil_mensal
            INNER JOIN conta c
                ON c.id_conta = scm.id_conta_saldo_contabil_mensal
            WHERE scm.id_saldo_contabil_mensal = %s
        """

        cursor.execute(sql, (id_saldo_contabil_mensal,))

        saldo = cursor.fetchone()

        if not saldo:

            print("\nSaldo contábil mensal não encontrado.")
            return

        print("\n========== SALDO CONTÁBIL MENSAL A SER REMOVIDO ==========")

        print(f"""
========================================
ID................: {saldo[0]}
Empresa...........: {saldo[1]}
Conta.............: {saldo[2]}
Competência.......: {saldo[3]}
Saldo Inicial.....: R$ {saldo[4]:.2f}
Total Débitos.....: R$ {saldo[5]:.2f}
Total Créditos....: R$ {saldo[6]:.2f}
Saldo Final.......: R$ {saldo[7]:.2f}
========================================
""")

        confirmar = input("Deseja realmente remover este saldo contábil mensal? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM saldo_contabil_mensal
                WHERE id_saldo_contabil_mensal = %s
            """

            cursor.execute(sql, (id_saldo_contabil_mensal,))
            conexao.commit()

            print("\nSaldo contábil mensal removido com sucesso!")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover saldo contábil mensal: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()