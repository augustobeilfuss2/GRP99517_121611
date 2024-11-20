import psycopg2
import csv

# Função para conectar ao banco de dados
def conectar_banco():
    return psycopg2.connect(
    dbname='postgres',
    user='postgres',  # Substitua com seu nome de usuário
    password='12345',  # Substitua com sua senha
    host='localhost',  # Ou o IP/hostname do servidor
    port='5432'  # Porta padrão do PostgreSQL
)

# Função para inserir dados do CSV na tabela do banco de dados
def inserir_csv_no_banco(caminho_csv):
    conn = conectar_banco()
    cursor = conn.cursor()

    # Abrir o arquivo CSV
    with open(caminho_csv, mode='r', encoding='utf-8') as file:
        # Criar um leitor CSV
        csv_reader = csv.reader(file)
        next(csv_reader)  # Pular o cabeçalho, caso exista
        print(csv_reader)
        # Preparar o comando SQL para inserção
        insert_query = """
        INSERT INTO Transacoes (Data, Conta, Categoria, Subcategoria, Nota, INR, TipoTransacao, Quantidade, Moeda, ContaAssociada)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        # Iterar sobre as linhas do CSV e inserir os dados na tabela
        for row in csv_reader:
            print(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10])
           
            cursor.execute(insert_query, (row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10]))

    # Commit para salvar as alterações no banco
    conn.commit()

    # Fechar a conexão
    cursor.close()
    conn.close()

    print(f'{len(list(csv_reader))} linhas inseridas com sucesso no banco de dados.')

# Chamar a função para gravar os dados do CSV no banco
caminho_csv = 'expense_data_1.csv'
inserir_csv_no_banco(caminho_csv)
