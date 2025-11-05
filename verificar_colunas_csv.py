import pandas as pd

import sys



if len(sys.argv) > 1:

    nome_do_arquivo_para_teste = sys.argv[1]

else:

    print("\nERRO: Você precisa especificar um nome de arquivo para verificar.")

    print("Uso correto: python verificar_colunas.py nome_do_arquivo.csv")

    sys.exit() # Encerra o script



try:

    # Tentamos ler o arquivo CSV, usando ponto e vírgula como separador

    # nrows=1 faz ler só o cabeçalho, é mais rápido

    df_teste = pd.read_csv(nome_do_arquivo_para_teste, sep=';', nrows=1)



    print(f"\n--- Colunas encontradas no arquivo: '{nome_do_arquivo_para_teste}' ---")

   

    # Limpa os nomes das colunas de espaços e aspas para facilitar

    colunas_limpas = df_teste.columns.str.strip().str.strip("'").tolist()

   

    print(colunas_limpas) # Imprime a lista de colunas limpas

    print("--------------------------------------------------")



except FileNotFoundError:

    print(f"ERRO: Não encontrei o arquivo '{nome_do_arquivo_para_teste}'.")

    print("Verifique se o nome do arquivo está correto.")

except Exception as e:

    print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")
