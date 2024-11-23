import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from data import init_object

class valuesDataFrame:
    def __init__(self, df):
        self.df=df

    def print_dados(self):
        #Técnicas de Manipulação de dados.Inspecao
        print(df.head())
        print(df.info())
        print(df.describe())
        #

    def print_moda(self):
        #Técnicas de Manipulação de dados.Inspecao
        print(df['categoria'].mode()[0])
        #
        return df['categoria'].mode()[0]

    def print_sum_month(self, mes, ano):
        #Técnicas de Manipulação de dados.Transformação
        df['data']=pd.to_datetime(df['data'])
        #
        #Técnicas de Manipulação de dados.Inspecao
        df_mes = df[(df['data'].dt.month == mes) & (df['data'].dt.year == ano)]
        gastos_totais = df_mes['quantidade'].sum()
        print(gastos_totais)
        #
        return gastos_totais

    def plot_history_month(self):
        #Técnicas de Manipulação de dados.Transformação
        df['data']=pd.to_datetime(df['data'])
        #
        #Técnicas de Manipulação de dados.Modelagem
        gastos_por_mes = df.groupby(pd.Grouper(key='data', freq='M'))['quantidade'].sum().astype(float)
        plt.figure(figsize=(10, 6))
        gastos_por_mes.plot(kind='line')
        plt.title('Gastos Mensais')
        plt.xlabel('Mês')
        plt.ylabel('Quantidade (R$)')
        plt.grid(True)
        plt.show()
        #
        pass

    def plot_heatmap(self):
        #Técnicas de Manipulação de dados.Transformação
        df['data']=pd.to_datetime(df['data'],format='mixed')
        
        #
        #Técnicas de Manipulação de dados.Modelagem
        gastos_por_categoria_mes = df.groupby(['categoria', pd.Grouper(key='data', freq='M')])['quantidade'].sum().astype(float).unstack()
        sns.set()
        ax = sns.heatmap(gastos_por_categoria_mes) 
        plt.xticks(rotation=-90)
        plt.show()
        #
        pass

df=init_object()
handler=valuesDataFrame(df)
#handler.plot_history_month()
handler.print_sum_month(3,2022)
#handler.plot_heatmap()