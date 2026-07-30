from database.database import conectar


def exibir_cargo(cargo):

    descricao = cargo[2] if cargo[2] else "Não informada"
    salario = cargo[4] if cargo[4] is not None else 0

    print(f"""
========================================
ID................: {cargo[0]}
Nome..............: {cargo[1]}
Descrição.........: {descricao}
Nível Hierárquico.: {cargo[3]}
Salário Base......: R$ {salario:.2f}
Status............: {cargo[5]}
========================================
""")


def cadastrar_cargo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        nome = input("Nome do cargo: ")
        descricao = input("Descrição: ")
        nivel = int(input("Nível hierárquico: "))
        salario = float(input("Salário base: "))
        status = input("Status (Ativo/Inativo): ")

        sql = """
            INSERT INTO cargo
            (
                nome_cargo,
                descricao_cargo,
                nivel_hierarquico_cargo,
                salario_base_cargo,
                status_cargo
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            nome,
            descricao,
            nivel,
            salario,
            status
        ))

        conexao.commit()

        print("\nCargo cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar cargo: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def listar_cargo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_cargo,
                nome_cargo,
                descricao_cargo,
                nivel_hierarquico_cargo,
                salario_base_cargo,
                status_cargo
            FROM cargo
            ORDER BY nome_cargo
        """

        cursor.execute(sql)

        cargos = cursor.fetchall()

        if not cargos:

            print("\nNenhum cargo encontrado.")

        else:

            print("\n========== CARGOS CADASTRADOS ==========")

            for cargo in cargos:
                exibir_cargo(cargo)

    except Exception as erro:

        print(f"\nErro ao listar cargos: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def buscar_cargo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_cargo = int(input("Informe o ID do cargo: "))

        sql = """
            SELECT
                id_cargo,
                nome_cargo,
                descricao_cargo,
                nivel_hierarquico_cargo,
                salario_base_cargo,
                status_cargo
            FROM cargo
            WHERE id_cargo = %s
        """

        cursor.execute(sql, (id_cargo,))

        cargo = cursor.fetchone()

        if cargo:

            print("\n========== CARGO ENCONTRADO ==========")

            exibir_cargo(cargo)

        else:

            print("\nCargo não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar cargo: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def atualizar_cargo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_cargo = int(input("Informe o ID do cargo: "))

        sql = """
            SELECT
                id_cargo,
                nome_cargo,
                descricao_cargo,
                nivel_hierarquico_cargo,
                salario_base_cargo,
                status_cargo
            FROM cargo
            WHERE id_cargo = %s
        """

        cursor.execute(sql, (id_cargo,))

        cargo = cursor.fetchone()

        if not cargo:

            print("\nCargo não encontrado.")
            return

        print("\n========== CARGO ATUAL ==========")

        exibir_cargo(cargo)

        nome = input("Novo nome: ")
        descricao = input("Nova descrição: ")
        nivel = int(input("Novo nível hierárquico: "))
        salario = float(input("Novo salário base: "))
        status = input("Novo status: ")

        sql = """
            UPDATE cargo
            SET
                nome_cargo = %s,
                descricao_cargo = %s,
                nivel_hierarquico_cargo = %s,
                salario_base_cargo = %s,
                status_cargo = %s
            WHERE id_cargo = %s
        """

        cursor.execute(sql, (
            nome,
            descricao,
            nivel,
            salario,
            status,
            id_cargo
        ))

        conexao.commit()

        print("\nCargo atualizado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao atualizar cargo: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()


def remover_cargo():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_cargo = int(input("Informe o ID do cargo: "))

        sql = """
            SELECT
                id_cargo,
                nome_cargo,
                descricao_cargo,
                nivel_hierarquico_cargo,
                salario_base_cargo,
                status_cargo
            FROM cargo
            WHERE id_cargo = %s
        """

        cursor.execute(sql, (id_cargo,))

        cargo = cursor.fetchone()

        if not cargo:

            print("\nCargo não encontrado.")
            return

        print("\n========== CARGO A SER REMOVIDO ==========")

        exibir_cargo(cargo)

        confirmar = input("Deseja realmente remover este cargo? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM cargo
                WHERE id_cargo = %s
            """

            cursor.execute(sql, (id_cargo,))
            conexao.commit()

            print("\nCargo removido com sucesso!")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover cargo: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()