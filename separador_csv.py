import pandas as pd

import os



# --- CONFIGURAÇÃO ---

# Nome do seu arquivo original aqui

arquivo_original = 'TODOS_os_dados_filtrados.csv.csv'



# Nomes dos arquivos de saída

arquivo_book = 'saida_book.csv'

arquivo_info = 'saida_info.csv'



# Nome da coluna que será analisada

coluna_alvo = 'StatusCode'





# --- LÓGICA DO SCRIPT ---

def separar_csv():

    # Verifica se o arquivo original existe

    if not os.path.exists(arquivo_original):

        print(f"Erro: O arquivo '{arquivo_original}' não foi encontrado no diretório.")

        return



    try:

        # Carrega o arquivo CSV inteiro para um DataFrame do pandas

        print(f"Lendo o arquivo '{arquivo_original}'...")

        df = pd.read_csv(arquivo_original, sep=';')



        # Verifica se a coluna alvo existe no arquivo

        if coluna_alvo not in df.columns:

            print(f"Erro: A coluna '{coluna_alvo}' não foi encontrada no arquivo.")

            print(f"Colunas disponíveis: {list(df.columns)}")

            return



        # 1. Filtra o DataFrame para obter apenas as linhas onde a coluna_alvo é 'BOOK'

        print(f"Filtrando por '{coluna_alvo}' igual a 'BOOK'...")

        df_book = df[df[coluna_alvo] == 'BOOK']



        # 2. Filtra o DataFrame para obter apenas as linhas onde a coluna_alvo é 'INFO'

        print(f"Filtrando por '{coluna_alvo}' igual a 'INFO'...")

        df_info = df[df[coluna_alvo] == 'INFO']



        # Salva o DataFrame filtrado 'BOOK' em um novo arquivo CSV

        # O argumento index=False evita que o pandas adicione uma nova coluna de índice ao CSV

        df_book.to_csv(arquivo_book, index=False, encoding='utf-8')

        print(f"✔ Sucesso! {len(df_book)} linhas salvas em '{arquivo_book}'")



        # Salva o DataFrame filtrado 'INFO' em um novo arquivo CSV

        df_info.to_csv(arquivo_info, index=False, encoding='utf-8')

        print(f"✔ Sucesso! {len(df_info)} linhas salvas em '{arquivo_info}'")



    except Exception as e:

        print(f"Ocorreu um erro inesperado: {e}")



# Executa a função principal

if __name__ == '__main__':

    separar_csv()
