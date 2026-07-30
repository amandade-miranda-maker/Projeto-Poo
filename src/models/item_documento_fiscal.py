from database.database import conectar


def cadastrar_item_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_documento = int(input("ID do documento fiscal: "))
        numero_item = int(input("Número do item: "))
        codigo_produto = input("Código do produto: ")
        descricao_produto = input("Descrição do produto: ")
        ncm = input("NCM: ")
        cfop = input("CFOP: ")
        unidade = input("Unidade: ")
        quantidade = float(input("Quantidade: "))
        valor_unitario = float(input("Valor unitário: "))
        valor_total = float(input("Valor total: "))
        valor_icms = float(input("Valor do ICMS: "))
        valor_ipi = float(input("Valor do IPI: "))

        conta = input("ID da conta (Enter para deixar vazio): ")

        if conta == "":
            conta = None
        else:
            conta = int(conta)

        sql = """
            INSERT INTO item_documento_fiscal
            (
                id_documento_fiscal_item_documento_fiscal,
                numero_item_documento_fiscal,
                codigo_produto_item_documento_fiscal,
                descricao_produto_item_documento_fiscal,
                ncm_item_documento_fiscal,
                cfop_item_documento_fiscal,
                unidade_item_documento_fiscal,
                quantidade_item_documento_fiscal,
                valor_unitario_item_documento_fiscal,
                valor_total_item_documento_fiscal,
                valor_icms_item_documento_fiscal,
                valor_ipi_item_documento_fiscal,
                id_conta_item_documento_fiscal
            )
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            id_documento,
            numero_item,
            codigo_produto,
            descricao_produto,
            ncm,
            cfop,
            unidade,
            quantidade,
            valor_unitario,
            valor_total,
            valor_icms,
            valor_ipi,
            conta
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nItem do documento fiscal cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar item do documento fiscal: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_item_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_item_documento_fiscal,
                id_documento_fiscal_item_documento_fiscal,
                numero_item_documento_fiscal,
                codigo_produto_item_documento_fiscal,
                descricao_produto_item_documento_fiscal,
                quantidade_item_documento_fiscal,
                valor_unitario_item_documento_fiscal,
                valor_total_item_documento_fiscal
            FROM item_documento_fiscal
            ORDER BY id_documento_fiscal_item_documento_fiscal,
                     numero_item_documento_fiscal
        """

        cursor.execute(sql)

        itens = cursor.fetchall()

        if not itens:

            print("\nNenhum item encontrado.")

        else:

            print("\n========== ITENS DOS DOCUMENTOS FISCAIS ==========")

            for item in itens:

                print(f"""
ID..................: {item[0]}
ID Documento........: {item[1]}
Número do Item......: {item[2]}
Código..............: {item[3]}
Produto.............: {item[4]}
Quantidade..........: {item[5]}
Valor Unitário......: R$ {item[6]:.2f}
Valor Total.........: R$ {item[7]:.2f}
""")

    except Exception as erro:

        print(f"\nErro ao listar itens: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_item_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_item = int(input("Informe o ID do item: "))

        sql = """
            SELECT
                id_item_documento_fiscal,
                id_documento_fiscal_item_documento_fiscal,
                numero_item_documento_fiscal,
                codigo_produto_item_documento_fiscal,
                descricao_produto_item_documento_fiscal,
                ncm_item_documento_fiscal,
                cfop_item_documento_fiscal,
                unidade_item_documento_fiscal,
                quantidade_item_documento_fiscal,
                valor_unitario_item_documento_fiscal,
                valor_total_item_documento_fiscal,
                valor_icms_item_documento_fiscal,
                valor_ipi_item_documento_fiscal,
                id_conta_item_documento_fiscal
            FROM item_documento_fiscal
            WHERE id_item_documento_fiscal = %s
        """

        cursor.execute(sql, (id_item,))

        item = cursor.fetchone()

        if item:

            print(f"""
========== ITEM DO DOCUMENTO FISCAL ==========

ID..................: {item[0]}
ID Documento........: {item[1]}
Número do Item......: {item[2]}
Código..............: {item[3]}
Descrição...........: {item[4]}
NCM.................: {item[5]}
CFOP................: {item[6]}
Unidade.............: {item[7]}
Quantidade..........: {item[8]}
Valor Unitário......: R$ {item[9]:.2f}
Valor Total.........: R$ {item[10]:.2f}
Valor ICMS..........: R$ {item[11]:.2f}
Valor IPI...........: R$ {item[12]:.2f}
ID Conta............: {item[13]}
""")

        else:

            print("\nItem não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar item: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_item_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_item = int(input("ID do item: "))

        id_documento = int(input("Novo ID do documento fiscal: "))
        numero_item = int(input("Novo número do item: "))
        codigo_produto = input("Novo código do produto: ")
        descricao_produto = input("Nova descrição do produto: ")
        ncm = input("Novo NCM: ")
        cfop = input("Novo CFOP: ")
        unidade = input("Nova unidade: ")
        quantidade = float(input("Nova quantidade: "))
        valor_unitario = float(input("Novo valor unitário: "))
        valor_total = float(input("Novo valor total: "))
        valor_icms = float(input("Novo valor do ICMS: "))
        valor_ipi = float(input("Novo valor do IPI: "))

        conta = input("Novo ID da conta (Enter para deixar vazio): ")

        if conta == "":
            conta = None
        else:
            conta = int(conta)

        sql = """
            UPDATE item_documento_fiscal
            SET
                id_documento_fiscal_item_documento_fiscal = %s,
                numero_item_documento_fiscal = %s,
                codigo_produto_item_documento_fiscal = %s,
                descricao_produto_item_documento_fiscal = %s,
                ncm_item_documento_fiscal = %s,
                cfop_item_documento_fiscal = %s,
                unidade_item_documento_fiscal = %s,
                quantidade_item_documento_fiscal = %s,
                valor_unitario_item_documento_fiscal = %s,
                valor_total_item_documento_fiscal = %s,
                valor_icms_item_documento_fiscal = %s,
                valor_ipi_item_documento_fiscal = %s,
                id_conta_item_documento_fiscal = %s
            WHERE id_item_documento_fiscal = %s
        """

        valores = (
            id_documento,
            numero_item,
            codigo_produto,
            descricao_produto,
            ncm,
            cfop,
            unidade,
            quantidade,
            valor_unitario,
            valor_total,
            valor_icms,
            valor_ipi,
            conta,
            id_item
        )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nItem atualizado com sucesso!")

        else:

            print("\nItem não encontrado.")

    except Exception as erro:

        print(f"\nErro ao atualizar item: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_item_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_item = int(input("ID do item: "))

        confirmar = input("Deseja realmente remover este item? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM item_documento_fiscal
                WHERE id_item_documento_fiscal = %s
            """

            cursor.execute(sql, (id_item,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nItem do documento fiscal removido com sucesso!")

            else:

                print("\nItem não encontrado.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover item: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()