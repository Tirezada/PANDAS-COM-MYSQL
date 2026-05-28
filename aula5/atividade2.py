from sqlalchemy import create_engine
import pandas as pd 

#CONEXÃO COM O BANCO:
host = 'localhost'
user = 'root'
password = ''
db = 'aula6'

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{db}'
)

#CRIANDO DATA FRAMES:
try:
    
    df_clientes = pd.read_sql('tb_clientes', engine)
    df_itens = pd.read_sql('tb_itens', engine)
    df_pedidos = pd.read_sql('tb_pedidos', engine)
    df_produtos = pd.read_sql('tb_produtos', engine)

except Exception as e:
    print(e)

#RELACIONANDO AS TABELAS:
try:
    df_merge1 = pd.merge(df_pedidos, df_clientes, on="codigo_cliente")
    df_merge2 = pd.merge(df_merge1, df_itens, on="codigo_pedido")
    df_merge3 = pd.merge(df_merge2, df_produtos, on="codigo_produto")

    filtro = (df_merge3['cidade'] == 'Sao Paulo')
    df_SP = df_merge3[filtro]
    
except Exception as e:
    print(e)

#RELATÓRIO:
    

print(f'''
-------------------------------------- Relatório --------------------------------------

      
{df_SP[['nome', 'sobrenome', 'cidade', 'codigo_pedido', 'data_pedido', 'produto', 'valor' ]]}


---------------------------------------------------------------------------------------''')



#print(df_carlos[['nome', 'sobrenome', 'cidade', 'codigo_pedido', 'data_pedido', 'produto', 'valor' ]])
#print(gasto_carlos)

