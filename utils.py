import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def organiza():
  print("-" *80)

def apresenta_resultado(produto):
  return (f"Oproduto mais vendido foi {produto['nome']} que vendeu {produto['quantidade']} unidades.")

def selecionar_arquivo():
  Tk().wothdraw()
  caminho = askopenfilename(title="Selecione o arquivo CSV", filetype=[("arquivo CSV", "*.csv")])
  return caminho

def carrega_dados():
  try:
    caminho_vendas = selecionar_arquivos()
    caminho_produto = selecionar_arquivo()
    caminho_categoria = selecionar_arquivo()

    df_vendas = pd.read_csv(caminho_vendas)
    df_produto = pd.read_csv(caminho_produto)
    df_categoria = pd.read_csv(caminho_categoria)
    
    return df_vendas, df_produtos, df_categoria

  except Exception as e:
    print("Erro ao carregar arquivos. Verifique se selecionou arquivos CSV válidos.")
    print(f"Erro ao carregar arquivo: {e}")
    return None
