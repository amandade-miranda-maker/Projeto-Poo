from database.database import conectar


def cadastrar_contato_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        nome = input("Nome do contato: ")

        cargo = input("Cargo (Enter para deixar vazio): ")

        if cargo == "":
            cargo = None

        email = input("E-mail (Enter para deixar vazio): ")

        if email == "":
            email = None

        telefone = input("Telefone (Enter para deixar vazio): ")

        if telefone == "":
            telefone = None

        tipo = input("Tipo (Financeiro/Fiscal/Societário/Geral): ")

        principal = input("É o contato principal? (S/N): ").upper()

        if principal == "S":
            principal = True
        else:
            principal = False

        sql = """
            INSERT INTO contato_empresa
            (
                id_empresa_contato_empresa,
                nome_contato_empresa,
                cargo_contato_empresa,
                email_contato_empresa,
                telefone_contato_empresa,
                tipo_contato_empresa,
                principal_contato_empresa
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s)
        """

        valores = (
            id_empresa,
            nome,
            cargo,
            email,
            telefone,
            tipo,
            principal
        )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nContato cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar contato: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def listar_contato_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
            SELECT
                id_contato_empresa,
                id_empresa_contato_empresa,
                nome_contato_empresa,
                cargo_contato_empresa,
                email_contato_empresa,
                telefone_contato_empresa,
                tipo_contato_empresa,
                principal_contato_empresa
            FROM contato_empresa
            ORDER BY id_contato_empresa
        """

        cursor.execute(sql)

        contatos = cursor.fetchall()

        if not contatos:

            print("\nNenhum contato encontrado.")

        else:

            print("\n========== CONTATOS ==========")

            for contato in contatos:

                principal = "Sim" if contato[7] else "Não"

                print(f"""
ID......................: {contato[0]}
ID Empresa..............: {contato[1]}
Nome....................: {contato[2]}
Cargo...................: {contato[3]}
E-mail..................: {contato[4]}
Telefone................: {contato[5]}
Tipo....................: {contato[6]}
Principal...............: {principal}
""")

    except Exception as erro:

        print(f"\nErro ao listar contatos: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_contato_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_contato = int(input("Informe o ID do contato: "))

        sql = """
            SELECT
                id_contato_empresa,
                id_empresa_contato_empresa,
                nome_contato_empresa,
                cargo_contato_empresa,
                email_contato_empresa,
                telefone_contato_empresa,
                tipo_contato_empresa,
                principal_contato_empresa
            FROM contato_empresa
            WHERE id_contato_empresa = %s
        """

        cursor.execute(sql, (id_contato,))

        contato = cursor.fetchone()

        if contato:

            principal = "Sim" if contato[7] else "Não"

            print(f"""
========== CONTATO ==========

ID......................: {contato[0]}
ID Empresa..............: {contato[1]}
Nome....................: {contato[2]}
Cargo...................: {contato[3]}
E-mail..................: {contato[4]}
Telefone................: {contato[5]}
Tipo....................: {contato[6]}
Principal...............: {principal}
""")

        else:

            print("\nContato não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar contato: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def atualizar_contato_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_contato = int(input("ID do contato: "))
        id_empresa = int(input("Novo ID da empresa: "))
        nome = input("Novo nome: ")

        cargo = input("Novo cargo (Enter para deixar vazio): ")

        if cargo == "":
            cargo = None

        email = input("Novo e-mail (Enter para deixar vazio): ")

        if email == "":
            email = None

        telefone = input("Novo telefone (Enter para deixar vazio): ")

        if telefone == "":
            telefone = None

        tipo = input("Novo tipo (Financeiro/Fiscal/Societário/Geral): ")

        principal = input("É o contato principal? (S/N): ").upper()

        if principal == "S":
            principal = True
        else:
            principal = False

        sql = """
            UPDATE contato_empresa
            SET
                id_empresa_contato_empresa = %s,
                nome_contato_empresa = %s,
                cargo_contato_empresa = %s,
                email_contato_empresa = %s,
                telefone_contato_empresa = %s,
                tipo_contato_empresa = %s,
                principal_contato_empresa = %s
            WHERE id_contato_empresa = %s
        """

        valores = (
            id_empresa,
            nome,
            cargo,
            email,
            telefone,
            tipo,
            principal,
            id_contato
        )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nContato atualizado com sucesso!")

        else:

            print("\nContato não encontrado.")

    except Exception as erro:

        print(f"\nErro ao atualizar contato: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()
    
def remover_contato_empresa():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_contato = int(input("ID do contato: "))

        confirmar = input("Deseja realmente remover este contato? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM contato_empresa
                WHERE id_contato_empresa = %s
            """

            cursor.execute(sql, (id_contato,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nContato removido com sucesso!")

            else:

                print("\nContato não encontrado.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover contato: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()