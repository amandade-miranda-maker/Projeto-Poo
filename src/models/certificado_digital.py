from database.database import conectar


def cadastrar_certificado_digital():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        tipo = input("Tipo (A1/A3): ")
        numero_serie = input("Número de série: ")

        emissor = input("Emissor (Enter para deixar vazio): ")

        if emissor == "":
            emissor = None

        data_emissao = input("Data de emissão (AAAA-MM-DD): ")
        data_validade = input("Data de validade (AAAA-MM-DD): ")

        arquivo = input("Arquivo do certificado (Enter para deixar vazio): ")

        if arquivo == "":
            arquivo = None

        referencia = input("Referência da senha no cofre (Enter para deixar vazio): ")

        if referencia == "":
            referencia = None

        status = input("Status (Válido/Vencido/Revogado): ")

        sql = """
            INSERT INTO certificado_digital
            (
                id_empresa_certificado_digital,
                tipo_certificado_digital,
                numero_serie_certificado_digital,
                emissor_certificado_digital,
                data_emissao_certificado_digital,
                data_validade_certificado_digital,
                arquivo_certificado_digital,
                referencia_senha_cofre_certificado_digital,
                status_certificado_digital
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (
            id_empresa,
            tipo,
            numero_serie,
            emissor,
            data_emissao,
            data_validade,
            arquivo,
            referencia,
            status
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nCertificado digital cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar certificado digital: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def listar_certificado_digital():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_certificado_digital,
                id_empresa_certificado_digital,
                tipo_certificado_digital,
                numero_serie_certificado_digital,
                emissor_certificado_digital,
                data_emissao_certificado_digital,
                data_validade_certificado_digital,
                status_certificado_digital
            FROM certificado_digital
            ORDER BY id_certificado_digital
        """

        cursor.execute(sql)

        certificados = cursor.fetchall()

        if not certificados:

            print("\nNenhum certificado encontrado.")

        else:

            print("\n========== CERTIFICADOS DIGITAIS ==========")

            for certificado in certificados:

                print(f"""
ID......................: {certificado[0]}
ID Empresa..............: {certificado[1]}
Tipo....................: {certificado[2]}
Número de Série.........: {certificado[3]}
Emissor.................: {certificado[4]}
Data de Emissão.........: {certificado[5]}
Data de Validade........: {certificado[6]}
Status..................: {certificado[7]}
""")

    except Exception as erro:

        print(f"\nErro ao listar certificados digitais: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_certificado_digital():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_certificado = int(input("Informe o ID do certificado digital: "))

        sql = """
            SELECT
                id_certificado_digital,
                id_empresa_certificado_digital,
                tipo_certificado_digital,
                numero_serie_certificado_digital,
                emissor_certificado_digital,
                data_emissao_certificado_digital,
                data_validade_certificado_digital,
                arquivo_certificado_digital,
                referencia_senha_cofre_certificado_digital,
                status_certificado_digital
            FROM certificado_digital
            WHERE id_certificado_digital = %s
        """

        cursor.execute(sql, (id_certificado,))

        certificado = cursor.fetchone()

        if certificado:

            print(f"""
========== CERTIFICADO DIGITAL ==========

ID......................: {certificado[0]}
ID Empresa..............: {certificado[1]}
Tipo....................: {certificado[2]}
Número de Série.........: {certificado[3]}
Emissor.................: {certificado[4]}
Data de Emissão.........: {certificado[5]}
Data de Validade........: {certificado[6]}
Arquivo.................: {certificado[7]}
Referência no Cofre.....: {certificado[8]}
Status..................: {certificado[9]}
""")

        else:

            print("\nCertificado digital não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar certificado digital: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def atualizar_certificado_digital():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_certificado = int(input("ID do certificado digital: "))

        id_empresa = int(input("Novo ID da empresa: "))
        tipo = input("Novo tipo (A1/A3): ")
        numero_serie = input("Novo número de série: ")

        emissor = input("Novo emissor (Enter para deixar vazio): ")

        if emissor == "":
            emissor = None

        data_emissao = input("Nova data de emissão (AAAA-MM-DD): ")
        data_validade = input("Nova data de validade (AAAA-MM-DD): ")

        arquivo = input("Novo arquivo (Enter para deixar vazio): ")

        if arquivo == "":
            arquivo = None

        referencia = input("Nova referência da senha (Enter para deixar vazio): ")

        if referencia == "":
            referencia = None

        status = input("Novo status (Válido/Vencido/Revogado): ")

        sql = """
            UPDATE certificado_digital
            SET
                id_empresa_certificado_digital = %s,
                tipo_certificado_digital = %s,
                numero_serie_certificado_digital = %s,
                emissor_certificado_digital = %s,
                data_emissao_certificado_digital = %s,
                data_validade_certificado_digital = %s,
                arquivo_certificado_digital = %s,
                referencia_senha_cofre_certificado_digital = %s,
                status_certificado_digital = %s
            WHERE id_certificado_digital = %s
        """

        valores = (
            id_empresa,
            tipo,
            numero_serie,
            emissor,
            data_emissao,
            data_validade,
            arquivo,
            referencia,
            status,
            id_certificado
        )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nCertificado digital atualizado com sucesso!")

        else:

            print("\nCertificado digital não encontrado.")

    except Exception as erro:

        print(f"\nErro ao atualizar certificado digital: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_certificado_digital():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_certificado = int(input("ID do certificado digital: "))

        confirmar = input("Deseja realmente remover este certificado digital? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM certificado_digital
                WHERE id_certificado_digital = %s
            """

            cursor.execute(sql, (id_certificado,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nCertificado digital removido com sucesso!")

            else:

                print("\nCertificado digital não encontrado.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover certificado digital: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()