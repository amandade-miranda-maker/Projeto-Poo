from database.database import conectar


def cadastrar_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        tipo = input("Tipo do documento: ")
        direcao = input("Direção (E/S): ").upper()
        numero = int(input("Número do documento: "))
        serie = input("Série: ")
        chave = input("Chave de acesso (44 dígitos): ")
        data_emissao = input("Data de emissão (AAAA-MM-DD HH:MM:SS): ")
        cfop = input("CFOP: ")
        natureza = input("Natureza da operação: ")

        valor_produtos = float(input("Valor dos produtos: "))
        valor_frete = float(input("Valor do frete: "))
        valor_desconto = float(input("Valor do desconto: "))
        valor_icms = float(input("Valor do ICMS: "))
        valor_ipi = float(input("Valor do IPI: "))
        valor_pis = float(input("Valor do PIS: "))
        valor_cofins = float(input("Valor do COFINS: "))
        valor_total = float(input("Valor total: "))

        status = input("Status (Autorizado/Cancelado/Inutilizado): ")

        arquivo_xml = input("Caminho do XML: ")
        arquivo_pdf = input("Caminho do DANFE (PDF): ")

        nome_contraparte = input("Nome da contraparte: ")
        cnpj_cpf = input("CNPJ/CPF da contraparte: ")

        sql = """
            INSERT INTO documento_fiscal
            (
                id_empresa_documento_fiscal,
                tipo_documento_fiscal,
                direcao_documento_fiscal,
                numero_documento_fiscal,
                serie_documento_fiscal,
                chave_acesso_documento_fiscal,
                data_emissao_documento_fiscal,
                cfop_documento_fiscal,
                natureza_operacao_documento_fiscal,
                valor_produtos_documento_fiscal,
                valor_frete_documento_fiscal,
                valor_desconto_documento_fiscal,
                valor_icms_documento_fiscal,
                valor_ipi_documento_fiscal,
                valor_pis_documento_fiscal,
                valor_cofins_documento_fiscal,
                valor_total_documento_fiscal,
                status_documento_fiscal,
                arquivo_xml_documento_fiscal,
                arquivo_danfe_pdf_documento_fiscal,
                nome_contraparte_documento_fiscal,
                cnpj_cpf_contraparte_documento_fiscal
            )
            VALUES
            (
                %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s
            )
        """

        valores = (
            id_empresa,
            tipo,
            direcao,
            numero,
            serie,
            chave,
            data_emissao,
            cfop,
            natureza,
            valor_produtos,
            valor_frete,
            valor_desconto,
            valor_icms,
            valor_ipi,
            valor_pis,
            valor_cofins,
            valor_total,
            status,
            arquivo_xml,
            arquivo_pdf,
            nome_contraparte,
            cnpj_cpf
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nDocumento fiscal cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar documento fiscal: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def listar_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_documento_fiscal,
                id_empresa_documento_fiscal,
                tipo_documento_fiscal,
                direcao_documento_fiscal,
                numero_documento_fiscal,
                serie_documento_fiscal,
                data_emissao_documento_fiscal,
                valor_total_documento_fiscal,
                status_documento_fiscal,
                nome_contraparte_documento_fiscal,
                cnpj_cpf_contraparte_documento_fiscal
            FROM documento_fiscal
            ORDER BY id_documento_fiscal
        """

        cursor.execute(sql)

        documentos = cursor.fetchall()

        if not documentos:

            print("\nNenhum documento fiscal encontrado.")

        else:

            print("\n========== DOCUMENTOS FISCAIS CADASTRADOS ==========")

            for documento in documentos:

                print(f"""
ID......................: {documento[0]}
ID Empresa..............: {documento[1]}
Tipo....................: {documento[2]}
Direção.................: {documento[3]}
Número..................: {documento[4]}
Série...................: {documento[5]}
Data de Emissão.........: {documento[6]}
Valor Total.............: R$ {documento[7]:.2f}
Status..................: {documento[8]}
Contraparte.............: {documento[9]}
CNPJ/CPF................: {documento[10]}
""")

    except Exception as erro:

        print(f"\nErro ao listar documentos fiscais: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_documento = int(input("Informe o ID do documento fiscal: "))

        sql = """
            SELECT
                id_documento_fiscal,
                id_empresa_documento_fiscal,
                tipo_documento_fiscal,
                direcao_documento_fiscal,
                numero_documento_fiscal,
                serie_documento_fiscal,
                chave_acesso_documento_fiscal,
                data_emissao_documento_fiscal,
                cfop_documento_fiscal,
                natureza_operacao_documento_fiscal,
                valor_produtos_documento_fiscal,
                valor_frete_documento_fiscal,
                valor_desconto_documento_fiscal,
                valor_icms_documento_fiscal,
                valor_ipi_documento_fiscal,
                valor_pis_documento_fiscal,
                valor_cofins_documento_fiscal,
                valor_total_documento_fiscal,
                status_documento_fiscal,
                arquivo_xml_documento_fiscal,
                arquivo_danfe_pdf_documento_fiscal,
                nome_contraparte_documento_fiscal,
                cnpj_cpf_contraparte_documento_fiscal
            FROM documento_fiscal
            WHERE id_documento_fiscal = %s
        """

        cursor.execute(sql, (id_documento,))

        documento = cursor.fetchone()

        if documento:

            print(f"""
========== DOCUMENTO FISCAL ENCONTRADO ==========

ID......................: {documento[0]}
ID Empresa..............: {documento[1]}
Tipo....................: {documento[2]}
Direção.................: {documento[3]}
Número..................: {documento[4]}
Série...................: {documento[5]}
Chave de Acesso.........: {documento[6]}
Data de Emissão.........: {documento[7]}
CFOP....................: {documento[8]}
Natureza da Operação....: {documento[9]}
Valor Produtos..........: R$ {documento[10]:.2f}
Valor Frete.............: R$ {documento[11]:.2f}
Valor Desconto..........: R$ {documento[12]:.2f}
Valor ICMS..............: R$ {documento[13]:.2f}
Valor IPI...............: R$ {documento[14]:.2f}
Valor PIS...............: R$ {documento[15]:.2f}
Valor COFINS............: R$ {documento[16]:.2f}
Valor Total.............: R$ {documento[17]:.2f}
Status..................: {documento[18]}
Arquivo XML.............: {documento[19]}
Arquivo DANFE...........: {documento[20]}
Contraparte.............: {documento[21]}
CNPJ/CPF................: {documento[22]}
""")

        else:

            print("\nDocumento fiscal não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar documento fiscal: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close() 

def atualizar_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_documento = int(input("ID do documento fiscal: "))

        id_empresa = int(input("Novo ID da empresa: "))
        tipo = input("Novo tipo do documento: ")
        direcao = input("Nova direção (E/S): ").upper()
        numero = int(input("Novo número do documento: "))
        serie = input("Nova série: ")
        chave = input("Nova chave de acesso: ")
        data_emissao = input("Nova data de emissão (AAAA-MM-DD HH:MM:SS): ")
        cfop = input("Novo CFOP: ")
        natureza = input("Nova natureza da operação: ")

        valor_produtos = float(input("Novo valor dos produtos: "))
        valor_frete = float(input("Novo valor do frete: "))
        valor_desconto = float(input("Novo valor do desconto: "))
        valor_icms = float(input("Novo valor do ICMS: "))
        valor_ipi = float(input("Novo valor do IPI: "))
        valor_pis = float(input("Novo valor do PIS: "))
        valor_cofins = float(input("Novo valor do COFINS: "))
        valor_total = float(input("Novo valor total: "))

        status = input("Novo status: ")

        arquivo_xml = input("Novo caminho do XML: ")
        arquivo_pdf = input("Novo caminho do DANFE (PDF): ")

        nome_contraparte = input("Novo nome da contraparte: ")
        cnpj_cpf = input("Novo CNPJ/CPF da contraparte: ")

        sql = """
            UPDATE documento_fiscal
            SET
                id_empresa_documento_fiscal = %s,
                tipo_documento_fiscal = %s,
                direcao_documento_fiscal = %s,
                numero_documento_fiscal = %s,
                serie_documento_fiscal = %s,
                chave_acesso_documento_fiscal = %s,
                data_emissao_documento_fiscal = %s,
                cfop_documento_fiscal = %s,
                natureza_operacao_documento_fiscal = %s,
                valor_produtos_documento_fiscal = %s,
                valor_frete_documento_fiscal = %s,
                valor_desconto_documento_fiscal = %s,
                valor_icms_documento_fiscal = %s,
                valor_ipi_documento_fiscal = %s,
                valor_pis_documento_fiscal = %s,
                valor_cofins_documento_fiscal = %s,
                valor_total_documento_fiscal = %s,
                status_documento_fiscal = %s,
                arquivo_xml_documento_fiscal = %s,
                arquivo_danfe_pdf_documento_fiscal = %s,
                nome_contraparte_documento_fiscal = %s,
                cnpj_cpf_contraparte_documento_fiscal = %s
            WHERE id_documento_fiscal = %s
        """

        valores = (
            id_empresa,
            tipo,
            direcao,
            numero,
            serie,
            chave,
            data_emissao,
            cfop,
            natureza,
            valor_produtos,
            valor_frete,
            valor_desconto,
            valor_icms,
            valor_ipi,
            valor_pis,
            valor_cofins,
            valor_total,
            status,
            arquivo_xml,
            arquivo_pdf,
            nome_contraparte,
            cnpj_cpf,
            id_documento
        )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nDocumento fiscal atualizado com sucesso!")

        else:

            print("\nDocumento fiscal não encontrado.")

    except Exception as erro:

        print(f"\nErro ao atualizar documento fiscal: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_documento_fiscal():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_documento = int(input("ID do documento fiscal: "))

        confirmar = input("Deseja realmente remover este documento fiscal? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM documento_fiscal
                WHERE id_documento_fiscal = %s
            """

            cursor.execute(sql, (id_documento,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nDocumento fiscal removido com sucesso!")

            else:

                print("\nDocumento fiscal não encontrado.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover documento fiscal: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()