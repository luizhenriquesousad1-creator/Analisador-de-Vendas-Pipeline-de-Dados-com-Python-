def produto_mais_vendido(df_geral):
  """
  Identifica o produto com maior quantiade de venda.
  Parâmetro:
    df_geral: dataframe contendo os daods de vendas.
  Retorna:
    series: linhas correspondentes ao produto masi vendiso.
  """
  idx = df_geral['quantidade'].idxmax()
  return df_geral.loc[idx]

def produto_mais_lucrativo(df_geral):
  """
  Calcula o faturmaneto total por categoria de produto.

  Parâmetro: df_geral: dataframe contendo od dados de vendas.
  Retorna: tupla com o nome do produto masi lucrativo e seu faturamento total.
  """
  total = df_geral.groupby('nome')['faturamento'].sum()
  return total.idxmax(), total.max()

def calc_faturamento_por_categoria(df_geral):
  """
  Calcula o faturamento total por categoria de produto.
  Parâmetro: df_geral: dataframe contendo os dados de vendas.
  Retorna: Série contendo os dados de faturamento por produto
  """
  return df_geral['faturamento].groupby(df_geral['categoria']).sum()

def mostra_faturamento_por_categoria(faturamento):
  """
  Identifica a categoria com maior faturamento.
  Parâmetro: df_geral: dataframe contendo os dados de vendas.
  Retorna: Tupla com nome da categoria com maior faturamento e o valor correspondente.
  """
  produto = faturamentpo.idxmax()
  valor = faturamento[produto]
  return produto, valor
