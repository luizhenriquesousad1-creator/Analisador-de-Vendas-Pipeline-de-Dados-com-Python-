# 📊 Analisador de Vendas — Pipeline de Dados com Python

Este projeto consiste em um sistema de análise de vendas desenvolvido em Python utilizando Pandas, com arquitetura modular e foco em boas práticas de engenharia de dados.

A aplicação simula um fluxo real de processamento de dados, desde a ingestão até a geração de insights, com interface interativa via terminal (CLI).

---

## 🎯 Objetivo

O objetivo deste projeto é demonstrar habilidades em:

* Manipulação e análise de dados com Pandas
* Integração de múltiplas fontes de dados (merge/join)
* Construção de pipelines de dados
* Aplicação de regras de negócio
* Estruturação de código em módulos
* Desenvolvimento de aplicações interativas (CLI)

---

## 🧱 Estrutura do Projeto

```bash
projeto/
│
├── main.py            # Ponto de entrada (interface CLI)
├── processamento.py   # Preparação e transformação dos dados
├── analise.py         # Cálculos e métricas
├── utils.py           # Funções auxiliares
└── dados/             # (futuro) arquivos CSV
```

---

## 📦 Fonte de Dados

O sistema simula três conjuntos de dados:

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

## 🔄 Pipeline de Dados

O processamento segue as seguintes etapas:

1. Criação dos DataFrames
2. Junção dos dados com `merge`
3. Tratamento de valores nulos
4. Criação da coluna de faturamento
5. Classificação de desempenho dos produtos
6. Análises agregadas com `groupby`

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
* Modularização de código
* CLI interativa

### 📊 Pandas

* DataFrame
* `merge` / `join`
* `groupby`
* operações vetorizadas
* `apply()`

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse a pasta do projeto:

```bash
cd projeto
```

3. Execute:

```bash
python main.py
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
* 💾 Exportação de resultados (CSV / Excel)
* ⚙️ Automação do pipeline
* 📊 Visualizações com Matplotlib / Seaborn
* 🧪 Testes automatizados

---

## 📌 Status do Projeto

🟢 Em evolução
🚀 Projeto desenvolvido como parte da evolução para nível profissional em Python (Data + Engenharia)

---

## 👨‍💻 Autor

Luiz Henrique
