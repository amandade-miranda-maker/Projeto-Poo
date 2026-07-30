from database.database import conectar


def cadastrar_cronograma_tributario():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_empresa = int(input("ID da empresa: "))
        id_imposto = int(input("ID do imposto: "))
        competencia = input("Competência (AAAA-MM): ")
        data_vencimento = input("Data de vencimento (AAAA-MM-DD): ")

        valor_calculado = float(input("Valor calculado: "))

        valor_pago = input("Valor pago (Enter para deixar vazio): ")

        if valor_pago == "":
            valor_pago = None
        else:
            valor_pago = float(valor_pago)

        data_pagamento = input("Data de pagamento (AAAA-MM-DD ou Enter): ")

        if data_pagamento == "":
            data_pagamento = None

        status = input("Status (Pendente/Pago/Atrasado/Isento): ")

        comprovante = input("Comprovante de pagamento (Enter para deixar vazio): ")

        if comprovante == "":
            comprovante = None

        id_colaborador = input("ID do colaborador responsável (Enter para deixar vazio): ")

        if id_colaborador == "":
            id_colaborador = None
        else:
            id_colaborador = int(id_colaborador)

        sql = """
            INSERT INTO cronograma_tributario
            (
                id_empresa_cronograma_tributario,
                id_imposto_cronograma_tributario,
                competencia_cronograma_tributario,
                data_vencimento_cronograma_tributario,
                valor_calculado_cronograma_tributario,
                valor_pago_cronograma_tributario,
                data_pagamento_cronograma_tributario,
                status_cronograma_tributario,
                comprovante_pagamento_cronograma_tributario,
                id_colaborador_resp_cronograma_tributario
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

        valores = (
                    id_empresa,
                    id_imposto,
                    competencia,
                    data_vencimento,
                    valor_calculado,
                    valor_pago,
                    data_pagamento,
                    status,
                    comprovante,
                    id_colaborador
                    )

        cursor.execute(sql, valores)

        conexao.commit()

        print("\nCronograma tributário cadastrado com sucesso!")

    except Exception as erro:

        print(f"\nErro ao cadastrar cronograma tributário: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def listar_cronograma_tributario():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
                SELECT
                    id_cronograma_tributario,
                    id_empresa_cronograma_tributario,
                    id_imposto_cronograma_tributario,
                    competencia_cronograma_tributario,
                    data_vencimento_cronograma_tributario,
                    valor_calculado_cronograma_tributario,
                    status_cronograma_tributario
                FROM cronograma_tributario
                ORDER BY id_cronograma_tributario
            """

        cursor.execute(sql)

        cronogramas = cursor.fetchall()

        if not cronogramas:

            print("\nNenhum cronograma tributário encontrado.")

        else:

            print("\n========== CRONOGRAMAS TRIBUTÁRIOS ==========")

            for cronograma in cronogramas:

                print(f"""
ID......................: {cronograma[0]}
ID Empresa..............: {cronograma[1]}
ID Imposto..............: {cronograma[2]}
Competência.............: {cronograma[3]}
Data de Vencimento......: {cronograma[4]}
Valor Calculado.........: R$ {cronograma[5]:.2f}
Status..................: {cronograma[6]}
""")

    except Exception as erro:

        print(f"\nErro ao listar cronogramas tributários: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def buscar_cronograma_tributario():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_cronograma = int(input("Informe o ID do cronograma tributário: "))

        sql = """
                SELECT
                    id_cronograma_tributario,
                    id_empresa_cronograma_tributario,
                    id_imposto_cronograma_tributario,
                    competencia_cronograma_tributario,
                    data_vencimento_cronograma_tributario,
                    valor_calculado_cronograma_tributario,
                    valor_pago_cronograma_tributario,
                    data_pagamento_cronograma_tributario,
                    status_cronograma_tributario,
                    comprovante_pagamento_cronograma_tributario,
                    id_colaborador_resp_cronograma_tributario
                FROM cronograma_tributario
                WHERE id_cronograma_tributario = %s
                """

        cursor.execute(sql, (id_cronograma,))

        cronograma = cursor.fetchone()

        if cronograma:

            print(f"""
========== CRONOGRAMA TRIBUTÁRIO ==========

ID......................: {cronograma[0]}
ID Empresa..............: {cronograma[1]}
ID Imposto..............: {cronograma[2]}
Competência.............: {cronograma[3]}
Data de Vencimento......: {cronograma[4]}
Valor Calculado.........: R$ {cronograma[5]:.2f}
Valor Pago..............: {cronograma[6]}
Data Pagamento..........: {cronograma[7]}
Status..................: {cronograma[8]}
Comprovante.............: {cronograma[9]}
ID Colaborador..........: {cronograma[10]}
""")

        else:

            print("\nCronograma tributário não encontrado.")

    except Exception as erro:

        print(f"\nErro ao buscar cronograma tributário: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def atualizar_cronograma_tributario():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_cronograma = int(input("ID do cronograma tributário: "))
        id_empresa = int(input("Novo ID da empresa: "))
        id_imposto = int(input("Novo ID do imposto: "))
        competencia = input("Nova competência (AAAA-MM): ")
        data_vencimento = input("Nova data de vencimento (AAAA-MM-DD): ")

        valor_calculado = float(input("Novo valor calculado: "))

        valor_pago = input("Novo valor pago (Enter para deixar vazio): ")

        if valor_pago == "":
            valor_pago = None
        else:
            valor_pago = float(valor_pago)

        data_pagamento = input("Nova data de pagamento (AAAA-MM-DD ou Enter): ")

        if data_pagamento == "":
            data_pagamento = None

        status = input("Novo status (Pendente/Pago/Atrasado/Isento): ")

        comprovante = input("Novo comprovante (Enter para deixar vazio): ")

        if comprovante == "":
            comprovante = None

        id_colaborador = input("Novo ID do colaborador (Enter para deixar vazio): ")

        if id_colaborador == "":
            id_colaborador = None
        else:
            id_colaborador = int(id_colaborador)

        sql = """
                UPDATE cronograma_tributario
                SET
                    id_empresa_cronograma_tributario = %s,
                    id_imposto_cronograma_tributario = %s,
                    competencia_cronograma_tributario = %s,
                    data_vencimento_cronograma_tributario = %s,
                    valor_calculado_cronograma_tributario = %s,
                    valor_pago_cronograma_tributario = %s,
                    data_pagamento_cronograma_tributario = %s,
                    status_cronograma_tributario = %s,
                    comprovante_pagamento_cronograma_tributario = %s,
                    id_colaborador_resp_cronograma_tributario = %s
                WHERE id_cronograma_tributario = %s
            """

        valores = (
                id_empresa,
                id_imposto,
                competencia,
                data_vencimento,
                valor_calculado,
                valor_pago,
                data_pagamento,
                status,
                comprovante,
                id_colaborador,
                id_cronograma
                )

        cursor.execute(sql, valores)

        conexao.commit()

        if cursor.rowcount > 0:

            print("\nCronograma tributário atualizado com sucesso!")

        else:

            print("\nCronograma tributário não encontrado.")

    except Exception as erro:

        print(f"\nErro ao atualizar cronograma tributário: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()

def remover_cronograma_tributario():

    conexao = None
    cursor = None

    try:

        conexao = conectar()
        cursor = conexao.cursor()

        id_cronograma = int(input("ID do cronograma tributário: "))

        confirmar = input("Deseja realmente remover este cronograma tributário? (S/N): ").upper()

        if confirmar == "S":

            sql = """
                DELETE FROM cronograma_tributario
                WHERE id_cronograma_tributario = %s
            """

            cursor.execute(sql, (id_cronograma,))

            conexao.commit()

            if cursor.rowcount > 0:

                print("\nCronograma tributário removido com sucesso!")

            else:

                print("\nCronograma tributário não encontrado.")

        else:

            print("\nOperação cancelada.")

    except Exception as erro:

        print(f"\nErro ao remover cronograma tributário: {erro}")

    finally:

        if cursor:
            cursor.close()

        if conexao:
            conexao.close()