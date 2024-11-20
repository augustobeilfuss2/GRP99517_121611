import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


link ='https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
df = pd.read_csv(link)

print(df.head())