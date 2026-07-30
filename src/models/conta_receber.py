from database.database import conectar


def cadastrar_conta_receber():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        cliente = input("Cliente: ")
        cnpj_cpf = input("CNPJ/CPF do cliente: ")
        descricao = input("Descrição: ")
        valor_original = input("Valor original: ")
        valor_recebido = input("Valor recebido (Enter para nenhum): ")
        data_emissao = input("Data de emissão (AAAA-MM-DD): ")
        data_vencimento = input("Data de vencimento (AAAA-MM-DD): ")
        data_recebimento = input("Data de recebimento (AAAA-MM-DD ou Enter): ")
        id_conta_bancaria = input("ID da conta bancária (Enter para nenhum): ")
        id_documento_fiscal = input("ID do documento fiscal (Enter para nenhum): ")
        status = input("Status (Pendente/Recebido/Atrasado/Cancelado): ")

        if cnpj_cpf == "":
            cnpj_cpf = None

        if valor_recebido == "":
            valor_recebido = None

        if data_recebimento == "":
            data_recebimento = None

        if id_conta_bancaria == "":
            id_conta_bancaria = None
        else:
            id_conta_bancaria = int(id_conta_bancaria)

        if id_documento_fiscal == "":
            id_documento_fiscal = None
        else:
            id_documento_fiscal = int(id_documento_fiscal)

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

        if id_conta_bancaria is not None:

            sql = """
                SELECT
                    id_conta_bancaria,
                    banco_conta_bancaria
                FROM conta_bancaria
                WHERE id_conta_bancaria = %s
            """

            cursor.execute(sql, (id_conta_bancaria,))

            conta = cursor.fetchone()

            if not conta:

                print("\nConta bancária não encontrada.")
                return

            print(f"Conta bancária: {conta[1]}")

        if id_documento_fiscal is not None:

            sql = """
                SELECT
                    id_documento_fiscal
                FROM documento_fiscal
                WHERE id_documento_fiscal = %s
            """

            cursor.execute(sql, (id_documento_fiscal,))

            documento = cursor.fetchone()

            if not documento:

                print("\nDocumento fiscal não encontrado.")
                return

        sql = """
            INSERT INTO conta_receber
            (
                id_empresa_conta_receber,
                cliente_conta_receber,
                cnpj_cpf_cliente_conta_receber,
                descricao_conta_receber,
                valor_original_conta_receber,
                valor_recebido_conta_receber,
                data_emissao_conta_receber,
                data_vencimento_conta_receber,
                data_recebimento_conta_receber,
                id_conta_bancaria_conta_receber,
                id_documento_fiscal_conta_receber,
                status_conta_receber
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute((
            sql
        ), (
            id_empresa,
            cliente,
            cnpj_cpf,
            descricao,
            valor_original,
            valor_recebido,
            data_emissao,
            data_vencimento,
            data_recebimento,
            id_conta_bancaria,
            id_documento_fiscal,
            status
        ))

        conexao.commit()

        print("\nConta a receber cadastrada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar conta a receber: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_conta_receber():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                cr.id_conta_receber,
                e.razao_social_empresa,
                cr.cliente_conta_receber,
                cr.descricao_conta_receber,
                cr.valor_original_conta_receber,
                cr.valor_recebido_conta_receber,
                cr.data_emissao_conta_receber,
                cr.data_vencimento_conta_receber,
                cr.data_recebimento_conta_receber,
                cr.status_conta_receber
            FROM conta_receber cr
            INNER JOIN empresa e
                ON e.id_empresa = cr.id_empresa_conta_receber
            ORDER BY
                cr.data_vencimento_conta_receber,
                cr.id_conta_receber
        """

        cursor.execute(sql)

        contas = cursor.fetchall()

        if not contas:

            print("\nNenhuma conta a receber encontrada.")

        else:

            print("\n========== CONTAS A RECEBER ==========")

            for conta in contas:

                data_recebimento = (
                    conta[8].strftime("%d/%m/%Y")
                    if conta[8]
                    else "Não recebido"
                )

                valor_recebido = (
                    f"R$ {conta[5]:.2f}"
                    if conta[5] is not None
                    else "Não informado"
                )

                print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Cliente...........: {conta[2]}
Descrição.........: {conta[3]}
Valor Original....: R$ {conta[4]:.2f}
Valor Recebido....: {valor_recebido}
Emissão...........: {conta[6].strftime("%d/%m/%Y")}
Vencimento........: {conta[7].strftime("%d/%m/%Y")}
Recebimento.......: {data_recebimento}
Status............: {conta[9]}
========================================
""")

    except Exception as erro:

        print(f"\nErro ao listar contas a receber: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_conta_receber():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_receber = int(input("Informe o ID da conta a receber: "))

        sql = """
            SELECT
                cr.id_conta_receber,
                e.razao_social_empresa,
                cr.cliente_conta_receber,
                cr.descricao_conta_receber,
                cr.valor_original_conta_receber,
                cr.valor_recebido_conta_receber,
                cr.data_emissao_conta_receber,
                cr.data_vencimento_conta_receber,
                cr.data_recebimento_conta_receber,
                cr.status_conta_receber
            FROM conta_receber cr
            INNER JOIN empresa e
                ON e.id_empresa = cr.id_empresa_conta_receber
            WHERE cr.id_conta_receber = %s
        """

        cursor.execute(sql, (id_conta_receber,))

        conta = cursor.fetchone()

        if conta:

            data_recebimento = (
                conta[8].strftime("%d/%m/%Y")
                if conta[8]
                else "Não recebido"
            )

            valor_recebido = (
                f"R$ {conta[5]:.2f}"
                if conta[5] is not None
                else "Não informado"
            )

            print("\n========== CONTA A RECEBER ENCONTRADA ==========")

            print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Cliente...........: {conta[2]}
Descrição.........: {conta[3]}
Valor Original....: R$ {conta[4]:.2f}
Valor Recebido....: {valor_recebido}
Emissão...........: {conta[6].strftime("%d/%m/%Y")}
Vencimento........: {conta[7].strftime("%d/%m/%Y")}
Recebimento.......: {data_recebimento}
Status............: {conta[9]}
========================================
""")

        else:

            print("\nConta a receber não encontrada.")

    except Exception as erro:

        print(f"\nErro ao buscar conta a receber: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_conta_receber():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_receber = int(input("Informe o ID da conta a receber: "))

        sql = """
            SELECT
                cr.id_conta_receber,
                e.razao_social_empresa,
                cr.cliente_conta_receber,
                cr.descricao_conta_receber,
                cr.valor_original_conta_receber,
                cr.valor_recebido_conta_receber,
                cr.data_emissao_conta_receber,
                cr.data_vencimento_conta_receber,
                cr.data_recebimento_conta_receber,
                cr.status_conta_receber
            FROM conta_receber cr
            INNER JOIN empresa e
                ON e.id_empresa = cr.id_empresa_conta_receber
            WHERE cr.id_conta_receber = %s
        """

        cursor.execute(sql, (id_conta_receber,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta a receber não encontrada.")
            return

        print("\n========== CONTA A RECEBER ATUAL ==========")

        data_recebimento = (
            conta[8].strftime("%d/%m/%Y")
            if conta[8]
            else "Não recebido"
        )

        valor_recebido = (
            f"R$ {conta[5]:.2f}"
            if conta[5] is not None
            else "Não informado"
        )

        print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Cliente...........: {conta[2]}
Descrição.........: {conta[3]}
Valor Original....: R$ {conta[4]:.2f}
Valor Recebido....: {valor_recebido}
Emissão...........: {conta[6].strftime("%d/%m/%Y")}
Vencimento........: {conta[7].strftime("%d/%m/%Y")}
Recebimento.......: {data_recebimento}
Status............: {conta[9]}
========================================
""")

        id_empresa = int(input("Novo ID da empresa: "))
        cliente = input("Novo cliente: ")
        cnpj_cpf = input("Novo CNPJ/CPF: ")
        descricao = input("Nova descrição: ")
        valor_original = input("Novo valor original: ")
        valor_recebido = input("Novo valor recebido (Enter para nenhum): ")
        data_emissao = input("Nova data de emissão (AAAA-MM-DD): ")
        data_vencimento = input("Nova data de vencimento (AAAA-MM-DD): ")
        data_recebimento = input("Nova data de recebimento (AAAA-MM-DD ou Enter): ")
        id_conta_bancaria = input("Novo ID da conta bancária (Enter para nenhum): ")
        id_documento_fiscal = input("Novo ID do documento fiscal (Enter para nenhum): ")
        status = input("Novo status (Pendente/Recebido/Atrasado/Cancelado): ")

        if cnpj_cpf == "":
            cnpj_cpf = None

        if valor_recebido == "":
            valor_recebido = None

        if data_recebimento == "":
            data_recebimento = None

        if id_conta_bancaria == "":
            id_conta_bancaria = None
        else:
            id_conta_bancaria = int(id_conta_bancaria)

        if id_documento_fiscal == "":
            id_documento_fiscal = None
        else:
            id_documento_fiscal = int(id_documento_fiscal)

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

        if id_conta_bancaria is not None:

            sql = """
                SELECT
                    id_conta_bancaria
                FROM conta_bancaria
                WHERE id_conta_bancaria = %s
            """

            cursor.execute(sql, (id_conta_bancaria,))

            if not cursor.fetchone():

                print("\nConta bancária não encontrada.")
                return

        if id_documento_fiscal is not None:

            sql = """
                SELECT
                    id_documento_fiscal
                FROM documento_fiscal
                WHERE id_documento_fiscal = %s
            """

            cursor.execute(sql, (id_documento_fiscal,))

            if not cursor.fetchone():

                print("\nDocumento fiscal não encontrado.")
                return

        sql = """
            UPDATE conta_receber
            SET
                id_empresa_conta_receber = %s,
                cliente_conta_receber = %s,
                cnpj_cpf_cliente_conta_receber = %s,
                descricao_conta_receber = %s,
                valor_original_conta_receber = %s,
                valor_recebido_conta_receber = %s,
                data_emissao_conta_receber = %s,
                data_vencimento_conta_receber = %s,
                data_recebimento_conta_receber = %s,
                id_conta_bancaria_conta_receber = %s,
                id_documento_fiscal_conta_receber = %s,
                status_conta_receber = %s
            WHERE id_conta_receber = %s
        """

        cursor.execute(sql, (
            id_empresa,
            cliente,
            cnpj_cpf,
            descricao,
            valor_original,
            valor_recebido,
            data_emissao,
            data_vencimento,
            data_recebimento,
            id_conta_bancaria,
            id_documento_fiscal,
            status,
            id_conta_receber
        ))

        conexao.commit()

        print("\nConta a receber atualizada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao atualizar conta a receber: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_conta_receber():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_receber = int(input("Informe o ID da conta a receber: "))

        sql = """
            SELECT
                cr.id_conta_receber,
                e.razao_social_empresa,
                cr.cliente_conta_receber,
                cr.descricao_conta_receber,
                cr.valor_original_conta_receber,
                cr.valor_recebido_conta_receber,
                cr.data_emissao_conta_receber,
                cr.data_vencimento_conta_receber,
                cr.data_recebimento_conta_receber,
                cr.status_conta_receber
            FROM conta_receber cr
            INNER JOIN empresa e
                ON e.id_empresa = cr.id_empresa_conta_receber
            WHERE cr.id_conta_receber = %s
        """

        cursor.execute(sql, (id_conta_receber,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta a receber não encontrada.")
            return

        data_recebimento = (
            conta[8].strftime("%d/%m/%Y")
            if conta[8]
            else "Não recebido"
        )

        valor_recebido = (
            f"R$ {conta[5]:.2f}"
            if conta[5] is not None
            else "Não informado"
        )

        print("\n========== CONTA A RECEBER A SER REMOVIDA ==========")

        print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Cliente...........: {conta[2]}
Descrição.........: {conta[3]}
Valor Original....: R$ {conta[4]:.2f}
Valor Recebido....: {valor_recebido}
Emissão...........: {conta[6].strftime("%d/%m/%Y")}
Vencimento........: {conta[7].strftime("%d/%m/%Y")}
Recebimento.......: {data_recebimento}
Status............: {conta[9]}
========================================
""")

        confirmar = input("Deseja realmente remover esta conta a receber? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM conta_receber
                WHERE id_conta_receber = %s
            """

            cursor.execute(sql, (id_conta_receber,))
            conexao.commit()

            print("\nConta a receber removida com sucesso!")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover conta a receber: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()