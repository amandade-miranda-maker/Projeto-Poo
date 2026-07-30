from database.database import conectar


def cadastrar_conta_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        banco = input("Banco: ")
        codigo_banco = input("Código do banco: ")
        agencia = input("Agência: ")
        numero_conta = input("Número da conta: ")
        tipo_conta = input("Tipo da conta (Corrente/Poupança/Aplicação): ")
        saldo_atual = input("Saldo atual: ")
        status = input("Status (Ativa/Inativa/Encerrada): ")

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
            INSERT INTO conta_bancaria
            (
                id_empresa_conta_bancaria,
                banco_conta_bancaria,
                codigo_banco_conta_bancaria,
                agencia_conta_bancaria,
                numero_conta_conta_bancaria,
                tipo_conta_bancaria,
                saldo_atual_conta_bancaria,
                status_conta_bancaria
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, (
            id_empresa,
            banco,
            codigo_banco,
            agencia,
            numero_conta,
            tipo_conta,
            saldo_atual,
            status
        ))

        conexao.commit()

        print("\nConta bancária cadastrada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar conta bancária: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_conta_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                cb.id_conta_bancaria,
                e.razao_social_empresa,
                cb.banco_conta_bancaria,
                cb.codigo_banco_conta_bancaria,
                cb.agencia_conta_bancaria,
                cb.numero_conta_conta_bancaria,
                cb.tipo_conta_bancaria,
                cb.saldo_atual_conta_bancaria,
                cb.status_conta_bancaria
            FROM conta_bancaria cb
            INNER JOIN empresa e
                ON e.id_empresa = cb.id_empresa_conta_bancaria
            ORDER BY
                e.razao_social_empresa,
                cb.banco_conta_bancaria
        """

        cursor.execute(sql)

        contas = cursor.fetchall()

        if not contas:

            print("\nNenhuma conta bancária encontrada.")

        else:

            print("\n========== CONTAS BANCÁRIAS ==========")

            for conta in contas:

                print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Banco.............: {conta[2]}
Código Banco......: {conta[3]}
Agência...........: {conta[4]}
Número Conta......: {conta[5]}
Tipo Conta........: {conta[6]}
Saldo Atual.......: R$ {conta[7]:.2f}
Status............: {conta[8]}
========================================
""")

    except Exception as erro:

        print(f"\nErro ao listar contas bancárias: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_conta_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_bancaria = int(input("Informe o ID da conta bancária: "))

        sql = """
            SELECT
                cb.id_conta_bancaria,
                e.razao_social_empresa,
                cb.banco_conta_bancaria,
                cb.codigo_banco_conta_bancaria,
                cb.agencia_conta_bancaria,
                cb.numero_conta_conta_bancaria,
                cb.tipo_conta_bancaria,
                cb.saldo_atual_conta_bancaria,
                cb.status_conta_bancaria
            FROM conta_bancaria cb
            INNER JOIN empresa e
                ON e.id_empresa = cb.id_empresa_conta_bancaria
            WHERE cb.id_conta_bancaria = %s
        """

        cursor.execute(sql, (id_conta_bancaria,))

        conta = cursor.fetchone()

        if conta:

            print("\n========== CONTA BANCÁRIA ENCONTRADA ==========")

            print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Banco.............: {conta[2]}
Código Banco......: {conta[3]}
Agência...........: {conta[4]}
Número Conta......: {conta[5]}
Tipo Conta........: {conta[6]}
Saldo Atual.......: R$ {conta[7]:.2f}
Status............: {conta[8]}
========================================
""")

        else:

            print("\nConta bancária não encontrada.")

    except Exception as erro:

        print(f"\nErro ao buscar conta bancária: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_conta_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_bancaria = int(input("Informe o ID da conta bancária: "))

        sql = """
            SELECT
                cb.id_conta_bancaria,
                e.razao_social_empresa,
                cb.banco_conta_bancaria,
                cb.codigo_banco_conta_bancaria,
                cb.agencia_conta_bancaria,
                cb.numero_conta_conta_bancaria,
                cb.tipo_conta_bancaria,
                cb.saldo_atual_conta_bancaria,
                cb.status_conta_bancaria
            FROM conta_bancaria cb
            INNER JOIN empresa e
                ON e.id_empresa = cb.id_empresa_conta_bancaria
            WHERE cb.id_conta_bancaria = %s
        """

        cursor.execute(sql, (id_conta_bancaria,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta bancária não encontrada.")
            return

        print("\n========== CONTA BANCÁRIA ATUAL ==========")

        print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Banco.............: {conta[2]}
Código Banco......: {conta[3]}
Agência...........: {conta[4]}
Número Conta......: {conta[5]}
Tipo Conta........: {conta[6]}
Saldo Atual.......: R$ {conta[7]:.2f}
Status............: {conta[8]}
========================================
""")

        id_empresa = int(input("Novo ID da empresa: "))
        banco = input("Novo banco: ")
        codigo_banco = input("Novo código do banco: ")
        agencia = input("Nova agência: ")
        numero_conta = input("Novo número da conta: ")
        tipo_conta = input("Novo tipo da conta (Corrente/Poupança/Aplicação): ")
        saldo_atual = input("Novo saldo atual: ")
        status = input("Novo status (Ativa/Inativa/Encerrada): ")

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
            UPDATE conta_bancaria
            SET
                id_empresa_conta_bancaria = %s,
                banco_conta_bancaria = %s,
                codigo_banco_conta_bancaria = %s,
                agencia_conta_bancaria = %s,
                numero_conta_conta_bancaria = %s,
                tipo_conta_bancaria = %s,
                saldo_atual_conta_bancaria = %s,
                status_conta_bancaria = %s
            WHERE id_conta_bancaria = %s
        """

        cursor.execute(sql, (
            id_empresa,
            banco,
            codigo_banco,
            agencia,
            numero_conta,
            tipo_conta,
            saldo_atual,
            status,
            id_conta_bancaria
        ))

        conexao.commit()

        print("\nConta bancária atualizada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao atualizar conta bancária: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_conta_bancaria():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_bancaria = int(input("Informe o ID da conta bancária: "))

        sql = """
            SELECT
                cb.id_conta_bancaria,
                e.razao_social_empresa,
                cb.banco_conta_bancaria,
                cb.codigo_banco_conta_bancaria,
                cb.agencia_conta_bancaria,
                cb.numero_conta_conta_bancaria,
                cb.tipo_conta_bancaria,
                cb.saldo_atual_conta_bancaria,
                cb.status_conta_bancaria
            FROM conta_bancaria cb
            INNER JOIN empresa e
                ON e.id_empresa = cb.id_empresa_conta_bancaria
            WHERE cb.id_conta_bancaria = %s
        """

        cursor.execute(sql, (id_conta_bancaria,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta bancária não encontrada.")
            return

        print("\n========== CONTA BANCÁRIA A SER REMOVIDA ==========")

        print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Banco.............: {conta[2]}
Código Banco......: {conta[3]}
Agência...........: {conta[4]}
Número Conta......: {conta[5]}
Tipo Conta........: {conta[6]}
Saldo Atual.......: R$ {conta[7]:.2f}
Status............: {conta[8]}
========================================
""")

        confirmar = input("Deseja realmente remover esta conta bancária? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM conta_bancaria
                WHERE id_conta_bancaria = %s
            """

            cursor.execute(sql, (id_conta_bancaria,))
            conexao.commit()

            print("\nConta bancária removida com sucesso!")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover conta bancária: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()