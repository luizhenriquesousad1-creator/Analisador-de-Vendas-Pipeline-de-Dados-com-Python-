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

