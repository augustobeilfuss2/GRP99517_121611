
import psycopg2
from psycopg2 import sql

# Conectar-se ao servidor PostgreSQL (sem especificar um banco de dados)
conn = psycopg2.connect(
    dbname='postgres',  # Banco de dados padrão no PostgreSQL
    user='postgres',  # Substitua com seu nome de usuário
    password='12345',  # Substitua com sua senha
    host='localhost',  # Ou o IP/hostname do servidor
    port='5432'  # Porta padrão do PostgreSQL
)

# Criar um cursor para executar comandos SQL
cur = conn.cursor()



# Fechar a conexão com o banco de dados padrão e reconectar-se ao novo banco de dados
cur.close()
conn.close()

# Conectar-se ao novo banco de dados FinancasDB
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',  # Substitua com seu nome de usuário
    password='12345',  # Substitua com sua senha
    host='localhost',  # Ou o IP/hostname do servidor
    port='5432'  # Porta padrão do PostgreSQL
)

# Criar um novo cursor para o banco de dados FinancasDB
cur = conn.cursor()

# SQL para criar a tabela de transações
create_table_query = """
CREATE TABLE IF NOT EXISTS Transacoes (
    ID SERIAL PRIMARY KEY,
    Data DATE NOT NULL,
    Conta VARCHAR(255) NOT NULL,
    Categoria VARCHAR(255) NOT NULL,
    Subcategoria VARCHAR(255),
    Nota TEXT,
    INR DECIMAL(15, 2),
    TipoTransacao VARCHAR(10) CHECK (TipoTransacao IN ('Income', 'Expense')) NOT NULL,
    Quantidade DECIMAL(15, 2),
    Moeda VARCHAR(3) NOT NULL,
    ContaAssociada VARCHAR(255)
);
"""

# Executar o comando SQL para criar a tabela
cur.execute(create_table_query)

# Confirmar as alterações no banco de dados
conn.commit()

# Fechar a conexão e o cursor
cur.close()
conn.close()

print("Banco de dados e tabela criados com sucesso!")
