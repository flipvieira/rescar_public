import pandas as pd
import requests
from io import StringIO
from config import DATA_RAW

# -------------------------------------------------------------------------------------
# EXTRAÇÃO DE PLANILHAS DA WIKIPEDIA CONTENDO OS RESULTADOS DO CARNAVAL NO RJ
# -------------------------------------------------------------------------------------


# Armazena os trechos imutáveis comuns a todas as URLs de todos os anos

url_base = "https://pt.wikipedia.org/wiki/Resultados_do_Carnaval_do_Rio_de_Janeiro_em_"


# Loop que itera pelas URLs de 1996 ao ano-limite

def extract_resultados(ano):


    for n in range(1996, ano + 1):


        # Caminho dos arquivos .csv de saída, cria o diretório se não existir

        opath = DATA_RAW / f'{n}.csv'
        opath.parent.mkdir(parents=True, exist_ok=True)


        # A cada iteração, muda o ano na URL

        url = f'{url_base}{n}'


        # Insere headers para o requests não ser barrado pelo servidor

        headers = {
            "User-Agent": "Mozilla/5.0"
        }


        # Armazena o HTML que retorna do requests ao pedido de acesso à URL

        response = requests.get(url, headers=headers)


        # Armazena as tabelas existentes na página, lida como string (atributo .text) pelo StringIO e assim passada
        # pelo Pandas (.read_html)

        tables = pd.read_html(StringIO(response.text))


        # Armazena as tabelas que correspondem ao check booleano no loop abaixo

        valid_table = None


        # Nested loop que itera pelas tabelas e checa se são tabelas de resultados do Grupo Especial

        for df in tables:


            # Triagem de tabelas

            if len(df.columns) > 28:

                valid_table = df
                df.to_csv(opath, header=False, index=False, decimal=',')

                break


        # Log que explicita se algum ano não tiver resultados, como no caso de 2021 (pandemia, não houve carnaval)

        if valid_table is not None:
            print(f'{n}: Processado!')
        else:
            print(f'{n}: Sem carnaval. :(')


def main():


    # Recebe como input um ano-limite inserido pelo usuário

    ano = int(input('Último ano da série: '))


    extract_resultados(ano)


if __name__ == "__main__":
    main()