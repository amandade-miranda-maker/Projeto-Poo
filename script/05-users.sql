use INOVE_CONTABILIDADE;

# Criação de usuários
CREATE USER 'douglas'@'%' IDENTIFIED by 'douglas123';
CREATE USER 'amanda'@'%' IDENTIFIED by 'amanda123';
CREATE USER 'emanuel'@'%' IDENTIFIED by 'emanuel123';
CREATE USER 'augusto'@'%' IDENTIFIED by 'augusto123';

#Dando privilégios
GRANT all ON INOVE_CONTABILIDADE.* TO 'douglas'@'%';
GRANT SELECT,DELETE,UPDATE,INSERT ON INOVE_CONTABILIDADE.* TO 'amanda'@'%';
GRANT SELECT,DELETE,UPDATE,INSERT ON INOVE_CONTABILIDADE.* TO 'emanuel'@'%';
GRANT SELECT ON INOVE_CONTABILIDADE.* TO 'augusto'@'%';

#Recaregando sistema
FLUSH PRIVILEGES;

SELECT * FROM mysql.user;

#Mostrando os usuários e seus privilégios
SHOW GRANTS FOR 'douglas'@'%';
SHOW GRANTS FOR 'amanda'@'%';
SHOW GRANTS FOR 'emanuel'@'%';
SHOW GRANTS FOR 'augusto'@'%';


#Criação de cargos

CREATE ROLE 'DBA'; -- DBA é o Database Administrador

CREATE ROLE 'Editor';

CREATE ROLE 'Leitor';

CREATE ROLE 'Desenvolvedor';


#Dando os privelégios para os cargos

GRANT all ON INOVE_CONTABILIDADE.* TO 'DBA';

GRANT SELECT, INSERT, UPDATE ON INOVE_CONTABILIDADE.* TO 'Editor';

GRANT SELECT ON INOVE_CONTABILIDADE.* TO 'Leitor';

GRANT SELECT ON INOVE_CONTABILIDADE.* TO 'Desenvolvedor';

#Mostrando os privilégios

SHOW GRANTS FOR 'DBA';

SHOW GRANTS FOR 'Editor';

SHOW GRANTS FOR 'Leitor';

SHOW GRANTS FOR 'Desenvolvedor';