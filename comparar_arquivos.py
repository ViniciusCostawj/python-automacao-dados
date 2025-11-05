import pandas as pd

import os



# --- CONFIGURAÇÃO ---

# Nomes dos arquivos, que devem estar na mesma pasta do script

arquivo1_path = 'saida_book.csv'

arquivo2_path = 'principal.csv'



# Defina o separador para CADA arquivo individualmente

separador_arquivo1 = ','  

separador_arquivo2 = ';'  



# Nome da coluna que será usada como chave para a comparação

coluna_chave = 'nuop'



# Pasta e nome do arquivo de saída

pasta_saida = '.'

arquivo_saida = 'divergencias.csv'

# --------------------





def comparar_arquivos():

    """

    Função principal para ler, comparar e salvar as divergências entre dois arquivos CSV.

    """

    print("Iniciando a comparação de arquivos...")



    # --- Passo 1: Preparar pasta de saída ---

    try:

        os.makedirs(pasta_saida, exist_ok=True)

        print(f"Pasta de saída '{pasta_saida}' pronta.")

    except OSError as e:

        print(f"ERRO: Não foi possível criar a pasta de saída. Erro: {e}")

        return



    # --- Passo 2: Ler os arquivos CSV com seus separadores específicos ---

    try:

        print(f"Lendo o Arquivo 1: {arquivo1_path} (usando separador '{separador_arquivo1}')")

        df1 = pd.read_csv(arquivo1_path, sep=separador_arquivo1, dtype=str).fillna('')

       

        print(f"Lendo o Arquivo 2: {arquivo2_path} (usando separador '{separador_arquivo2}')")

        df2 = pd.read_csv(arquivo2_path, sep=separador_arquivo2, dtype=str).fillna('')



    except FileNotFoundError as e:

        print(f"ERRO: Arquivo não encontrado. Verifique o nome do arquivo na configuração. Detalhes: {e}")

        return

    except Exception as e:

        print(f"ERRO ao ler os arquivos CSV: {e}")

        return



    # --- Validação das Colunas ---

    if coluna_chave not in df1.columns:

        print(f"\n--- ERRO ---")

        print(f"A coluna chave '{coluna_chave}' não foi encontrada no arquivo: '{arquivo1_path}'")

        print("As colunas que encontrei neste arquivo são:")

        print(list(df1.columns))

        print("------------\n")

        return



    if coluna_chave not in df2.columns:

        print(f"\n--- ERRO ---")

        print(f"A coluna chave '{coluna_chave}' não foi encontrada no arquivo: '{arquivo2_path}'")

        print("As colunas que encontrei neste arquivo são:")

        print(list(df2.columns))

        print("------------\n")

        return

       

    # --- Passo 3: Encontrar as divergências ---

    print(f"Comparando os arquivos pela coluna '{coluna_chave}'...")



    df_merged = df1.merge(df2, on=coluna_chave, how='outer', indicator=True)

    df_divergentes = df_merged[df_merged['_merge'] != 'both']



    if df_divergentes.empty:

        print("\nÓtima notícia! Nenhum valor divergente encontrado na coluna chave.")

        return



    # --- Passo 4: Preparar o arquivo de saída ---

    nome_arquivo1 = os.path.basename(arquivo1_path)

    nome_arquivo2 = os.path.basename(arquivo2_path)

   

    df_divergentes['_merge'] = df_divergentes['_merge'].map({

        'left_only': f'Apenas no {nome_arquivo1}',

        'right_only': f'Apenas no {nome_arquivo2}'

    })

    df_divergentes.rename(columns={'_merge': 'OrigemDivergencia'}, inplace=True)



    # --- Passo 5: Salvar o resultado ---

    # Vamos salvar o arquivo final com ponto e vírgula para manter um padrão

    caminho_final_saida = os.path.join(pasta_saida, arquivo_saida)

    try:

        df_divergentes.to_csv(caminho_final_saida, index=False, sep=';')

        print("\n--- SUCESSO! ---")

        print(f"Foram encontradas {len(df_divergentes)} linhas divergentes.")

        print(f"O resultado foi salvo em: {caminho_final_saida}")

    except Exception as e:

        print(f"ERRO ao salvar o arquivo de saída: {e}")





# Executar a função

if __name__ == "__main__":

    comparar_arquivos()
