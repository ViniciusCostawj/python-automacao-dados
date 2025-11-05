# Scripts de Automação e Análise de Dados com Pandas

Este repositório é uma coleção de scripts utilitários em Python, usando a biblioteca **Pandas**, para resolver problemas comuns de manipulação, reconciliação e análise de dados em arquivos CSV.

---

### 1. Calculadora de Resumo Financeiro (`calcular_resumo_financeiro.py`)

Este script lê um arquivo CSV de movimentações financeiras, limpa os dados e calcula um resumo final.

**O que ele faz:**
* Lê um arquivo CSV (`divergencias.csv`).
* Unifica colunas de dados que podem vir duplicadas (ex: `Amount_x`, `Amount_y`).
* Limpa e padroniza os indicadores de Crédito/Débito (aceitando formatos como 'CRDT'/'C' e 'DBIT'/'D').
* Converte valores monetários (tratando vírgulas como separador decimal) para numérico.
* Calcula e exibe o **Total de Créditos**, **Total de Débitos** e o **Saldo Final**.

### 2. Comparador e Reconciliador de CSVs (`comparar_arquivos.py`)

Este script compara dois arquivos CSV com base em uma coluna-chave e gera um terceiro arquivo contendo **apenas as divergências**.

**O que ele faz:**
* Lê dois arquivos CSV distintos (ex: `saida_book.csv` e `principal.csv`), cada um podendo ter seu próprio separador (ex: `,` e `;`).
* Compara os arquivos usando `pandas.merge` em uma coluna-chave (ex: `nuop`).
* Identifica quais linhas existem **apenas no arquivo 1** e quais existem **apenas no arquivo 2**.
* Salva um novo CSV (`divergencias.csv`) contendo *apenas* as linhas divergentes, com uma coluna extra indicando a origem da divergência.

### 3. Divisor de CSV por Categoria (`separar_csv.py`)

Este script lê um arquivo CSV grande e o divide em múltiplos arquivos menores com base no valor de uma coluna específica.

**O que ele faz:**
* Lê um arquivo principal (ex: `TODOS_os_dados_filtrados.csv.csv`).
* Filtra as linhas com base em um valor (ex: `StatusCode == 'BOOK'`).
* Salva um novo CSV (`saida_book.csv`) apenas com esses dados.
* Filtra as linhas com base em outro valor (ex: `StatusCode == 'INFO'`).
* Salva um segundo CSV (`saida_info.csv`) com o restante dos dados.

### 4. Inspetor de Colunas CSV (`verificar_colunas.py`)

Um script utilitário de linha de comando para inspecionar rapidamente as colunas de um arquivo CSV, sem ter que abri-lo.

**O que ele faz:**
* Recebe um nome de arquivo como argumento no terminal.
* Lê de forma eficiente **apenas a primeira linha** (cabeçalho) do arquivo.
* Limpa os nomes das colunas (removendo espaços ou aspas).
* Imprime uma lista limpa dos nomes das colunas encontrados.
