from database.database import conectar


def exibir_colaborador(colaborador):

    data_demissao = (
        colaborador[7].strftime("%d/%m/%Y")
        if colaborador[7]
        else "Não informada"
    )

    print(f"""
========================================
ID................: {colaborador[0]}
Nome..............: {colaborador[1]}
CPF...............: {colaborador[2]}
Nascimento........: {colaborador[3].strftime("%d/%m/%Y")}
E-mail............: {colaborador[4]}
Telefone..........: {colaborador[5]}
Admissão..........: {colaborador[6].strftime("%d/%m/%Y")}
Demissão..........: {data_demissao}
Status............: {colaborador[8]}
Cargo.............: {colaborador[9]}
========================================
""")


def cadastrar_colaborador():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        nome = input("Nome: ")
        cpf = input("CPF: ")
        nascimento = input("Data de nascimento (AAAA-MM-DD): ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        admissao = input("Data de admissão (AAAA-MM-DD): ")
        demissao = input("Data de demissão (AAAA-MM-DD ou Enter): ")

        if demissao == "":
            demissao = None

        status = input("Status (Ativo/Inativo): ")

        id_cargo = int(input("ID do cargo: "))

        sql = """
            SELECT
                id_cargo,
                nome_cargo
            FROM cargo
            WHERE id_cargo = %s
        """

        cursor.execute(sql, (id_cargo,))

        cargo = cursor.fetchone()

        if not cargo:

            print("\nCargo não encontrado.")
            return

        print(f"\nCargo selecionado: {cargo[1]}")

        sql = """
            INSERT INTO colaborador
            (
                nome_colaborador,
                cpf_colaborador,
                data_nascimento_colaborador,
                email_colaborador,
                telefone_colaborador,
                data_admissao_colaborador,
                data_demissao_colaborador,
                status_colaborador,
                id_cargo_colaborador
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(sql, (
            nome,
            cpf,
            nascimento,
            email,
            telefone,
            admissao,
            demissao,
            status,
            id_cargo
        ))

        conexao.commit()

        print("\nColaborador cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar colaborador: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_colaborador():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                c.id_colaborador,
                c.nome_colaborador,
                c.cpf_colaborador,
                c.data_nascimento_colaborador,
                c.email_colaborador,
                c.telefone_colaborador,
                c.data_admissao_colaborador,
                c.data_demissao_colaborador,
                c.status_colaborador,
                ca.nome_cargo
            FROM colaborador c
            INNER JOIN cargo ca
                ON ca.id_cargo = c.id_cargo_colaborador
            ORDER BY c.nome_colaborador
        """

        cursor.execute(sql)

        colaboradores = cursor.fetchall()

        if not colaboradores:

            print("\nNenhum colaborador encontrado.")

        else:

            print("\n========== COLABORADORES CADASTRADOS ==========")

            for colaborador in colaboradores:

                exibir_colaborador(colaborador)

    except Exception as erro:

        print(f"\nErro ao listar colaboradores: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_colaborador():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_colaborador = int(input("Informe o ID do colaborador: "))
        nome_colaborador = input("Informe o nome do colaborador (ou pressione Enter para pular): ")


        sql = """
            SELECT
                c.id_colaborador,
                c.nome_colaborador,
                c.cpf_colaborador,
                c.data_nascimento_colaborador,
                c.email_colaborador,
                c.telefone_colaborador,
                c.data_admissao_colaborador,
                c.data_demissao_colaborador,
                c.status_colaborador,
                ca.nome_cargo
            FROM colaborador c
            INNER JOIN cargo ca
                ON ca.id_cargo = c.id_cargo_colaborador
            WHERE c.id_colaborador = %s AND c.nome_colaborador = %s
        """

        cursor.execute(sql, (id_colaborador, nome_colaborador))

        colaborador = cursor.fetchone()

        if colaborador:

            print("\n========== COLABORADOR ENCONTRADO ==========")

            exibir_colaborador(colaborador)

        else:

            print("\nColaborador não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar colaborador: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_colaborador():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_colaborador = int(input("Informe o ID do colaborador: "))

        sql = """
            SELECT
                c.id_colaborador,
                c.nome_colaborador,
                c.cpf_colaborador,
                c.data_nascimento_colaborador,
                c.email_colaborador,
                c.telefone_colaborador,
                c.data_admissao_colaborador,
                c.data_demissao_colaborador,
                c.status_colaborador,
                ca.nome_cargo
            FROM colaborador c
            INNER JOIN cargo ca
                ON ca.id_cargo = c.id_cargo_colaborador
            WHERE c.id_colaborador = %s
        """

        cursor.execute(sql, (id_colaborador,))

        colaborador = cursor.fetchone()

        if not colaborador:

            print("\nColaborador não encontrado.")
            return

        print("\n========== COLABORADOR ATUAL ==========")

        exibir_colaborador(colaborador)

        nome = input("Novo nome: ")
        cpf = input("Novo CPF: ")
        nascimento = input("Nova data de nascimento (AAAA-MM-DD): ")
        email = input("Novo e-mail: ")
        telefone = input("Novo telefone: ")
        admissao = input("Nova data de admissão (AAAA-MM-DD): ")
        demissao = input("Nova data de demissão (AAAA-MM-DD ou Enter): ")

        if demissao == "":
            demissao = None

        status = input("Novo status: ")

        id_cargo = int(input("Novo ID do cargo: "))

        sql = """
            SELECT
                id_cargo,
                nome_cargo
            FROM cargo
            WHERE id_cargo = %s
        """

        cursor.execute(sql, (id_cargo,))

        cargo = cursor.fetchone()

        if not cargo:

            print("\nCargo não encontrado.")
            return

        print(f"\nNovo cargo: {cargo[1]}")

        sql = """
            UPDATE colaborador
            SET
                nome_colaborador = %s,
                cpf_colaborador = %s,
                data_nascimento_colaborador = %s,
                email_colaborador = %s,
                telefone_colaborador = %s,
                data_admissao_colaborador = %s,
                data_demissao_colaborador = %s,
                status_colaborador = %s,
                id_cargo_colaborador = %s
            WHERE id_colaborador = %s
        """

        cursor.execute(sql, (
            nome,
            cpf,
            nascimento,
            email,
            telefone,
            admissao,
            demissao,
            status,
            id_cargo,
            id_colaborador
        ))

        conexao.commit()

        print("\nColaborador atualizado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao atualizar colaborador: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def remover_colaborador():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_colaborador = int(input("Informe o ID do colaborador: "))

        sql = """
            SELECT
                c.id_colaborador,
                c.nome_colaborador,
                c.cpf_colaborador,
                c.data_nascimento_colaborador,
                c.email_colaborador,
                c.telefone_colaborador,
                c.data_admissao_colaborador,
                c.data_demissao_colaborador,
                c.status_colaborador,
                ca.nome_cargo
            FROM colaborador c
            INNER JOIN cargo ca
                ON ca.id_cargo = c.id_cargo_colaborador
            WHERE c.id_colaborador = %s
        """

        cursor.execute(sql, (id_colaborador,))

        colaborador = cursor.fetchone()

        if not colaborador:

            print("\nColaborador não encontrado.")
            return

        print("\n========== COLABORADOR A SER REMOVIDO ==========")

        exibir_colaborador(colaborador)

        confirmar = input("Deseja realmente remover este colaborador? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM colaborador
                WHERE id_colaborador = %s
            """

            cursor.execute(sql, (id_colaborador,))
            conexao.commit()

            print("\nColaborador removido com sucesso!")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover colaborador: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()