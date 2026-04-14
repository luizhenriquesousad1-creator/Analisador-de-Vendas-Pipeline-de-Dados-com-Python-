import pandas as pd

from processamento import (criar_dataframe, criar_dataframe_geral,
                           trata_nulos, adiciona_faturamento,
                           criar_coluna_classificacao)

from analise import (produto_mais_vendido, produto_mais_lucrativo,
                     calc_faturamento_por_categoria, mostra_faturamento_por_categoria)

from utils import (organiza, apresenta_resultado)


def main():
    vendas = {'id_vendas':[1,2,3], 'produto_id':[0,1,2],'quantidade':[2,4,6,]}
    produtos = {'produto_id': [0, 1, 2], 'nome': ['batata', 'cenoura', 'tomate'],
                'preco': [10, 200, 3000]}
    categoria = {'produto_id': [0, 1, 2], 'categoria': ['vegetais', 'legumes', 'fruta']}

    df_vendas, df_produtos, df_categoria = criar_dataframe(vendas, produtos, categoria)

    df_geral = criar_dataframe_geral(df_vendas, df_produtos, df_categoria)
    df_geral = trata_nulos(df_geral)
    df_geral = adiciona_faturamento(df_geral)
    df_geral = criar_coluna_classificacao(df_geral)
    faturamento = calc_faturamento_por_categoria(df_geral)
    produto = produto_mais_vendido(df_geral)

    organiza()
    print(df_geral)
    organiza()
    while True:
        print("Produto mais vendido    - [0]")
        print("Produto mais lucrativo  - [1]")
        print("Faturamento por produto - [2]")
        print("finalizar programa      - [9]")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except:
            print("Opção inválida, tente novamente.")

        if opcao == 0:
            print(apresenta_resultado(produto))

        elif opcao == 1:
            nome, valor = produto_mais_lucrativo(df_geral)
            print(f"{nome} gerou {valor} reais")

        elif opcao == 2:
            cat, valor = mostra_faturamento_por_categoria(faturamento)
            print(f"{cat} faturou {valor} reais")

        elif opcao == 9:
            break

if __name__ == "__main__":
    main()
