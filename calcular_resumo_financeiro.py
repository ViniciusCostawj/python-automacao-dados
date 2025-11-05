import pandas as pd

import numpy as np



# --- CONFIGURAÇÃO ---

arquivo_para_calcular = 'divergencias.csv'

separador_csv = ';'

# --------------------





def calcular_resumo_financeiro():

    try:

        print(f"Lendo o arquivo: {arquivo_para_calcular}...")

        df = pd.read_csv(arquivo_para_calcular, sep=separador_csv, dtype=str)

       

        print("Unificando colunas '_x' e '_y'...")



        df['Amount'] = df['Amount_y'].fillna(df['Amount_x'])

        df['CreditDebitIndicator_unificado'] = df['CreditDebitIndicator_y'].fillna(df['CreditDebitIndicator_x'])

        df['CreditDebitIndicator'] = df['CreditDebitIndicator_unificado'].str.strip()

       

        coluna_valor = 'Amount'

        coluna_indicador = 'CreditDebitIndicator'



        print("Calculando o resumo financeiro...")

       

        # Converte a coluna de valor para número, tratando vírgulas como separador decimal

        df[coluna_valor] = pd.to_numeric(df[coluna_valor].str.replace(',', '.'), errors='coerce').fillna(0)



        # ================================================================= #

        # AQUI ESTÁ A CORREÇÃO FINAL: Usamos .isin() para aceitar ambos os formatos #

        # ================================================================= #

        creditos = df[df[coluna_indicador].isin(['CRDT', 'C'])]

        debitos = df[df[coluna_indicador].isin(['DBIT', 'D'])]



        total_credito = creditos[coluna_valor].sum()

        total_debito = debitos[coluna_valor].sum()

        saldo_final = total_credito +c total_debito

       

        print("\n-------------------------------------------")

        print("      Resumo Financeiro do Arquivo")

        print("-------------------------------------------")

        print(f"Total de Créditos (CRDT/C): {total_credito:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

        print(f"Total de Débitos (DBIT/D):  {total_debito:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

        print("-------------------------------------------")

        print(f"Saldo Final (Créditos - Débitos): {saldo_final:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))

        print("-------------------------------------------")



    except FileNotFoundError:

        print(f"ERRO: Arquivo não encontrado em '{arquivo_para_calcular}'. Verifique o nome na configuração.")

    except KeyError as e:

        print(f"ERRO: Não encontrei uma das colunas necessárias ({e}). Verifique o arquivo.")

    except Exception as e:

        print(f"Ocorreu um erro inesperado: {e}")



if __name__ == "__main__":

    calcular_resumo_financeiro()
