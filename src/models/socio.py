from database.database import conectar


def cadastrar_socio():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        nome = input("Nome do sócio: ")
        cnpj_cpf = input("CPF/CNPJ: ")
        percentual = float(input("Percentual de participação: "))
        data_entrada = input("Data de entrada (AAAA-MM-DD): ")

        data_saida = input("Data de saída (AAAA-MM-DD ou Enter): ")

        if data_saida == "":
            data_saida = None

        administrador = input("É administrador? (S/N): ").upper()

        if administrador == "S":
            administrador = True
        else:
            administrador = False

        status = input("Status (Ativo/Inativo): ")

        sql = """
            INSERT INTO socio
            (
                id_empresa_socio,
                nome_socio,
                cnpj_cpf_socio,
                percentual_participacao_socio,
                data_entrada_socio,
                data_saida_socio,
                administrador_socio,
                status_socio
            )
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            id_empresa,
            nome,
            cnpj_cpf,
            percentual,
            data_entrada,
            data_saida,
            administrador,
            status
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nSócio cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar sócio: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_socio():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_socio,
                id_empresa_socio,
                nome_socio,
                cnpj_cpf_socio,
                percentual_participacao_socio,
                administrador_socio,
                status_socio
            FROM socio
            ORDER BY id_socio
        """

        cursor.execute(sql)

        socios = cursor.fetchall()

        if not socios:

            print("\nNenhum sócio encontrado.")

        else:

            print("\n========== SÓCIOS ==========")

            for socio in socios:

                administrador = "Sim" if socio[5] else "Não"

                print(f"""
ID......................: {socio[0]}
ID Empresa..............: {socio[1]}
Nome....................: {socio[2]}
CPF/CNPJ................: {socio[3]}
Participação............: {socio[4]}%
Administrador...........: {administrador}
Status..................: {socio[6]}
""")

    except Exception as erro:

        print(f"\nErro ao listar sócios: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_socio():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_socio = int(input("Informe o ID do sócio: "))

        sql = """
            SELECT
                id_socio,
                id_empresa_socio,
                nome_socio,
                cnpj_cpf_socio,
                percentual_participacao_socio,
                data_entrada_socio,
                data_saida_socio,
                administrador_socio,
                status_socio
            FROM socio
            WHERE id_socio = %s
        """

        cursor.execute(sql, (id_socio,))

        socio = cursor.fetchone()

        if socio:

            administrador = "Sim" if socio[7] else "Não"

            print(f"""
========== SÓCIO ==========

ID......................: {socio[0]}
ID Empresa..............: {socio[1]}
Nome....................: {socio[2]}
CPF/CNPJ................: {socio[3]}
Participação............: {socio[4]}%
Data de Entrada.........: {socio[5]}
Data de Saída...........: {socio[6]}
Administrador...........: {administrador}
Status..................: {socio[8]}
""")

        else:

            print("\nSócio não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar sócio: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_socio():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_socio = int(input("ID do sócio: "))

        id_empresa = int(input("Novo ID da empresa: "))
        nome = input("Novo nome: ")
        cnpj_cpf = input("Novo CPF/CNPJ: ")
        percentual = float(input("Novo percentual de participação: "))
        data_entrada = input("Nova data de entrada (AAAA-MM-DD): ")

        data_saida = input("Nova data de saída (AAAA-MM-DD ou Enter): ")

        if data_saida == "":
            data_saida = None

        administrador = input("É administrador? (S/N): ").upper()

        if administrador == "S":
            administrador = True
        else:
            administrador = False

        status = input("Novo status (Ativo/Inativo): ")

        sql = """
            UPDATE socio
            SET
                id_empresa_socio = %s,
                nome_socio = %s,
                cnpj_cpf_socio = %s,
                percentual_participacao_socio = %s,
                data_entrada_socio = %s,
                data_saida_socio = %s,
                administrador_socio = %s,
                status_socio = %s
            WHERE id_socio = %s
        """

        valores = (
            id_empresa,
            nome,
            cnpj_cpf,
            percentual,
            data_entrada,
            data_saida,
            administrador,
            status,
            id_socio
        )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nSócio atualizado com sucesso!")

        else:

            print("\nSócio não encontrado.")

    except Exception as erro:

        print(f"\nErro ao atualizar sócio: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_socio():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_socio = int(input("ID do sócio: "))

        confirmar = input("Deseja realmente remover este sócio? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM socio
                WHERE id_socio = %s
            """

            cursor.execute(sql, (id_socio,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nSócio removido com sucesso!")

            else:

                print("\nSócio não encontrado.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover sócio: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()