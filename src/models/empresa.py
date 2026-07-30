from database.database import conectar


def exibir_empresa(empresa):

    nome_fantasia = empresa[2] if empresa[2] else "Não informado"
    inscricao_estadual = empresa[4] if empresa[4] else "Não informada"
    inscricao_municipal = empresa[5] if empresa[5] else "Não informada"
    complemento = empresa[15] if empresa[15] else "Não informado"
    responsavel = empresa[21] if empresa[21] else "Não informado"

    print(f"""
========================================
ID................: {empresa[0]}
Razão Social......: {empresa[1]}
Nome Fantasia.....: {nome_fantasia}
CNPJ..............: {empresa[3]}
Inscrição Estadual: {inscricao_estadual}
Inscrição Municipal: {inscricao_municipal}
CNAE..............: {empresa[6]}
Regime Tributário.: {empresa[7]}
Data Abertura.....: {empresa[8].strftime("%d/%m/%Y")}
Data Cadastro.....: {empresa[9].strftime("%d/%m/%Y %H:%M:%S")}
Status............: {empresa[10]}
E-mail............: {empresa[11]}
Telefone..........: {empresa[12]}
Logradouro........: {empresa[13]}
Número............: {empresa[14]}
Complemento.......: {complemento}
Bairro............: {empresa[16]}
Cidade............: {empresa[17]}
UF................: {empresa[18]}
CEP...............: {empresa[19]}
Capital Social....: R$ {empresa[20]:.2f}
Responsável.......: {responsavel}
========================================
""")


def cadastrar_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        razao_social = input("Razão social: ")
        nome_fantasia = input("Nome fantasia: ")
        cnpj = input("CNPJ: ")
        inscricao_estadual = input("Inscrição estadual: ")
        inscricao_municipal = input("Inscrição municipal: ")
        cnae = input("CNAE principal: ")
        regime = input("Regime tributário: ")
        data_abertura = input("Data de abertura (AAAA-MM-DD): ")
        status = input("Status: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        logradouro = input("Logradouro: ")
        numero = input("Número: ")
        complemento = input("Complemento: ")

        if complemento == "":
            complemento = None

        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        uf = input("UF: ")
        cep = input("CEP: ")
        capital_social = float(input("Capital social: "))

        id_responsavel = input("ID do colaborador responsável (Enter para nenhum): ")

        if id_responsavel == "":
            id_responsavel = None
        else:

            id_responsavel = int(id_responsavel)

            sql = """
                SELECT
                    id_colaborador,
                    nome_colaborador
                FROM colaborador
                WHERE id_colaborador = %s
            """

            cursor.execute(sql, (id_responsavel,))

            colaborador = cursor.fetchone()

            if not colaborador:

                print("\nColaborador não encontrado.")
                return

            print(f"\nResponsável: {colaborador[1]}")

        sql = """
            INSERT INTO empresa
            (
                razao_social_empresa,
                nome_fantasia_empresa,
                cnpj_empresa,
                inscricao_estadual_empresa,
                inscricao_municipal_empresa,
                cnae_principal_empresa,
                regime_tributario_empresa,
                data_abertura_empresa,
                status_empresa,
                email_empresa,
                telefone_empresa,
                logradouro_empresa,
                numero_empresa,
                complemento_empresa,
                bairro_empresa,
                cidade_empresa,
                uf_empresa,
                cep_empresa,
                capital_social_empresa,
                id_colaborador_resp_empresa
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (
            razao_social,
            nome_fantasia,
            cnpj,
            inscricao_estadual,
            inscricao_municipal,
            cnae,
            regime,
            data_abertura,
            status,
            email,
            telefone,
            logradouro,
            numero,
            complemento,
            bairro,
            cidade,
            uf,
            cep,
            capital_social,
            id_responsavel
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nEmpresa cadastrada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar empresa: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def listar_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                e.id_empresa,
                e.razao_social_empresa,
                e.nome_fantasia_empresa,
                e.cnpj_empresa,
                e.inscricao_estadual_empresa,
                e.inscricao_municipal_empresa,
                e.cnae_principal_empresa,
                e.regime_tributario_empresa,
                e.data_abertura_empresa,
                e.data_cadastro_empresa,
                e.status_empresa,
                e.email_empresa,
                e.telefone_empresa,
                e.logradouro_empresa,
                e.numero_empresa,
                e.complemento_empresa,
                e.bairro_empresa,
                e.cidade_empresa,
                e.uf_empresa,
                e.cep_empresa,
                e.capital_social_empresa,
                c.nome_colaborador
            FROM empresa e
            LEFT JOIN colaborador c
                ON c.id_colaborador = e.id_colaborador_resp_empresa
            ORDER BY e.razao_social_empresa
        """

        cursor.execute(sql)

        empresas = cursor.fetchall()

        if not empresas:

            print("\nNenhuma empresa encontrada.")

        else:

            print("\n========== EMPRESAS CADASTRADAS ==========")

            for empresa in empresas:

                exibir_empresa(empresa)

    except Exception as erro:

        print(f"\nErro ao listar empresas: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def buscar_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("Informe o ID da empresa: "))
        nome_empresa = input("Informe o nome da empresa: ")

        sql = """
            SELECT
                e.id_empresa,
                e.razao_social_empresa,
                e.nome_fantasia_empresa,
                e.cnpj_empresa,
                e.inscricao_estadual_empresa,
                e.inscricao_municipal_empresa,
                e.cnae_principal_empresa,
                e.regime_tributario_empresa,
                e.data_abertura_empresa,
                e.data_cadastro_empresa,
                e.status_empresa,
                e.email_empresa,
                e.telefone_empresa,
                e.logradouro_empresa,
                e.numero_empresa,
                e.complemento_empresa,
                e.bairro_empresa,
                e.cidade_empresa,
                e.uf_empresa,
                e.cep_empresa,
                e.capital_social_empresa,
                c.nome_colaborador
            FROM empresa e
            LEFT JOIN colaborador c
                ON c.id_colaborador = e.id_colaborador_resp_empresa
            WHERE e.id_empresa = %s
        """

        cursor.execute(sql, (id_empresa, nome_empresa))

        empresa = cursor.fetchone()

        if empresa:

            print("\n========== EMPRESA ENCONTRADA ==========")

            exibir_empresa(empresa)

        else:

            print("\nEmpresa não encontrada.")

    except Exception as erro:

        print(f"\nErro ao buscar empresa: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def atualizar_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("Informe o ID da empresa: "))

        sql = """
            SELECT
                e.id_empresa,
                e.razao_social_empresa,
                e.nome_fantasia_empresa,
                e.cnpj_empresa,
                e.inscricao_estadual_empresa,
                e.inscricao_municipal_empresa,
                e.cnae_principal_empresa,
                e.regime_tributario_empresa,
                e.data_abertura_empresa,
                e.data_cadastro_empresa,
                e.status_empresa,
                e.email_empresa,
                e.telefone_empresa,
                e.logradouro_empresa,
                e.numero_empresa,
                e.complemento_empresa,
                e.bairro_empresa,
                e.cidade_empresa,
                e.uf_empresa,
                e.cep_empresa,
                e.capital_social_empresa,
                c.nome_colaborador
            FROM empresa e
            LEFT JOIN colaborador c
                ON c.id_colaborador = e.id_colaborador_resp_empresa
            WHERE e.id_empresa = %s
        """

        cursor.execute(sql, (id_empresa,))

        empresa = cursor.fetchone()

        if not empresa:

            print("\nEmpresa não encontrada.")
            return

        print("\n========== EMPRESA ATUAL ==========")

        exibir_empresa(empresa)

        razao_social = input("Nova razão social: ")
        nome_fantasia = input("Novo nome fantasia: ")
        cnpj = input("Novo CNPJ: ")
        inscricao_estadual = input("Nova inscrição estadual: ")
        inscricao_municipal = input("Nova inscrição municipal: ")
        cnae = input("Novo CNAE principal: ")
        regime = input("Novo regime tributário: ")
        data_abertura = input("Nova data de abertura (AAAA-MM-DD): ")
        status = input("Novo status: ")
        email = input("Novo e-mail: ")
        telefone = input("Novo telefone: ")
        logradouro = input("Novo logradouro: ")
        numero = input("Novo número: ")
        complemento = input("Novo complemento: ")

        if complemento == "":
            complemento = None

        bairro = input("Novo bairro: ")
        cidade = input("Nova cidade: ")
        uf = input("Nova UF: ")
        cep = input("Novo CEP: ")
        capital_social = float(input("Novo capital social: "))

        id_responsavel = input("Novo ID do responsável (Enter para nenhum): ")

        if id_responsavel == "":
            id_responsavel = None

        else:

            id_responsavel = int(id_responsavel)

            sql = """
                SELECT
                    id_colaborador,
                    nome_colaborador
                FROM colaborador
                WHERE id_colaborador = %s
            """

            cursor.execute(sql, (id_responsavel,))

            colaborador = cursor.fetchone()

            if not colaborador:

                print("\nColaborador não encontrado.")
                return

            print(f"\nResponsável selecionado: {colaborador[1]}")

        sql = """
            UPDATE empresa
            SET
                razao_social_empresa = %s,
                nome_fantasia_empresa = %s,
                cnpj_empresa = %s,
                inscricao_estadual_empresa = %s,
                inscricao_municipal_empresa = %s,
                cnae_principal_empresa = %s,
                regime_tributario_empresa = %s,
                data_abertura_empresa = %s,
                status_empresa = %s,
                email_empresa = %s,
                telefone_empresa = %s,
                logradouro_empresa = %s,
                numero_empresa = %s,
                complemento_empresa = %s,
                bairro_empresa = %s,
                cidade_empresa = %s,
                uf_empresa = %s,
                cep_empresa = %s,
                capital_social_empresa = %s,
                id_colaborador_resp_empresa = %s
            WHERE id_empresa = %s
        """

        valores = (
            razao_social,
            nome_fantasia,
            cnpj,
            inscricao_estadual,
            inscricao_municipal,
            cnae,
            regime,
            data_abertura,
            status,
            email,
            telefone,
            logradouro,
            numero,
            complemento,
            bairro,
            cidade,
            uf,
            cep,
            capital_social,
            id_responsavel,
            id_empresa
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nEmpresa atualizada com sucesso!")

    except Exception as erro:

        print(f"\nErro ao atualizar empresa: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def remover_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("Informe o ID da empresa: "))

        sql = """
            SELECT
                e.id_empresa,
                e.razao_social_empresa,
                e.nome_fantasia_empresa,
                e.cnpj_empresa,
                e.inscricao_estadual_empresa,
                e.inscricao_municipal_empresa,
                e.cnae_principal_empresa,
                e.regime_tributario_empresa,
                e.data_abertura_empresa,
                e.data_cadastro_empresa,
                e.status_empresa,
                e.email_empresa,
                e.telefone_empresa,
                e.logradouro_empresa,
                e.numero_empresa,
                e.complemento_empresa,
                e.bairro_empresa,
                e.cidade_empresa,
                e.uf_empresa,
                e.cep_empresa,
                e.capital_social_empresa,
                c.nome_colaborador
            FROM empresa e
            LEFT JOIN colaborador c
                ON c.id_colaborador = e.id_colaborador_resp_empresa
            WHERE e.id_empresa = %s
        """

        cursor.execute(sql, (id_empresa,))

        empresa = cursor.fetchone()

        if not empresa:

            print("\nEmpresa não encontrada.")
            return

        print("\n========== EMPRESA A SER REMOVIDA ==========")

        exibir_empresa(empresa)

        confirmar = input("Deseja realmente remover esta empresa? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM empresa
                WHERE id_empresa = %s
            """

            cursor.execute(sql, (id_empresa,))

            conexao.commit()

            print("\nEmpresa removida com sucesso!")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover empresa: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()