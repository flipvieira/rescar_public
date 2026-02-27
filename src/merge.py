import pandas as pd
from config import DATA_DIR, DATA_MERGED

# -------------------------------------------------------------------------------------
# MERGE DE TODOS OS ARQUIVOS .CSV CONTIDOS EM data/raw/transformed
# -------------------------------------------------------------------------------------

# Esse script foi escrito separadamente do de transformação para o caso de se precisar dos arquivos individuais e não
# do merge.


# Função que retorna um nome padronizado para o merge no formato 'resultados_carnaval_1996-AAAA'

def name(ipath):

    oname = f"resultados_carnaval_{ipath.parent.name}_{min([int(i.stem) for i in ipath.glob('*.csv')])}-{max([int(i.stem) for i in ipath.glob('*.csv')])}"

    return oname


def merge_csvs(csv_path):

    opath = DATA_MERGED
    opath.mkdir(parents=True, exist_ok=True)

    # Armazena uma lista de arquivos .csv passados pelo Pandas (DataFrames)

    dfs = []


    # Concatena todos os itens da lista dfs e faz o merge em um .csv unificado

    for f in csv_path.glob('*.csv'):
        dfs.append(pd.read_csv(f))

    pd.concat(dfs).to_csv(opath / f'{name(csv_path)}.csv', index=False)


def main():


    # Diretórios comuns

    pasta = input('Diretório [raw, transformed, clean]: ')
    csv_path = DATA_DIR / f'{pasta}' / 'csv'


    merge_csvs(csv_path)


if __name__ == "__main__":
    main()