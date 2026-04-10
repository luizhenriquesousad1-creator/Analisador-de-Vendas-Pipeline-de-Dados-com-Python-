import pandas as pd


def criar_dataframe(vendas, produtos, categoria):
  """
  Cria um dataframe a partir dos dicionários de entrada
  """
  df_vendas = pd.DataFrame(vendas)
  df_produtos = pd.DataFrame(produtos)
  df_categoria = pd.DataFrame(categoria)
  return df_vendas, df_produtos, df_categoria

def criar_dataframe_geral(df_vendas, df_produtos, df_categoria):
  """Função que cria um dataframe consolidado a partir dos dados de vendas, produtos e categoria,
  realizando juntção (merge) pela coluna 'produto_id'.

  Retorna: DataFrame contendo irformações complestas de cada venda."""
  df_geral = df_vendas.merger(df_produtos, on'produto_id').merge(df_categoria, on='produto_id')
  return df_geral

def trata_nulos(df_geral):
  """
  substitui valores nulos por0.
  """
  return df_geral.fillna(0)

def adiciona_faturamento(df_geral):
  """
  Adiciona a coluna 'faturamento' com base em preco * quantidade.
  """
  df_geral = df_geral.copy()
  df_geral['faturamento'] = df_geral['preco' * df_geral['quantidade']
  return df_geral

def criar_coluna_classificacao:(df_geral):
  """
  Cria a coluna 'classificacao' com base no faturamento.
  """
  df_geral = df_geral.copy()
  df_geral['classificacao'] = df.apply(classifica, axis=')
  return df_geral
