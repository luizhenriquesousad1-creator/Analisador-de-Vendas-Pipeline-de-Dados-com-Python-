# 📊 Analisador de Vendas — Pipeline de Dados com Python

Este projeto implementa um pipeline completo de análise de vendas utilizando Python e Pandas, simulando um fluxo real de dados com múltiplas fontes, processamento, análise e interação via terminal.

---

## 🎯 Objetivo

O objetivo do projeto é desenvolver habilidades práticas em:

* Manipulação e análise de dados com Pandas
* Integração de múltiplos datasets (`merge`)
* Construção de pipelines de dados
* Aplicação de regras de negócio
* Estruturação de código em módulos
* Interação com usuário via CLI

---

## 🧱 Arquitetura do Projeto

O projeto foi estruturado em módulos para melhor organização e escalabilidade:

```bash
src/
│
├── main.py           # Controle da aplicação (CLI)
├── processamento.py  # Transformação e preparação dos dados
├── analise.py        # Funções de análise
└── utils.py          # Funções auxiliares (I/O e interface)
```

---

## 📂 Entrada de Dados

O sistema trabalha com três arquivos CSV:

* 📦 **vendas.csv** → quantidade vendida por produto
* 🏷️ **produtos.csv** → nome e preço
* 🗂️ **categorias.csv** → categoria do produto

Os arquivos são selecionados dinamicamente pelo usuário via interface gráfica.

---

## 🔗 Pipeline de Dados

O fluxo de processamento segue as etapas:

1. Leitura dos arquivos CSV
2. Junção dos dados (`merge`)
3. Tratamento de valores nulos
4. Criação de métricas (faturamento)
5. Classificação de desempenho
6. Análise agregada

---

## 📊 Funcionalidades

O sistema permite:

* 📦 Identificar o produto mais vendido
* 💰 Identificar o produto mais lucrativo
* 📈 Analisar faturamento por categoria
* 🧠 Classificar produtos por desempenho
* 🖥️ Interagir via menu no terminal

---

## 🧠 Tecnologias Utilizadas

* Python 3
* Pandas
* Tkinter (seleção de arquivos)

---

## ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/luizhenriquesousad1-creator/Analisador-de-Vendas-Pipeline-de-Dados-com-Python-
```

2. Acesse a pasta:

```bash
cd Analisador-de-Vendas-Pipeline-de-Dados-com-Python-
```

3. Execute:

```bash
python src/main.py
```

4. Selecione os arquivos CSV quando solicitado

---

## 📌 Exemplo de Saída

```text
produto_id | nome    | quantidade | preco | categoria | faturamento | Classificação
0          | batata  | 2          | 10    | vegetais  | 20          | Baixo
1          | cenoura | 4          | 200   | legumes   | 800         | Médio
2          | tomate  | 6          | 3000  | fruta     | 18000       | Alto
```

---

## 📈 Próximas Melhorias

* 💾 Exportação automática de relatórios (CSV/Excel)
* ⚙️ Execução sem interface gráfica (CLI puro)
* 📊 Visualizações com gráficos
* 🔍 Validação de dados de entrada

---

## 📌 Status

🟢 Projeto funcional
🚀 Em evolução contínua

---

## 👨‍💻 Autor

Luiz Henrique
