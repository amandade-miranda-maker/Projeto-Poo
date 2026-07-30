from database.database import conectar


def cadastrar_conta_pagar():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        fornecedor = input("Fornecedor: ")
        cnpj_cpf = input("CNPJ/CPF do fornecedor: ")
        descricao = input("Descrição: ")
        valor_original = input("Valor original: ")
        valor_pago = input("Valor pago (Enter para nenhum): ")
        data_emissao = input("Data de emissão (AAAA-MM-DD): ")
        data_vencimento = input("Data de vencimento (AAAA-MM-DD): ")
        data_pagamento = input("Data de pagamento (AAAA-MM-DD ou Enter): ")
        id_conta_bancaria = input("ID da conta bancária (Enter para nenhum): ")
        id_documento_fiscal = input("ID do documento fiscal (Enter para nenhum): ")
        status = input("Status (Pendente/Pago/Atrasado/Cancelado): ")

        if cnpj_cpf == "":
            cnpj_cpf = None

        if valor_pago == "":
            valor_pago = None

        if data_pagamento == "":
            data_pagamento = None

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
            INSERT INTO conta_pagar
            (
                id_empresa_conta_pagar,
                fornecedor_conta_pagar,
                cnpj_cpf_fornecedor_conta_pagar,
                descricao_conta_pagar,
                valor_original_conta_pagar,
                valor_pago_conta_pagar,
                data_emissao_conta_pagar,
                data_vencimento_conta_pagar,
                data_pagamento_conta_pagar,
                id_conta_bancaria_conta_pagar,
                id_documento_fiscal_conta_pagar,
                status_conta_pagar
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, (
            id_empresa,
            fornecedor,
            cnpj_cpf,
            descricao,
            valor_original,
            valor_pago,
            data_emissao,
            data_vencimento,
            data_pagamento,
            id_conta_bancaria,
            id_documento_fiscal,
            status
        ))

        conexao.commit()

        print("\nConta a pagar cadastrada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar conta a pagar: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_conta_pagar():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                cp.id_conta_pagar,
                e.razao_social_empresa,
                cp.fornecedor_conta_pagar,
                cp.descricao_conta_pagar,
                cp.valor_original_conta_pagar,
                cp.valor_pago_conta_pagar,
                cp.data_emissao_conta_pagar,
                cp.data_vencimento_conta_pagar,
                cp.data_pagamento_conta_pagar,
                cp.status_conta_pagar
            FROM conta_pagar cp
            INNER JOIN empresa e
                ON e.id_empresa = cp.id_empresa_conta_pagar
            ORDER BY
                cp.data_vencimento_conta_pagar,
                cp.id_conta_pagar
        """

        cursor.execute(sql)

        contas = cursor.fetchall()

        if not contas:

            print("\nNenhuma conta a pagar encontrada.")

        else:

            print("\n========== CONTAS A PAGAR ==========")

            for conta in contas:

                data_pagamento = (
                    conta[8].strftime("%d/%m/%Y")
                    if conta[8]
                    else "Não realizado"
                )

                valor_pago = (
                    f"R$ {conta[5]:.2f}"
                    if conta[5] is not None
                    else "Não informado"
                )

                print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Fornecedor........: {conta[2]}
Descrição.........: {conta[3]}
Valor Original....: R$ {conta[4]:.2f}
Valor Pago........: {valor_pago}
Emissão...........: {conta[6].strftime("%d/%m/%Y")}
Vencimento........: {conta[7].strftime("%d/%m/%Y")}
Pagamento.........: {data_pagamento}
Status............: {conta[9]}
========================================
""")

    except Exception as erro:

        print(f"\nErro ao listar contas a pagar: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_conta_pagar():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_pagar = int(input("Informe o ID da conta a pagar: "))

        sql = """
            SELECT
                cp.id_conta_pagar,
                e.razao_social_empresa,
                cp.fornecedor_conta_pagar,
                cp.descricao_conta_pagar,
                cp.valor_original_conta_pagar,
                cp.valor_pago_conta_pagar,
                cp.data_emissao_conta_pagar,
                cp.data_vencimento_conta_pagar,
                cp.data_pagamento_conta_pagar,
                cp.status_conta_pagar
            FROM conta_pagar cp
            INNER JOIN empresa e
                ON e.id_empresa = cp.id_empresa_conta_pagar
            WHERE cp.id_conta_pagar = %s
        """

        cursor.execute(sql, (id_conta_pagar,))

        conta = cursor.fetchone()

        if conta:

            data_pagamento = (
                conta[8].strftime("%d/%m/%Y")
                if conta[8]
                else "Não realizado"
            )

            valor_pago = (
                f"R$ {conta[5]:.2f}"
                if conta[5] is not None
                else "Não informado"
            )

            print("\n========== CONTA A PAGAR ENCONTRADA ==========")

            print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Fornecedor........: {conta[2]}
Descrição.........: {conta[3]}
Valor Original....: R$ {conta[4]:.2f}
Valor Pago........: {valor_pago}
Emissão...........: {conta[6].strftime("%d/%m/%Y")}
Vencimento........: {conta[7].strftime("%d/%m/%Y")}
Pagamento.........: {data_pagamento}
Status............: {conta[9]}
========================================
""")

        else:

            print("\nConta a pagar não encontrada.")

    except Exception as erro:

        print(f"\nErro ao buscar conta a pagar: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_conta_pagar():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_pagar = int(input("Informe o ID da conta a pagar: "))

        sql = """
            SELECT
                cp.id_conta_pagar,
                e.razao_social_empresa,
                cp.fornecedor_conta_pagar,
                cp.descricao_conta_pagar,
                cp.valor_original_conta_pagar,
                cp.valor_pago_conta_pagar,
                cp.data_emissao_conta_pagar,
                cp.data_vencimento_conta_pagar,
                cp.data_pagamento_conta_pagar,
                cp.status_conta_pagar
            FROM conta_pagar cp
            INNER JOIN empresa e
                ON e.id_empresa = cp.id_empresa_conta_pagar
            WHERE cp.id_conta_pagar = %s
        """

        cursor.execute(sql, (id_conta_pagar,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta a pagar não encontrada.")
            return

        print("\n========== CONTA A PAGAR ATUAL ==========")

        data_pagamento = (
            conta[8].strftime("%d/%m/%Y")
            if conta[8]
            else "Não realizado"
        )

        valor_pago = (
            f"R$ {conta[5]:.2f}"
            if conta[5] is not None
            else "Não informado"
        )

        print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Fornecedor........: {conta[2]}
Descrição.........: {conta[3]}
Valor Original....: R$ {conta[4]:.2f}
Valor Pago........: {valor_pago}
Emissão...........: {conta[6].strftime("%d/%m/%Y")}
Vencimento........: {conta[7].strftime("%d/%m/%Y")}
Pagamento.........: {data_pagamento}
Status............: {conta[9]}
========================================
""")

        id_empresa = int(input("Novo ID da empresa: "))
        fornecedor = input("Novo fornecedor: ")
        cnpj_cpf = input("Novo CNPJ/CPF: ")
        descricao = input("Nova descrição: ")
        valor_original = input("Novo valor original: ")
        valor_pago = input("Novo valor pago (Enter para nenhum): ")
        data_emissao = input("Nova data de emissão (AAAA-MM-DD): ")
        data_vencimento = input("Nova data de vencimento (AAAA-MM-DD): ")
        data_pagamento = input("Nova data de pagamento (AAAA-MM-DD ou Enter): ")
        id_conta_bancaria = input("Novo ID da conta bancária (Enter para nenhum): ")
        id_documento_fiscal = input("Novo ID do documento fiscal (Enter para nenhum): ")
        status = input("Novo status (Pendente/Pago/Atrasado/Cancelado): ")

        if cnpj_cpf == "":
            cnpj_cpf = None

        if valor_pago == "":
            valor_pago = None

        if data_pagamento == "":
            data_pagamento = None

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
            UPDATE conta_pagar
            SET
                id_empresa_conta_pagar = %s,
                fornecedor_conta_pagar = %s,
                cnpj_cpf_fornecedor_conta_pagar = %s,
                descricao_conta_pagar = %s,
                valor_original_conta_pagar = %s,
                valor_pago_conta_pagar = %s,
                data_emissao_conta_pagar = %s,
                data_vencimento_conta_pagar = %s,
                data_pagamento_conta_pagar = %s,
                id_conta_bancaria_conta_pagar = %s,
                id_documento_fiscal_conta_pagar = %s,
                status_conta_pagar = %s
            WHERE id_conta_pagar = %s
        """

        cursor.execute(sql, (
            id_empresa,
            fornecedor,
            cnpj_cpf,
            descricao,
            valor_original,
            valor_pago,
            data_emissao,
            data_vencimento,
            data_pagamento,
            id_conta_bancaria,
            id_documento_fiscal,
            status,
            id_conta_pagar
        ))

        conexao.commit()

        print("\nConta a pagar atualizada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao atualizar conta a pagar: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_conta_pagar():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_conta_pagar = int(input("Informe o ID da conta a pagar: "))

        sql = """
            SELECT
                cp.id_conta_pagar,
                e.razao_social_empresa,
                cp.fornecedor_conta_pagar,
                cp.descricao_conta_pagar,
                cp.valor_original_conta_pagar,
                cp.valor_pago_conta_pagar,
                cp.data_emissao_conta_pagar,
                cp.data_vencimento_conta_pagar,
                cp.data_pagamento_conta_pagar,
                cp.status_conta_pagar
            FROM conta_pagar cp
            INNER JOIN empresa e
                ON e.id_empresa = cp.id_empresa_conta_pagar
            WHERE cp.id_conta_pagar = %s
        """

        cursor.execute(sql, (id_conta_pagar,))

        conta = cursor.fetchone()

        if not conta:

            print("\nConta a pagar não encontrada.")
            return

        data_pagamento = (
            conta[8].strftime("%d/%m/%Y")
            if conta[8]
            else "Não realizado"
        )

        valor_pago = (
            f"R$ {conta[5]:.2f}"
            if conta[5] is not None
            else "Não informado"
        )

        print("\n========== CONTA A PAGAR A SER REMOVIDA ==========")

        print(f"""
========================================
ID................: {conta[0]}
Empresa...........: {conta[1]}
Fornecedor........: {conta[2]}
Descrição.........: {conta[3]}
Valor Original....: R$ {conta[4]:.2f}
Valor Pago........: {valor_pago}
Emissão...........: {conta[6].strftime("%d/%m/%Y")}
Vencimento........: {conta[7].strftime("%d/%m/%Y")}
Pagamento.........: {data_pagamento}
Status............: {conta[9]}
========================================
""")

        confirmar = input("Deseja realmente remover esta conta a pagar? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM conta_pagar
                WHERE id_conta_pagar = %s
            """

            cursor.execute(sql, (id_conta_pagar,))
            conexao.commit()

            print("\nConta a pagar removida com sucesso!")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover conta a pagar: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()