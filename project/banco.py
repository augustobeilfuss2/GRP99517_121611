import psycopg2
from psycopg2 import sql





conn = conectar_banco()
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS transacoes (
    ID SERIAL PRIMARY KEY,
    Data DATE NOT NULL,
    Conta VARCHAR(255) NOT NULL,
    Categoria VARCHAR(255) NOT NULL,
    Nota TEXT,
    INR DECIMAL(15, 2),
    TipoTransacao VARCHAR(10) CHECK (TipoTransacao IN ('Income', 'Expense')) NOT NULL,
    Quantidade DECIMAL(15, 2),
    Moeda VARCHAR(3) NOT NULL,
    ContaAssociada VARCHAR(255)
);
"""

cursor.execute(create_table_query)
conn.commit()
cursor.close()
conn.close()

print("Banco de dados e tabela criados com sucesso!")
