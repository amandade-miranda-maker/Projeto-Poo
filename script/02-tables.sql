-- 1. Tabela: CARGO
CREATE TABLE cargo (
   id_cargo BIGINT AUTO_INCREMENT PRIMARY KEY,
   nome_cargo VARCHAR(100) NOT NULL,
   descricao_cargo TEXT,
   nivel_hierarquico_cargo INT NOT NULL DEFAULT 1,
   salario_base_cargo DECIMAL(15,2),
   status_cargo VARCHAR(20) DEFAULT 'Ativo',
   CONSTRAINT chk_status_cargo CHECK (status_cargo IN ('Ativo', 'Inativo'))
);

-- 2. Tabela: COLABORADOR
CREATE TABLE colaborador (
   id_colaborador BIGINT AUTO_INCREMENT PRIMARY KEY,
   nome_colaborador VARCHAR(255) NOT NULL,
   cpf_colaborador VARCHAR(11) NOT NULL UNIQUE,
   data_nascimento_colaborador DATE,
   email_colaborador VARCHAR(100) NOT NULL UNIQUE,
   telefone_colaborador VARCHAR(20),
   data_admissao_colaborador DATE NOT NULL,
   data_demissao_colaborador DATE,
   status_colaborador VARCHAR(20) DEFAULT 'Ativo',
   id_cargo_colaborador BIGINT NOT NULL,
   FOREIGN KEY (id_cargo_colaborador) REFERENCES cargo(id_cargo),
   CONSTRAINT chk_status_colaborador CHECK (status_colaborador IN ('Ativo', 'Inativo', 'Afastado', 'Demitido'))
);
CREATE INDEX idx_colaborador_cargo ON colaborador(id_cargo_colaborador);


-- 3. Tabela: LOG_AUDITORIA
CREATE TABLE log_auditoria (
   id_log_auditoria BIGINT AUTO_INCREMENT PRIMARY KEY,
   tabela_afetada_log_auditoria VARCHAR(100) NOT NULL,
   id_registro_afetado_log_auditoria BIGINT NOT NULL,
   tipo_operacao_log_auditoria VARCHAR(20) NOT NULL,
   dados_anteriores_log_auditoria TEXT,
   dados_novos_log_auditoria TEXT,
   ip_origem_log_auditoria VARCHAR(45),
   data_hora_log_auditoria TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   CONSTRAINT chk_tipo_operacao_log_auditoria CHECK (tipo_operacao_log_auditoria IN ('INSERT', 'UPDATE', 'DELETE'))
);
CREATE INDEX idx_log_auditoria_tabela ON log_auditoria(tabela_afetada_log_auditoria, id_registro_afetado_log_auditoria);
CREATE INDEX idx_log_auditoria_data ON log_auditoria(data_hora_log_auditoria);


-- 4. Tabela: EMPRESA
CREATE TABLE empresa (
   id_empresa BIGINT AUTO_INCREMENT PRIMARY KEY,
   razao_social_empresa VARCHAR(255) NOT NULL,
   nome_fantasia_empresa VARCHAR(255),
   cnpj_empresa VARCHAR(14) NOT NULL UNIQUE,
   inscricao_estadual_empresa VARCHAR(20),
   inscricao_municipal_empresa VARCHAR(20),
   cnae_principal_empresa VARCHAR(7) NOT NULL,
   regime_tributario_empresa VARCHAR(50) NOT NULL,
   data_abertura_empresa DATE NOT NULL,
   data_cadastro_empresa TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   status_empresa VARCHAR(20) DEFAULT 'Ativo',
   email_empresa VARCHAR(100) NOT NULL,
   telefone_empresa VARCHAR(20) NOT NULL,
   logradouro_empresa VARCHAR(255) NOT NULL,
   numero_empresa VARCHAR(20) NOT NULL,
   complemento_empresa VARCHAR(100),
   bairro_empresa VARCHAR(100) NOT NULL,
   cidade_empresa VARCHAR(100) NOT NULL,
   uf_empresa CHAR(2) NOT NULL,
   cep_empresa VARCHAR(8) NOT NULL,
   capital_social_empresa DECIMAL(15,2) NOT NULL,
   id_colaborador_resp_empresa BIGINT,
   FOREIGN KEY (id_colaborador_resp_empresa) REFERENCES colaborador(id_colaborador),
   CONSTRAINT chk_status_empresa CHECK (status_empresa IN ('Ativo', 'Inativo', 'Suspenso'))
);
CREATE INDEX idx_empresa_cnpj ON empresa(cnpj_empresa);


-- 5. Tabela: CONTATO_EMPRESA
CREATE TABLE contato_empresa (
   id_contato_empresa BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_contato_empresa BIGINT NOT NULL,
   nome_contato_empresa VARCHAR(255) NOT NULL,
   cargo_contato_empresa VARCHAR(100),
   email_contato_empresa VARCHAR(100),
   telefone_contato_empresa VARCHAR(20),
   tipo_contato_empresa VARCHAR(30) NOT NULL,
   principal_contato_empresa BOOLEAN DEFAULT FALSE,
   FOREIGN KEY (id_empresa_contato_empresa) REFERENCES empresa(id_empresa),
   CONSTRAINT chk_tipo_contato_empresa CHECK (tipo_contato_empresa IN ('Financeiro', 'Fiscal', 'Societário', 'Geral'))
);
CREATE INDEX idx_contato_empresa_empresa ON contato_empresa(id_empresa_contato_empresa);


-- 6. Tabela: SOCIO
CREATE TABLE socio (
   id_socio BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_socio BIGINT NOT NULL,
   nome_socio VARCHAR(255) NOT NULL,
   cnpj_cpf_socio VARCHAR(14) NOT NULL,
   percentual_participacao_socio DECIMAL(5,2) NOT NULL,
   data_entrada_socio DATE NOT NULL,
   data_saida_socio DATE,
   administrador_socio BOOLEAN DEFAULT FALSE,
   status_socio VARCHAR(20) DEFAULT 'Ativo',
   FOREIGN KEY (id_empresa_socio) REFERENCES empresa(id_empresa),
   CONSTRAINT chk_percentual_participacao_socio CHECK (percentual_participacao_socio BETWEEN 0 AND 100),
   CONSTRAINT chk_status_socio CHECK (status_socio IN ('Ativo', 'Inativo'))
);
CREATE INDEX idx_socio_empresa ON socio(id_empresa_socio);


-- 7. Tabela: CERTIFICADO_DIGITAL
CREATE TABLE certificado_digital (
   id_certificado_digital BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_certificado_digital BIGINT NOT NULL,
   tipo_certificado_digital VARCHAR(10) NOT NULL,
   numero_serie_certificado_digital VARCHAR(100) NOT NULL UNIQUE,
   emissor_certificado_digital VARCHAR(255),
   data_emissao_certificado_digital DATE NOT NULL,
   data_validade_certificado_digital DATE NOT NULL,
   arquivo_certificado_digital VARCHAR(512),
   -- ALERTA DE SEGURANÇA: nunca armazenar a senha do certificado em texto puro.
   -- Este campo deve guardar apenas uma referência/token de um cofre de segredos
   -- (ex.: Vault, AWS Secrets Manager), nunca a senha em si.
   referencia_senha_cofre_certificado_digital VARCHAR(255),
   status_certificado_digital VARCHAR(20) DEFAULT 'Válido',
   FOREIGN KEY (id_empresa_certificado_digital) REFERENCES empresa(id_empresa),
   CONSTRAINT chk_tipo_certificado_digital CHECK (tipo_certificado_digital IN ('A1', 'A3')),
   CONSTRAINT chk_status_certificado_digital CHECK (status_certificado_digital IN ('Válido', 'Vencido', 'Revogado'))
);
CREATE INDEX idx_certificado_digital_validade ON certificado_digital(data_validade_certificado_digital);


-- 8. Tabela: DOCUMENTO_FISCAL
CREATE TABLE documento_fiscal (
   id_documento_fiscal BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_documento_fiscal BIGINT NOT NULL,
   tipo_documento_fiscal VARCHAR(10) NOT NULL,
   direcao_documento_fiscal CHAR(1) NOT NULL,
   numero_documento_fiscal INT NOT NULL,
   serie_documento_fiscal VARCHAR(10) NOT NULL,
   chave_acesso_documento_fiscal CHAR(44) NOT NULL UNIQUE,
   data_emissao_documento_fiscal TIMESTAMP NOT NULL,
   data_entrada_sistema_documento_fiscal TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   cfop_documento_fiscal VARCHAR(4) NOT NULL,
   natureza_operacao_documento_fiscal VARCHAR(255) NOT NULL,
   valor_produtos_documento_fiscal DECIMAL(15,2) NOT NULL,
   valor_frete_documento_fiscal DECIMAL(15,2) DEFAULT 0.00,
   valor_desconto_documento_fiscal DECIMAL(15,2) DEFAULT 0.00,
   valor_icms_documento_fiscal DECIMAL(15,2) DEFAULT 0.00,
   valor_ipi_documento_fiscal DECIMAL(15,2) DEFAULT 0.00,
   valor_pis_documento_fiscal DECIMAL(15,2) DEFAULT 0.00,
   valor_cofins_documento_fiscal DECIMAL(15,2) DEFAULT 0.00,
   valor_total_documento_fiscal DECIMAL(15,2) NOT NULL,
   status_documento_fiscal VARCHAR(20) NOT NULL,
   arquivo_xml_documento_fiscal VARCHAR(512) NOT NULL,
   arquivo_danfe_pdf_documento_fiscal VARCHAR(512),
   nome_contraparte_documento_fiscal VARCHAR(255) NOT NULL,
   cnpj_cpf_contraparte_documento_fiscal VARCHAR(14) NOT NULL,
   FOREIGN KEY (id_empresa_documento_fiscal) REFERENCES empresa(id_empresa),
   CONSTRAINT chk_direcao_documento_fiscal CHECK (direcao_documento_fiscal IN ('E', 'S')),
   CONSTRAINT chk_status_documento_fiscal CHECK (status_documento_fiscal IN ('Autorizado', 'Cancelado', 'Inutilizado'))
);
CREATE INDEX idx_documento_fiscal_chave_acesso ON documento_fiscal(chave_acesso_documento_fiscal);
CREATE INDEX idx_documento_fiscal_empresa_data ON documento_fiscal(id_empresa_documento_fiscal, data_emissao_documento_fiscal);


-- 9. Tabela: ITEM_DOCUMENTO_FISCAL
CREATE TABLE item_documento_fiscal (
   id_item_documento_fiscal BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_documento_fiscal_item_documento_fiscal BIGINT NOT NULL,
   numero_item_documento_fiscal INT NOT NULL, -- posição do item dentro do documento
   codigo_produto_item_documento_fiscal VARCHAR(60) NOT NULL,
   descricao_produto_item_documento_fiscal VARCHAR(255) NOT NULL,
   ncm_item_documento_fiscal VARCHAR(8),
   cfop_item_documento_fiscal VARCHAR(4) NOT NULL,
   unidade_item_documento_fiscal VARCHAR(10),
   quantidade_item_documento_fiscal DECIMAL(15,4) NOT NULL,
   valor_unitario_item_documento_fiscal DECIMAL(15,4) NOT NULL,
   valor_total_item_documento_fiscal DECIMAL(15,2) NOT NULL,
   valor_icms_item_documento_fiscal DECIMAL(15,2) DEFAULT 0.00,
   valor_ipi_item_documento_fiscal DECIMAL(15,2) DEFAULT 0.00,
   id_conta_item_documento_fiscal BIGINT, -- classificação contábil do item (FK abaixo, criada após "conta")
   FOREIGN KEY (id_documento_fiscal_item_documento_fiscal) REFERENCES documento_fiscal(id_documento_fiscal) ON DELETE CASCADE,
   -- ADICIONADO (v4): impede dois itens com o mesmo número dentro do mesmo documento
   UNIQUE KEY uq_item_documento_fiscal_numero (id_documento_fiscal_item_documento_fiscal, numero_item_documento_fiscal)
);
CREATE INDEX idx_item_documento_fiscal_documento ON item_documento_fiscal(id_documento_fiscal_item_documento_fiscal);


-- 10. Tabela: IMPOSTO (catálogo de tributos)
CREATE TABLE imposto (
   id_imposto BIGINT AUTO_INCREMENT PRIMARY KEY,
   nome_imposto VARCHAR(50) NOT NULL UNIQUE, -- ICMS, IPI, PIS, COFINS, ISS, IRPJ, CSLL, Simples Nacional...
   esfera_imposto VARCHAR(20) NOT NULL,
   aliquota_padrao_imposto DECIMAL(6,4),
   status_imposto VARCHAR(20) DEFAULT 'Ativo',
   CONSTRAINT chk_esfera_imposto CHECK (esfera_imposto IN ('Federal', 'Estadual', 'Municipal')),
   CONSTRAINT chk_status_imposto CHECK (status_imposto IN ('Ativo', 'Inativo'))
);


-- 11. Tabela: CRONOGRAMA_TRIBUTARIO
-- MELHORIA: "tipo_imposto" (texto livre) foi substituído por FK para a tabela
-- IMPOSTO, evitando divergência de grafia (ex.: "ICMS" vs "Icms").
CREATE TABLE cronograma_tributario (
   id_cronograma_tributario BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_cronograma_tributario BIGINT NOT NULL,
   id_imposto_cronograma_tributario BIGINT NOT NULL,
   competencia_cronograma_tributario CHAR(7) NOT NULL,
   data_vencimento_cronograma_tributario DATE NOT NULL,
   valor_calculado_cronograma_tributario DECIMAL(15,2) NOT NULL,
   valor_pago_cronograma_tributario DECIMAL(15,2),
   data_pagamento_cronograma_tributario DATE,
   status_cronograma_tributario VARCHAR(20) DEFAULT 'Pendente',
   comprovante_pagamento_cronograma_tributario VARCHAR(512),
   id_colaborador_resp_cronograma_tributario BIGINT,
   FOREIGN KEY (id_empresa_cronograma_tributario) REFERENCES empresa(id_empresa),
   FOREIGN KEY (id_imposto_cronograma_tributario) REFERENCES imposto(id_imposto),
   FOREIGN KEY (id_colaborador_resp_cronograma_tributario) REFERENCES colaborador(id_colaborador),
   CONSTRAINT chk_status_cronograma_tributario CHECK (status_cronograma_tributario IN ('Pendente', 'Pago', 'Atrasado', 'Isento'))
);
CREATE INDEX idx_cronograma_tributario_vencimento ON cronograma_tributario(data_vencimento_cronograma_tributario, status_cronograma_tributario);


-- 12. Tabela: GUIA_PAGAMENTO
CREATE TABLE guia_pagamento (
   id_guia_pagamento BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_cronograma_tributario_guia_pagamento BIGINT NOT NULL,
   codigo_barras_guia_pagamento VARCHAR(48),
   linha_digitavel_guia_pagamento VARCHAR(60),
   data_emissao_guia_pagamento DATE NOT NULL,
   data_vencimento_guia_pagamento DATE NOT NULL,
   valor_guia_pagamento DECIMAL(15,2) NOT NULL,
   arquivo_guia_pagamento VARCHAR(512),
   status_guia_pagamento VARCHAR(20) DEFAULT 'Emitida',
   FOREIGN KEY (id_cronograma_tributario_guia_pagamento) REFERENCES cronograma_tributario(id_cronograma_tributario),
   CONSTRAINT chk_status_guia_pagamento CHECK (status_guia_pagamento IN ('Emitida', 'Paga', 'Vencida', 'Cancelada'))
);
CREATE INDEX idx_guia_pagamento_cronograma ON guia_pagamento(id_cronograma_tributario_guia_pagamento);


-- 13. Tabela: CONTA (plano de contas)
CREATE TABLE conta (
   id_conta BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_conta BIGINT NOT NULL,
   codigo_conta VARCHAR(50) NOT NULL,
   nome_conta VARCHAR(150) NOT NULL,
   tipo_conta VARCHAR(30) NOT NULL,
   id_conta_pai_conta BIGINT,
   natureza_conta CHAR(1) NOT NULL,
   FOREIGN KEY (id_empresa_conta) REFERENCES empresa(id_empresa),
   FOREIGN KEY (id_conta_pai_conta) REFERENCES conta(id_conta),
   CONSTRAINT chk_natureza_conta CHECK (natureza_conta IN ('D', 'C')),
   CONSTRAINT chk_tipo_conta CHECK (tipo_conta IN ('Sintética', 'Analítica'))
);


-- Agora que "conta" existe, fechamos a FK pendente de item_documento_fiscal
ALTER TABLE item_documento_fiscal
   ADD CONSTRAINT fk_item_documento_fiscal_conta
   FOREIGN KEY (id_conta_item_documento_fiscal) REFERENCES conta(id_conta);


-- 14. Tabela: CENTRO_CUSTO
CREATE TABLE centro_custo (
   id_centro_custo BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_centro_custo BIGINT NOT NULL,
   codigo_centro_custo VARCHAR(30) NOT NULL,
   nome_centro_custo VARCHAR(150) NOT NULL,
   id_centro_custo_pai_centro_custo BIGINT,
   status_centro_custo VARCHAR(20) DEFAULT 'Ativo',
   FOREIGN KEY (id_empresa_centro_custo) REFERENCES empresa(id_empresa),
   FOREIGN KEY (id_centro_custo_pai_centro_custo) REFERENCES centro_custo(id_centro_custo),
   CONSTRAINT chk_status_centro_custo CHECK (status_centro_custo IN ('Ativo', 'Inativo')),
   -- CORRIGIDO (v4): constraint nomeada, para consistência com as demais
   UNIQUE KEY uq_centro_custo_empresa_codigo (id_empresa_centro_custo, codigo_centro_custo)
);


-- 15. Tabela: LANCAMENTO (cabeçalho)
CREATE TABLE lancamento (
   id_lancamento BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_lancamento BIGINT NOT NULL,
   data_lancamento DATE NOT NULL,
   competencia_lancamento CHAR(7) NOT NULL,
   historico_geral_lancamento TEXT NOT NULL,
   id_documento_fiscal_origem_lancamento BIGINT,
   tipo_origem_lancamento VARCHAR(30) DEFAULT 'Manual',
   id_colaborador_resp_lancamento BIGINT,
   FOREIGN KEY (id_empresa_lancamento) REFERENCES empresa(id_empresa),
   FOREIGN KEY (id_documento_fiscal_origem_lancamento) REFERENCES documento_fiscal(id_documento_fiscal),
   FOREIGN KEY (id_colaborador_resp_lancamento) REFERENCES colaborador(id_colaborador)
);
CREATE INDEX idx_lancamento_competencia ON lancamento(id_empresa_lancamento, competencia_lancamento);


-- 16. Tabela: LANCAMENTO_ITEM
-- MELHORIA: adicionada FK opcional para CENTRO_CUSTO, permitindo rateio de
-- despesas/receitas por centro de custo diretamente na partida contábil.
CREATE TABLE lancamento_item (
   id_lancamento_item BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_lancamento_lancamento_item BIGINT NOT NULL,
   id_conta_lancamento_item BIGINT NOT NULL,
   id_centro_custo_lancamento_item BIGINT,
   tipo_movimento_lancamento_item CHAR(1) NOT NULL,
   valor_lancamento_item DECIMAL(15,2) NOT NULL,
   FOREIGN KEY (id_lancamento_lancamento_item) REFERENCES lancamento(id_lancamento) ON DELETE CASCADE,
   FOREIGN KEY (id_conta_lancamento_item) REFERENCES conta(id_conta),
   FOREIGN KEY (id_centro_custo_lancamento_item) REFERENCES centro_custo(id_centro_custo),
   CONSTRAINT chk_tipo_movimento_lancamento_item CHECK (tipo_movimento_lancamento_item IN ('D', 'C'))
);


-- 17. Tabela: SALDO_CONTABIL_MENSAL (motor de relatórios rápidos)
CREATE TABLE saldo_contabil_mensal (
   id_saldo_contabil_mensal BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_saldo_contabil_mensal BIGINT NOT NULL,
   id_conta_saldo_contabil_mensal BIGINT NOT NULL,
   competencia_saldo_contabil_mensal CHAR(7) NOT NULL,
   saldo_inicial_saldo_contabil_mensal DECIMAL(15,2) NOT NULL DEFAULT 0.00,
   total_debitos_saldo_contabil_mensal DECIMAL(15,2) NOT NULL DEFAULT 0.00,
   total_creditos_saldo_contabil_mensal DECIMAL(15,2) NOT NULL DEFAULT 0.00,
   saldo_final_saldo_contabil_mensal DECIMAL(15,2) NOT NULL DEFAULT 0.00,
   FOREIGN KEY (id_empresa_saldo_contabil_mensal) REFERENCES empresa(id_empresa),
   FOREIGN KEY (id_conta_saldo_contabil_mensal) REFERENCES conta(id_conta),
   UNIQUE KEY uq_empresa_conta_competencia_saldo_contabil_mensal (
       id_empresa_saldo_contabil_mensal,
       id_conta_saldo_contabil_mensal,
       competencia_saldo_contabil_mensal
   )
);


-- 18. Tabela: CONTA_BANCARIA
CREATE TABLE conta_bancaria (
   id_conta_bancaria BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_conta_bancaria BIGINT NOT NULL,
   banco_conta_bancaria VARCHAR(100) NOT NULL,
   codigo_banco_conta_bancaria VARCHAR(10) NOT NULL,
   agencia_conta_bancaria VARCHAR(20) NOT NULL,
   numero_conta_conta_bancaria VARCHAR(30) NOT NULL,
   tipo_conta_bancaria VARCHAR(20) NOT NULL,
   saldo_atual_conta_bancaria DECIMAL(15,2) NOT NULL DEFAULT 0.00,
   status_conta_bancaria VARCHAR(20) DEFAULT 'Ativa',
   FOREIGN KEY (id_empresa_conta_bancaria) REFERENCES empresa(id_empresa),
   CONSTRAINT chk_tipo_conta_bancaria CHECK (tipo_conta_bancaria IN ('Corrente', 'Poupança', 'Aplicação')),
   CONSTRAINT chk_status_conta_bancaria CHECK (status_conta_bancaria IN ('Ativa', 'Inativa', 'Encerrada')),
   -- CORRIGIDO (v4): constraint nomeada, para consistência com as demais
   UNIQUE KEY uq_conta_bancaria_dados_bancarios (id_empresa_conta_bancaria, codigo_banco_conta_bancaria, agencia_conta_bancaria, numero_conta_conta_bancaria)
);


-- 19. Tabela: MOVIMENTACAO_BANCARIA
CREATE TABLE movimentacao_bancaria (
   id_movimentacao_bancaria BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_conta_bancaria_movimentacao_bancaria BIGINT NOT NULL,
   data_movimentacao_bancaria DATE NOT NULL,
   tipo_movimentacao_bancaria CHAR(1) NOT NULL,
   valor_movimentacao_bancaria DECIMAL(15,2) NOT NULL,
   descricao_movimentacao_bancaria VARCHAR(255) NOT NULL,
   documento_referencia_movimentacao_bancaria VARCHAR(100),
   conciliado_movimentacao_bancaria BOOLEAN DEFAULT FALSE,
   id_lancamento_movimentacao_bancaria BIGINT, -- lançamento contábil gerado na conciliação
   FOREIGN KEY (id_conta_bancaria_movimentacao_bancaria) REFERENCES conta_bancaria(id_conta_bancaria),
   FOREIGN KEY (id_lancamento_movimentacao_bancaria) REFERENCES lancamento(id_lancamento),
   CONSTRAINT chk_tipo_movimentacao_bancaria CHECK (tipo_movimentacao_bancaria IN ('D', 'C'))
);
CREATE INDEX idx_movimentacao_bancaria_conta_data ON movimentacao_bancaria(id_conta_bancaria_movimentacao_bancaria, data_movimentacao_bancaria);


-- 20. Tabela: CONTA_PAGAR
CREATE TABLE conta_pagar (
   id_conta_pagar BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_conta_pagar BIGINT NOT NULL,
   fornecedor_conta_pagar VARCHAR(255) NOT NULL,
   cnpj_cpf_fornecedor_conta_pagar VARCHAR(14),
   descricao_conta_pagar VARCHAR(255) NOT NULL,
   valor_original_conta_pagar DECIMAL(15,2) NOT NULL,
   valor_pago_conta_pagar DECIMAL(15,2),
   data_emissao_conta_pagar DATE NOT NULL,
   data_vencimento_conta_pagar DATE NOT NULL,
   data_pagamento_conta_pagar DATE,
   id_conta_bancaria_conta_pagar BIGINT,
   id_documento_fiscal_conta_pagar BIGINT,
   status_conta_pagar VARCHAR(20) DEFAULT 'Pendente',
   FOREIGN KEY (id_empresa_conta_pagar) REFERENCES empresa(id_empresa),
   FOREIGN KEY (id_conta_bancaria_conta_pagar) REFERENCES conta_bancaria(id_conta_bancaria),
   FOREIGN KEY (id_documento_fiscal_conta_pagar) REFERENCES documento_fiscal(id_documento_fiscal),
   CONSTRAINT chk_status_conta_pagar CHECK (status_conta_pagar IN ('Pendente', 'Pago', 'Atrasado', 'Cancelado'))
);
CREATE INDEX idx_conta_pagar_vencimento ON conta_pagar(id_empresa_conta_pagar, data_vencimento_conta_pagar, status_conta_pagar);


-- 21. Tabela: CONTA_RECEBER
CREATE TABLE conta_receber (
   id_conta_receber BIGINT AUTO_INCREMENT PRIMARY KEY,
   id_empresa_conta_receber BIGINT NOT NULL,
   cliente_conta_receber VARCHAR(255) NOT NULL,
   cnpj_cpf_cliente_conta_receber VARCHAR(14),
   descricao_conta_receber VARCHAR(255) NOT NULL,
   valor_original_conta_receber DECIMAL(15,2) NOT NULL,
   valor_recebido_conta_receber DECIMAL(15,2),
   data_emissao_conta_receber DATE NOT NULL,
   data_vencimento_conta_receber DATE NOT NULL,
   data_recebimento_conta_receber DATE,
   id_conta_bancaria_conta_receber BIGINT,
   id_documento_fiscal_conta_receber BIGINT,
   status_conta_receber VARCHAR(20) DEFAULT 'Pendente',
   FOREIGN KEY (id_empresa_conta_receber) REFERENCES empresa(id_empresa),
   FOREIGN KEY (id_conta_bancaria_conta_receber) REFERENCES conta_bancaria(id_conta_bancaria),
   FOREIGN KEY (id_documento_fiscal_conta_receber) REFERENCES documento_fiscal(id_documento_fiscal),
   CONSTRAINT chk_status_conta_receber CHECK (status_conta_receber IN ('Pendente', 'Recebido', 'Atrasado', 'Cancelado'))
);
CREATE INDEX idx_conta_receber_vencimento ON conta_receber(id_empresa_conta_receber, data_vencimento_conta_receber, status_conta_receber);

-- ==============================================================================
-- SCRIPT DE CORREÇÃO: colunas que armazenam dados criptografados
-- (AES_ENCRYPT + TO_BASE64) precisam de espaço maior que o tamanho do dado
-- original em texto puro, pois o resultado cifrado + base64 é bem maior.
--
-- Rode este script ANTES de executar os seus INSERTs.
-- ==============================================================================

-- 1) colaborador.cpf_colaborador
ALTER TABLE colaborador
    MODIFY COLUMN cpf_colaborador VARCHAR(255) NOT NULL;

-- 2) empresa.cnpj_empresa
ALTER TABLE empresa
    MODIFY COLUMN cnpj_empresa VARCHAR(255) NOT NULL;

-- 3) socio.cnpj_cpf_socio
ALTER TABLE socio
    MODIFY COLUMN cnpj_cpf_socio VARCHAR(255) NOT NULL;

-- 4) documento_fiscal.cnpj_cpf_contraparte_documento_fiscal
ALTER TABLE documento_fiscal
    MODIFY COLUMN cnpj_cpf_contraparte_documento_fiscal VARCHAR(255) NOT NULL;

-- 5) conta_pagar.cnpj_cpf_fornecedor_conta_pagar
ALTER TABLE conta_pagar
    MODIFY COLUMN cnpj_cpf_fornecedor_conta_pagar VARCHAR(255);

-- 6) conta_receber.cnpj_cpf_cliente_conta_receber
ALTER TABLE conta_receber
    MODIFY COLUMN cnpj_cpf_cliente_conta_receber VARCHAR(255);

-- 7) conta_bancaria.agencia_conta_bancaria
ALTER TABLE conta_bancaria
    MODIFY COLUMN agencia_conta_bancaria VARCHAR(255) NOT NULL;

-- 8) conta_bancaria.numero_conta_conta_bancaria
ALTER TABLE conta_bancaria
    MODIFY COLUMN numero_conta_conta_bancaria VARCHAR(255) NOT NULL;

-- ==============================================================================
-- Observações:
-- - As UNIQUE KEYS existentes (cpf_colaborador, cnpj_empresa, e a composta
--   uq_conta_bancaria_dados_bancarios) continuam válidas: MySQL/InnoDB (Dynamic
--   ou Compressed row format, padrão a partir do MySQL 5.7+) suporta índices
--   bem acima do necessário aqui, então nenhuma constraint foi removida.
-- - Nenhuma outra estrutura (FKs, CHECKs, tipos de outras colunas) foi alterada.
-- ==============================================================================

ALTER TABLE guia_pagamento
    MODIFY COLUMN codigo_barras_guia_pagamento VARCHAR(255);

