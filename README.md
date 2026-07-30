# 📊 Sistema de Administração Empresarial (SA)

## 📖 Sobre o Projeto

O **Sistema de Administração Empresarial (SA)** é um projeto acadêmico desenvolvido para a disciplina de **Banco de Dados**, tendo como objetivo aplicar conceitos de modelagem relacional, normalização, integridade referencial e manipulação de dados através da implementação completa de operações **CRUD (Create, Read, Update e Delete)**.

O sistema foi desenvolvido em **Python**, utilizando o **MySQL** como Sistema Gerenciador de Banco de Dados (SGBD), permitindo o gerenciamento das principais informações administrativas, financeiras, fiscais e contábeis de uma empresa.

---

# 🎯 Objetivo

Desenvolver um sistema capaz de realizar o gerenciamento das informações empresariais através de um banco de dados relacional, garantindo consistência, organização e integridade dos dados.

---

# ⚙️ Tecnologias Utilizadas

- Python 3
- MySQL
- MySQL Connector for Python
- SQL
- Git
- GitHub

---

# 📂 Estrutura do Projeto

```
SA/
│
├── crud/
│   ├── cargo.py
│   ├── centro_custo.py
│   ├── certificado_digital.py
│   ├── colaborador.py
│   ├── conta.py
│   ├── contato_empresa.py
│   ├── cronograma_tributario.py
│   ├── documento_fiscal.py
│   ├── empresa.py
│   ├── guia_pagamento.py
│   ├── imposto.py
│   └── ...
│
├── menus/
│   ├── menu_cargo.py
│   ├── menu_centro_custo.py
│   ├── menu_colaborador.py
│   ├── menu_conta.py
│   ├── menu_imposto.py
│   └── ...
├── util/
│
├── database.py
│
├── main.py
│
└── README.md
```

---

# 📋 Funcionalidades

O sistema possui operações completas de **CRUD** para as entidades cadastradas.

## Cadastros

- Cargo
- Centro de Custo
- Certificado Digital
- Colaborador
- Conta Contábil
- Contato da Empresa
- Cronograma Tributário
- Documento Fiscal
- Empresa
- Guia de Pagamento
- Imposto
- Item do Documento Fiscal
- Lançamento Contábil
- Item de Lançamento
- Saldo Contábil Mensal
- Conta Bancária
- Movimentação Bancária
- Conta a Pagar
- Conta a Receber
- Sócio

---

# Funcionalidades disponíveis

Para cada entidade é possível realizar:

- ✅ Cadastro
- ✅ Consulta
- ✅ Listagem
- ✅ Atualização
- ✅ Remoção

---

# 🗄️ Banco de Dados

O banco foi modelado utilizando os princípios da modelagem relacional, contendo diversas entidades relacionadas através de chaves primárias e estrangeiras.

Algumas tabelas presentes no sistema:

- empresa
- colaborador
- cargo
- conta
- centro_custo
- certificado_digital
- contato_empresa
- cronograma_tributario
- documento_fiscal
- item_documento_fiscal
- imposto
- guia_pagamento
- lancamento
- lancamento_item
- saldo_contabil_mensal
- conta_bancaria
- movimentacao_bancaria
- conta_pagar
- conta_receber
- socio
- log_auditoria

---

# 🔗 Relacionamentos

O banco de dados utiliza:

- Chaves Primárias (Primary Keys)
- Chaves Estrangeiras (Foreign Keys)
- Integridade Referencial
- Restrições (CHECK)
- Relacionamentos 1:N

---

# ▶️ Como Executar

## 1. Clone o projeto

```bash
git clone <repositorio>
```

## 2. Instale as dependências

```bash
pip install -r requirements.txt
```

## 3. Configure o banco

Crie um arquivo .env e pegue o exemplo de .env.example:
```
coloque os dados do servidor
```

Informando:

- Host
- porta
- Usuário
- Senha
- Banco de Dados

---

## 4. Execute

```bash
python src/main.py ou clique na ferramenta para rodar o código direto na main.py
```

---

# 📌 Organização

O projeto foi dividido em módulos para facilitar a manutenção.

Cada entidade possui:

- Menu próprio
- Arquivo CRUD próprio
- Consultas SQL organizadas
- Tratamento de exceções
- Controle de conexão com o banco

---

# 🧩 Conceitos Aplicados

Durante o desenvolvimento foram utilizados conceitos como:

- Modelagem Entidade-Relacionamento
- Modelo Relacional
- Normalização
- Integridade Referencial
- SQL (DDL e DML)
- Programação Modular
- Persistência de Dados
- Tratamento de Exceções
- Boas práticas de organização de código

---

# 👨‍💻 Desenvolvido por
Amanda, Augusto, Douglas e Emanuel 