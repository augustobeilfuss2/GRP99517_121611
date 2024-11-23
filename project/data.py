import psycopg2
import os
import sys
import pandas as pd

def conectar_banco():
    return psycopg2.connect(
    dbname='postgres',
    user='postgres',  
    password='12345', 
    host='localhost', 
    port='5432')

def init_object():
    conn = conectar_banco()
    cursor = conn.cursor()
    query = "SELECT * FROM transacoes;"
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    cursor.close()
    conn.close()
    print(df)
    return df


