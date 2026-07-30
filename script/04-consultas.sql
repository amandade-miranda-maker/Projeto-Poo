-- 1) Empresas ativas com o nome do colaborador responsável e o cargo dele
SELECT
    e.razao_social_empresa,
    e.uf_empresa,
    c.nome_colaborador,
    ca.nome_cargo
FROM empresa e
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
WHERE e.status_empresa = 'Ativo'
ORDER BY e.razao_social_empresa;
 
-- 2) Colaboradores que respondem por mais de uma empresa, com o cargo
SELECT
    c.nome_colaborador,
    ca.nome_cargo,
    COUNT(e.id_empresa) AS qtd_empresas_responsavel
FROM colaborador c
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
JOIN empresa e ON e.id_colaborador_resp_empresa = c.id_colaborador
GROUP BY c.id_colaborador, c.nome_colaborador, ca.nome_cargo
HAVING COUNT(e.id_empresa) > 1
ORDER BY qtd_empresas_responsavel DESC;
 
-- 3) Média salarial por cargo dos colaboradores responsáveis por empresas ativas
SELECT
    ca.nome_cargo,
    COUNT(DISTINCT c.id_colaborador) AS qtd_colaboradores,
    ROUND(AVG(ca.salario_base_cargo), 2) AS media_salarial
FROM colaborador c
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
JOIN empresa e ON e.id_colaborador_resp_empresa = c.id_colaborador
WHERE e.status_empresa = 'Ativo'
GROUP BY ca.nome_cargo
ORDER BY media_salarial DESC;
 
-- 4) Colaboradores demitidos que ainda constam como responsáveis por empresa ativa (inconsistência)
SELECT
    c.nome_colaborador,
    c.status_colaborador,
    ca.nome_cargo,
    e.razao_social_empresa
FROM colaborador c
JOIN empresa e ON e.id_colaborador_resp_empresa = c.id_colaborador
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
WHERE c.status_colaborador = 'Demitido'
  AND e.status_empresa = 'Ativo';
 
-- 5) Contatos principais das empresas, com colaborador responsável e cargo dele
SELECT
    ce.nome_contato_empresa,
    ce.cargo_contato_empresa,
    e.razao_social_empresa,
    c.nome_colaborador AS responsavel_interno,
    ca.nome_cargo AS cargo_responsavel
FROM contato_empresa ce
JOIN empresa e ON e.id_empresa = ce.id_empresa_contato_empresa
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
WHERE ce.principal_contato_empresa = 1
ORDER BY e.razao_social_empresa;
 
-- 6) Auditoria de alterações (UPDATE) feitas na tabela colaborador, com o cargo atual
SELECT
    la.tipo_operacao_log_auditoria,
    la.data_hora_log_auditoria,
    la.ip_origem_log_auditoria,
    c.nome_colaborador,
    ca.nome_cargo
FROM log_auditoria la
JOIN colaborador c ON c.id_colaborador = la.id_registro_afetado_log_auditoria
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
WHERE la.tabela_afetada_log_auditoria = 'colaborador'
  AND la.tipo_operacao_log_auditoria = 'UPDATE'
ORDER BY la.data_hora_log_auditoria DESC;
 
 
-- 7) Sócios administradores ativos, com a empresa e o colaborador responsável
SELECT
    s.nome_socio,
    s.percentual_participacao_socio,
    e.razao_social_empresa,
    c.nome_colaborador AS responsavel_interno
FROM socio s
JOIN empresa e ON e.id_empresa = s.id_empresa_socio
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
WHERE s.administrador_socio = 1
  AND s.status_socio = 'Ativo'
ORDER BY s.percentual_participacao_socio DESC;
 
-- 8) Quantidade de sócios por empresa, com colaborador responsável e cargo dele
SELECT
    e.razao_social_empresa,
    c.nome_colaborador AS responsavel_interno,
    ca.nome_cargo,
    COUNT(s.id_socio) AS qtd_socios
FROM socio s
JOIN empresa e ON e.id_empresa = s.id_empresa_socio
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
GROUP BY e.id_empresa, e.razao_social_empresa, c.nome_colaborador, ca.nome_cargo
ORDER BY qtd_socios DESC;
 
-- 9) Sócios com participação acima de 50%, razão social/UF da empresa e cargo do responsável
SELECT
    s.nome_socio,
    s.percentual_participacao_socio,
    e.razao_social_empresa,
    e.uf_empresa,
    ca.nome_cargo AS cargo_responsavel
FROM socio s
JOIN empresa e ON e.id_empresa = s.id_empresa_socio
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
WHERE s.percentual_participacao_socio > 50
ORDER BY s.percentual_participacao_socio DESC;
 
-- 10) Sócios inativos (com data de saída registrada), empresa e colaborador responsável
SELECT
    s.nome_socio,
    s.data_entrada_socio,
    s.data_saida_socio,
    e.razao_social_empresa,
    c.nome_colaborador AS responsavel_interno
FROM socio s
JOIN empresa e ON e.id_empresa = s.id_empresa_socio
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
WHERE s.status_socio = 'Inativo'
ORDER BY s.data_saida_socio DESC;
 
 
-- 11) Certificados digitais vencidos, com empresa e colaborador responsável
SELECT
    cd.numero_serie_certificado_digital,
    cd.data_validade_certificado_digital,
    e.razao_social_empresa,
    c.nome_colaborador AS responsavel_interno
FROM certificado_digital cd
JOIN empresa e ON e.id_empresa = cd.id_empresa_certificado_digital
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
WHERE cd.status_certificado_digital = 'Vencido'
ORDER BY cd.data_validade_certificado_digital;
 
-- 12) Quantidade de certificados por status e cargo do colaborador responsável
SELECT
    cd.status_certificado_digital,
    ca.nome_cargo,
    COUNT(cd.id_certificado_digital) AS qtd_certificados
FROM certificado_digital cd
JOIN empresa e ON e.id_empresa = cd.id_empresa_certificado_digital
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
GROUP BY cd.status_certificado_digital, ca.nome_cargo
ORDER BY qtd_certificados DESC;
 
-- 13) Certificados A3 emitidos pela AC Soluti, com empresa e colaborador responsável
SELECT
    cd.numero_serie_certificado_digital,
    cd.data_emissao_certificado_digital,
    e.razao_social_empresa,
    c.nome_colaborador AS responsavel_interno
FROM certificado_digital cd
JOIN empresa e ON e.id_empresa = cd.id_empresa_certificado_digital
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
WHERE cd.tipo_certificado_digital = 'A3'
  AND cd.emissor_certificado_digital = 'AC Soluti'
ORDER BY cd.data_emissao_certificado_digital DESC;
 
 
 
-- 14) Documentos fiscais de saída com valor total acima de 40.000, empresa e responsável
SELECT
    df.numero_documento_fiscal,
    df.valor_total_documento_fiscal,
    e.razao_social_empresa,
    c.nome_colaborador AS responsavel_interno
FROM documento_fiscal df
JOIN empresa e ON e.id_empresa = df.id_empresa_documento_fiscal
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
WHERE df.direcao_documento_fiscal = 'S'
  AND df.valor_total_documento_fiscal > 40000
ORDER BY df.valor_total_documento_fiscal DESC;
 
-- 15) Itens de "Notebook Dell" vendidos, com o documento fiscal e a empresa emissora
SELECT
    idf.descricao_produto_item_documento_fiscal,
    idf.quantidade_item_documento_fiscal,
    idf.valor_total_item_documento_fiscal,
    df.numero_documento_fiscal,
    e.razao_social_empresa
FROM item_documento_fiscal idf
JOIN documento_fiscal df ON df.id_documento_fiscal = idf.id_documento_fiscal_item_documento_fiscal
JOIN empresa e ON e.id_empresa = df.id_empresa_documento_fiscal
WHERE idf.descricao_produto_item_documento_fiscal = 'Notebook Dell'
ORDER BY idf.valor_total_item_documento_fiscal DESC;
 
-- 16) Soma do valor total de documentos fiscais por CFOP, UF e responsável interno
SELECT
    df.cfop_documento_fiscal,
    e.uf_empresa,
    c.nome_colaborador AS responsavel_interno,
    SUM(df.valor_total_documento_fiscal) AS valor_total_acumulado
FROM documento_fiscal df
JOIN empresa e ON e.id_empresa = df.id_empresa_documento_fiscal
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
GROUP BY df.cfop_documento_fiscal, e.uf_empresa, c.nome_colaborador
ORDER BY valor_total_acumulado DESC;
 
-- 17) Documentos fiscais cancelados, com empresa e colaborador responsável
SELECT
    df.numero_documento_fiscal,
    df.tipo_documento_fiscal,
    df.data_emissao_documento_fiscal,
    e.razao_social_empresa,
    c.nome_colaborador AS responsavel_interno
FROM documento_fiscal df
JOIN empresa e ON e.id_empresa = df.id_empresa_documento_fiscal
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
WHERE df.status_documento_fiscal = 'Cancelado'
ORDER BY df.data_emissao_documento_fiscal DESC;
 
-- 18) Quantidade e valor total de itens por documento fiscal e empresa
SELECT
    df.numero_documento_fiscal,
    e.nome_fantasia_empresa,
    COUNT(idf.id_item_documento_fiscal) AS qtd_itens,
    SUM(idf.valor_total_item_documento_fiscal) AS valor_total_itens
FROM item_documento_fiscal idf
JOIN documento_fiscal df ON df.id_documento_fiscal = idf.id_documento_fiscal_item_documento_fiscal
JOIN empresa e ON e.id_empresa = df.id_empresa_documento_fiscal
GROUP BY df.id_documento_fiscal, df.numero_documento_fiscal, e.nome_fantasia_empresa
ORDER BY valor_total_itens DESC;
 
-- 19) Documentos fiscais de entrada, por regime tributário da empresa e responsável interno
SELECT
    df.numero_documento_fiscal,
    e.regime_tributario_empresa,
    c.nome_colaborador AS responsavel_interno
FROM documento_fiscal df
JOIN empresa e ON e.id_empresa = df.id_empresa_documento_fiscal
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
WHERE df.direcao_documento_fiscal = 'E'
ORDER BY e.regime_tributario_empresa;
 
 
-- 20) Cronograma tributário pendente, com empresa e imposto correspondente
SELECT
    ct.competencia_cronograma_tributario,
    ct.data_vencimento_cronograma_tributario,
    ct.valor_calculado_cronograma_tributario,
    e.razao_social_empresa,
    i.nome_imposto
FROM cronograma_tributario ct
JOIN empresa e ON e.id_empresa = ct.id_empresa_cronograma_tributario
JOIN imposto i ON i.id_imposto = ct.id_imposto_cronograma_tributario
WHERE ct.status_cronograma_tributario = 'Pendente'
ORDER BY ct.data_vencimento_cronograma_tributario;
 
-- 21) Cronograma tributário atrasado, com empresa, imposto e colaborador responsável
SELECT
    ct.data_vencimento_cronograma_tributario,
    ct.valor_calculado_cronograma_tributario,
    e.razao_social_empresa,
    i.nome_imposto,
    c.nome_colaborador AS responsavel_pagamento
FROM cronograma_tributario ct
JOIN empresa e ON e.id_empresa = ct.id_empresa_cronograma_tributario
JOIN imposto i ON i.id_imposto = ct.id_imposto_cronograma_tributario
JOIN colaborador c ON c.id_colaborador = ct.id_colaborador_resp_cronograma_tributario
WHERE ct.status_cronograma_tributario = 'Atrasado'
ORDER BY ct.data_vencimento_cronograma_tributario;
 
-- 22) Soma do valor calculado por imposto e UF da empresa
SELECT
    i.nome_imposto,
    e.uf_empresa,
    SUM(ct.valor_calculado_cronograma_tributario) AS valor_total_calculado
FROM cronograma_tributario ct
JOIN empresa e ON e.id_empresa = ct.id_empresa_cronograma_tributario
JOIN imposto i ON i.id_imposto = ct.id_imposto_cronograma_tributario
GROUP BY i.nome_imposto, e.uf_empresa
ORDER BY valor_total_calculado DESC;
 
-- 23) Cronograma tributário pago, com o colaborador responsável e o respectivo cargo
SELECT
    ct.competencia_cronograma_tributario,
    ct.valor_pago_cronograma_tributario,
    c.nome_colaborador AS responsavel_pagamento,
    ca.nome_cargo
FROM cronograma_tributario ct
JOIN colaborador c ON c.id_colaborador = ct.id_colaborador_resp_cronograma_tributario
JOIN cargo ca ON ca.id_cargo = c.id_cargo_colaborador
WHERE ct.status_cronograma_tributario = 'Pago'
ORDER BY ct.valor_pago_cronograma_tributario DESC;
 
-- 24) Impostos de esfera federal com cronograma pendente, com a razão social da empresa
SELECT
    i.nome_imposto,
    i.aliquota_padrao_imposto,
    ct.data_vencimento_cronograma_tributario,
    e.razao_social_empresa
FROM cronograma_tributario ct
JOIN imposto i ON i.id_imposto = ct.id_imposto_cronograma_tributario
JOIN empresa e ON e.id_empresa = ct.id_empresa_cronograma_tributario
WHERE i.esfera_imposto = 'Federal'
  AND ct.status_cronograma_tributario = 'Pendente'
ORDER BY ct.data_vencimento_cronograma_tributario;
 
 
-- 25) Empresas com saldo final negativo em determinada conta contábil
SELECT
    e.razao_social_empresa,
    ct.nome_conta,
    scm.competencia_saldo_contabil_mensal,
    scm.saldo_final_saldo_contabil_mensal
FROM saldo_contabil_mensal scm
JOIN empresa e ON e.id_empresa = scm.id_empresa_saldo_contabil_mensal
JOIN conta ct ON ct.id_conta = scm.id_conta_saldo_contabil_mensal
WHERE scm.saldo_final_saldo_contabil_mensal < 0
ORDER BY scm.saldo_final_saldo_contabil_mensal;
 
-- 26) Total de débitos e créditos por competência, empresa e conta contábil
SELECT
    scm.competencia_saldo_contabil_mensal,
    e.nome_fantasia_empresa,
    ct.nome_conta,
    SUM(scm.total_debitos_saldo_contabil_mensal) AS total_debitos,
    SUM(scm.total_creditos_saldo_contabil_mensal) AS total_creditos
FROM saldo_contabil_mensal scm
JOIN empresa e ON e.id_empresa = scm.id_empresa_saldo_contabil_mensal
JOIN conta ct ON ct.id_conta = scm.id_conta_saldo_contabil_mensal
GROUP BY scm.competencia_saldo_contabil_mensal, e.nome_fantasia_empresa, ct.nome_conta
ORDER BY scm.competencia_saldo_contabil_mensal;
 
-- 27) Saldo contábil mensal de empresas de SC, com a conta e o colaborador responsável
SELECT
    e.razao_social_empresa,
    ct.nome_conta,
    scm.saldo_final_saldo_contabil_mensal,
    c.nome_colaborador AS responsavel_interno
FROM saldo_contabil_mensal scm
JOIN empresa e ON e.id_empresa = scm.id_empresa_saldo_contabil_mensal
JOIN conta ct ON ct.id_conta = scm.id_conta_saldo_contabil_mensal
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
WHERE e.uf_empresa = 'SC'
ORDER BY scm.saldo_final_saldo_contabil_mensal DESC;
 
 
-- 28) Movimentações bancárias não conciliadas, com conta bancária e empresa
SELECT
    mb.data_movimentacao_bancaria,
    mb.tipo_movimentacao_bancaria,
    mb.valor_movimentacao_bancaria,
    cb.banco_conta_bancaria,
    e.razao_social_empresa
FROM movimentacao_bancaria mb
JOIN conta_bancaria cb ON cb.id_conta_bancaria = mb.id_conta_bancaria_movimentacao_bancaria
JOIN empresa e ON e.id_empresa = cb.id_empresa_conta_bancaria
WHERE mb.conciliado_movimentacao_bancaria = 0
ORDER BY mb.data_movimentacao_bancaria DESC;
 
-- 29) Saldo atual das contas bancárias por empresa e colaborador responsável
SELECT
    cb.banco_conta_bancaria,
    cb.tipo_conta_bancaria,
    cb.saldo_atual_conta_bancaria,
    e.razao_social_empresa,
    c.nome_colaborador AS responsavel_interno
FROM conta_bancaria cb
JOIN empresa e ON e.id_empresa = cb.id_empresa_conta_bancaria
JOIN colaborador c ON c.id_colaborador = e.id_colaborador_resp_empresa
WHERE cb.status_conta_bancaria = 'Ativa'
ORDER BY cb.saldo_atual_conta_bancaria DESC;
 
-- 30) Movimentações bancárias vinculadas a lançamentos contábeis, com conta e empresa
SELECT
    mb.data_movimentacao_bancaria,
    mb.valor_movimentacao_bancaria,
    l.descricao_lancamento,
    cb.banco_conta_bancaria,
    e.razao_social_empresa
FROM movimentacao_bancaria mb
JOIN conta_bancaria cb ON cb.id_conta_bancaria = mb.id_conta_bancaria_movimentacao_bancaria
JOIN empresa e ON e.id_empresa = cb.id_empresa_conta_bancaria
JOIN lancamento l ON l.id_lancamento = mb.id_lancamento_movimentacao_bancaria
ORDER BY mb.data_movimentacao_bancaria DESC;
 
-- 31) Total de créditos (entradas) por banco e empresa
SELECT
    cb.banco_conta_bancaria,
    e.razao_social_empresa,
    SUM(mb.valor_movimentacao_bancaria) AS total_creditos
FROM movimentacao_bancaria mb
JOIN conta_bancaria cb ON cb.id_conta_bancaria = mb.id_conta_bancaria_movimentacao_bancaria
JOIN empresa e ON e.id_empresa = cb.id_empresa_conta_bancaria
WHERE mb.tipo_movimentacao_bancaria = 'C'
GROUP BY cb.banco_conta_bancaria, e.razao_social_empresa
ORDER BY total_creditos DESC;
 
-- 32) Contas a pagar atrasadas, com empresa e conta bancária vinculada
SELECT
    cp.fornecedor_conta_pagar,
    cp.valor_original_conta_pagar,
    cp.data_vencimento_conta_pagar,
    e.razao_social_empresa,
    cb.banco_conta_bancaria
FROM conta_pagar cp
JOIN empresa e ON e.id_empresa = cp.id_empresa_conta_pagar
LEFT JOIN conta_bancaria cb ON cb.id_conta_bancaria = cp.id_conta_bancaria_conta_pagar
WHERE cp.status_conta_pagar = 'Atrasado'
ORDER BY cp.data_vencimento_conta_pagar;
 
-- 33) Contas a pagar vinculadas a um documento fiscal, com a empresa
SELECT
    cp.fornecedor_conta_pagar,
    cp.valor_original_conta_pagar,
    df.numero_documento_fiscal,
    e.razao_social_empresa
FROM conta_pagar cp
JOIN documento_fiscal df ON df.id_documento_fiscal = cp.id_documento_fiscal_conta_pagar
JOIN empresa e ON e.id_empresa = cp.id_empresa_conta_pagar
ORDER BY cp.valor_original_conta_pagar DESC;
 
-- 34) Contas a receber pendentes, com empresa e conta bancária de recebimento
SELECT
    cr.cliente_conta_receber,
    cr.valor_original_conta_receber,
    cr.data_vencimento_conta_receber,
    e.razao_social_empresa,
    cb.banco_conta_bancaria
FROM conta_receber cr
JOIN empresa e ON e.id_empresa = cr.id_empresa_conta_receber
LEFT JOIN conta_bancaria cb ON cb.id_conta_bancaria = cr.id_conta_bancaria_conta_receber
WHERE cr.status_conta_receber = 'Pendente'
ORDER BY cr.data_vencimento_conta_receber;
 
-- 35) Contas a receber vinculadas a documento fiscal, com valor recebido menor que o original
SELECT
    cr.cliente_conta_receber,
    cr.valor_original_conta_receber,
    cr.valor_recebido_conta_receber,
    df.numero_documento_fiscal,
    e.razao_social_empresa
FROM conta_receber cr
JOIN documento_fiscal df ON df.id_documento_fiscal = cr.id_documento_fiscal_conta_receber
JOIN empresa e ON e.id_empresa = cr.id_empresa_conta_receber
WHERE cr.valor_recebido_conta_receber IS NOT NULL
  AND cr.valor_recebido_conta_receber < cr.valor_original_conta_receber
ORDER BY (cr.valor_original_conta_receber - cr.valor_recebido_conta_receber) DESC;
 
-- 36) Total pago em contas a pagar, por fornecedor, empresa e conta bancária utilizada
SELECT
    cp.fornecedor_conta_pagar,
    e.razao_social_empresa,
    cb.banco_conta_bancaria,
    SUM(cp.valor_pago_conta_pagar) AS total_pago
FROM conta_pagar cp
JOIN empresa e ON e.id_empresa = cp.id_empresa_conta_pagar
JOIN conta_bancaria cb ON cb.id_conta_bancaria = cp.id_conta_bancaria_conta_pagar
WHERE cp.status_conta_pagar = 'Pago'
GROUP BY cp.fornecedor_conta_pagar, e.razao_social_empresa, cb.banco_conta_bancaria
ORDER BY total_pago DESC;
 
-- 37) Clientes com contas a receber canceladas, com empresa e documento fiscal de origem
SELECT
    cr.cliente_conta_receber,
    cr.valor_original_conta_receber,
    df.numero_documento_fiscal,
    e.razao_social_empresa
FROM conta_receber cr
JOIN empresa e ON e.id_empresa = cr.id_empresa_conta_receber
LEFT JOIN documento_fiscal df ON df.id_documento_fiscal = cr.id_documento_fiscal_conta_receber
WHERE cr.status_conta_receber = 'Cancelado'
ORDER BY cr.valor_original_conta_receber DESC;