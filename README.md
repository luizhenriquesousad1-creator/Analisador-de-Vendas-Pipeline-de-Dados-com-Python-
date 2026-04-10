📊 Analisador de Vendas (Pipeline de Dados com Python)

Este projeto consiste em um sistema de análise de vendas desenvolvido em Python utilizando a biblioteca Pandas.
A aplicação simula um fluxo real de dados, realizando integração de múltiplas fontes, tratamento, análise e geração de insights através de uma interface interativa no terminal.

---

## 🎯 Objetivo

O objetivo do projeto é praticar e demonstrar:

* Manipulação e análise de dados com Pandas
* Integração de múltiplos datasets (merge/join)
* Construção de pipelines de dados
* Aplicação de regras de negócio
* Desenvolvimento de aplicações interativas (CLI)
* Estruturação de código com boas práticas

---

## 📦 Estrutura dos Dados

O sistema simula três fontes de dados:

### 🧾 Vendas

* id_vendas
* produto_id
* quantidade

### 🏷️ Produtos

* produto_id
* nome
* preco

### 🗂️ Categorias

* produto_id
* categoria

---

## 🔗 Processamento

O pipeline realiza:

1. Criação dos DataFrames
2. Junção dos dados (`merge`)
3. Tratamento de valores nulos
4. Cálculo de métricas (faturamento)
5. Classificação de desempenho dos produtos
6. Análise agregada com `groupby`

---

## 📊 Funcionalidades

O sistema permite:

* 📦 Identificar o produto mais vendido
* 💰 Identificar o produto mais lucrativo
* 📈 Analisar faturamento por categoria
* 🧠 Classificar produtos por desempenho
* 🖥️ Interagir via menu no terminal

---

## 🧠 Tecnologias e Conceitos

### 🐍 Python

* Funções
* Estrutura de controle
* CLI interativa

### 📊 Pandas

* DataFrame
* `merge` / `join`
* `groupby`
* operações vetorizadas
* `apply()`

---

## ▶️ Como executar

```bash
python nome_do_arquivo.py
```

---

## 📌 Exemplo de saída

```
produto_id | nome    | quantidade | preco | categoria | faturamento | Classificação
0          | batata  | 2          | 10    | vegetais  | 20          | Baixo
1          | cenoura | 4          | 200   | legumes   | 800         | Medio
2          | tomate  | 6          | 3000  | fruta     | 18000       | Alto
```

---

## 📈 Próximos passos

* 📂 Leitura automática de arquivos CSV
* 💾 Exportação de relatórios (CSV/Excel)
* 🧱 Estrutura modular do projeto
* ⚙️ Automação do pipeline

---

## 📌 Status

🟢 Em evolução
🚀 Projeto em desenvolvimento contínuo com foco em Data + Engenharia

---

## 👨‍💻 Autor

Luiz Henrique
