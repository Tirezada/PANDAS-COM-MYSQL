from sqlalchemy import create_engine
import pandas as pd 

host = 'localhost'
user = 'root'
password = ''
db = 'bd_biblioteca'

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{db}'
)

try:
    df_user = pd.read_sql('tb_usuarios', engine)
    df_livro = pd.read_sql('tb_livros', engine)
    df_aluguel = pd.read_sql('tb_alugados', engine)
    df_item = pd.read_sql('tb_itens_alugados', engine)

    #print(f'''
#{df_user.head()}
#''')
    
except Exception as e:
    print(f'Falha de conexão: {e}')


#JUNÇÃO DOS DF
try:
    df_merge1 = pd.merge(df_livro, df_item, on='id_livro')
    df_merge2 = pd.merge(df_merge1, df_aluguel, on='id_aluguel')
    df_merge3 = pd.merge(df_merge2, df_user, on='id_usuario')
    #print(df_merge3)

    filtro = (
        (df_merge3['data_devolucao'] >= '2024-11-01') & (df_merge3['data_devolucao'] <= '2024-11-30')
    )

    df_novembro = df_merge3[filtro]

    print(
        df_novembro[[
            'id_usuario', 'nome', 'id_livro', 'titulo', 'id_aluguel', 'data_aluguel', 'data_devolucao', 'valor'
        ]]  
    )

except Exception as e:
    print(f'Erro no tratamento dos dados: {e}')