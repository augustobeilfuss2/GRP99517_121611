import psycopg2
import csv
from data import conectar_banco


def inserir_csv_no_banco(caminho_csv):
    conn = conectar_banco()
    cursor = conn.cursor()


    with open(caminho_csv, mode='r', encoding='utf-8') as file:
    
        csv_reader = csv.reader(file)
        next(csv_reader)
        next(csv_reader)  
        print(csv_reader)
        
        insert_query = """
        INSERT INTO transacoes (Data, Conta, Categoria, Nota, INR, TipoTransacao, Quantidade, Moeda, ContaAssociada  )
        VALUES (%s, %s, %s, %s, %s , %s, %s, %s, %s);
        """
        
        for row in csv_reader:
            print(row[0], row[1], row[2], row[3], row[4],row[5],row[6],row[7],row[8],row[9],row[10])
           
            cursor.execute(insert_query, (row[0], row[1], row[2], row[4], row[5], row[6], row[8],row[9],row[10]))
            
    conn.commit()

    cursor.close()
    conn.close()


caminho_csv = 'expense_data_1.csv'
inserir_csv_no_banco(caminho_csv)
