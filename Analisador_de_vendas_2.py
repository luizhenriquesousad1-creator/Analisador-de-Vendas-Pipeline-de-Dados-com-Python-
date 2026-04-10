import pandas as pd


vendas = {'id_vendas':[1,2,3], 'produto_id':[0,1,2], 'quantidade':[2,4,6]}
produtos = {'produto_id':[0,1,2], 'nome':['batata','cenoura','tomate'], 'preco':[10,200,3000]}
categoria = {'produto_id':[0,1,2], 'categoria':['vegetais','legumes','fruta']}


def organiza():
    print("-"*80)

def cria_dataframe(vendas, produtos, categoria):
    df_vendas = pd.DataFrame(vendas)
    df_produtos = pd.DataFrame(produtos)
    df_categoria = pd.DataFrame(categoria)
    return df_vendas, df_produtos, df_categoria

def criar_dataframe_geral(df_vendas, df_produtos, df_categoria):
    parcial = pd.merge(df_vendas, df_produtos, on='produto_id', how='inner')
    df_geral = pd.merge(parcial, df_categoria, on='produto_id', how='inner')
    return df_geral

def trata_nulos(df_geral):
    return df_geral.fillna(0)

def calc_faturamento(df_geral):
    return df_geral['preco'] * df_geral['quantidade']

def produto_mais_vendido(df_geral):
    idx = df_geral['quantidade'].idxmax()
    return df_geral.loc[idx]

def apresenta_resultado(produto):
    return (f"O produto mais vendido foi o {produto['nome']} que vendeu {produto['quantidade']}")

def produto_mais_lucrativo(df_geral):
    total = df_geral.groupby('nome')['faturamento'].sum()
    return total.idxmax(), total.max()

    """total_por_produto = calc_faturamento(df_geral).groupby(df_geral['nome']).sum()
    nome_produto = total_por_produto.idxmax()
    valor = total_por_produto.max()
    return nome_produto, valor"""

def calc_faturamento_por_categoria(df_geral):
    total_por_categoria = df_geral['faturamento'].groupby(df_geral['categoria']).sum()
    return total_por_categoria

def mostra_faturamento_por_categoria(faturamento_total_por_categoria):
    produto = faturamento_total_por_categoria.idxmax()
    valor = faturamento_total_por_categoria[produto]
    return produto, valor

def criar_coluna_classificacao(df_geral):
    df_geral = df_geral.copy()
    df_geral['Classificação'] = df_geral.apply(classifica, axis=1)
    return df_geral

def classifica(linha):
    if linha['faturamento'] > 1000:
        return 'Alto'
    elif linha['faturamento'] > 500:
        return 'Medio'
    else:
        return 'Baixo'

def main():
    df_vendas, df_produtos, df_categoria = cria_dataframe(vendas, produtos, categoria)
    df_geral = criar_dataframe_geral(df_vendas,
                                     df_produtos,
                                     df_categoria)
    df_geral= trata_nulos(df_geral)
    df_geral['faturamento'] = calc_faturamento(df_geral)
    produto = produto_mais_vendido(df_geral)
    faturamento_total_por_categoria = calc_faturamento_por_categoria(df_geral)

    df_geral = criar_coluna_classificacao(df_geral)

    organiza()
    print(df_geral)
    organiza()

    while True:


        print("Produto mais vendido    - [0]")
        print("Produto mais lucrativo  - [1]")
        print("Faturamento por produto - [2]")

        print("finalizar programa - [9]")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except:
            print("Opção invalida, por favor digite um numero: ")
            continue

        if opcao == 0:
            print(apresenta_resultado(produto))

        elif opcao == 1:
            nome_produto, valor = produto_mais_lucrativo(df_geral)
            print(f"produto mais lucrativo foi {nome_produto} e rendeu {valor} reais")

        elif opcao == 2:
            produto, faturamento = mostra_faturamento_por_categoria(faturamento_total_por_categoria)
            print(f"A categoria mais vendida foi {produto} que faturou {faturamento} reais")

        elif opcao == 9:
            break

if __name__ == "__main__":
    main()
