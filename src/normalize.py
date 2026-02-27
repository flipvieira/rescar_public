import pandas as pd
from config import DATA_DIR, DATA_NORM, DATA_MERGED

# -------------------------------------------------------------------------------------
# EXTRAÇÃO DE PLANILHAS DA WIKIPEDIA CONTENDO OS RESULTADOS DO CARNAVAL NO RJ
# -------------------------------------------------------------------------------------

# Esse script tem o objetivo de normalizar os dados já passados pelo script clean.py, para adequá-los ao formato
# específico do banco de dados PostgreSQL que modelei e implementei nesse projeto


# Dicionário de sinônimos

dn = {
'Acadêmicos da Rocinha': ['Rocinha', 'A. da Rocinha', 'A. Rocinha'],
'Acadêmicos de Niterói': ['Niterói', 'A. de Niterói', 'A. Niterói'],
'Acadêmicos de Santa Cruz': ['Santa Cruz', 'A. de Santa Cruz', 'A. Santa Cruz'],
'Acadêmicos do Grande Rio': ['Grande Rio', 'A. do Grande Rio', 'A. Grande Rio'],
'Beija-Flor de Nilópolis': ['Beija-Flor', 'Beija Flor'],
'Caprichosos de Pilares': ['Caprichosos', 'C. de Pilares'],
'Estácio de Sá': ['Estácio'],
'Imperatriz Leopoldinense': ['Imperatriz', 'I. Leopoldinense'],
'Império da Tijuca': ['I. Tijuca'],
'Império Serrano': ['I. Serrano', 'Império'],
'Inocentes de Belford Roxo': ['Inocentes', 'I. de Belford Roxo'],
'Mangueira': ['Estação Primeira de Mangueira', 'E.P. de Mangueira'],
'Mocidade Independente de Padre Miguel': ['Mocidade', 'Mocidade Independente'],
'Paraíso do Tuiuti': ['P. do Tuiuti', 'Tuiuti'],
'Portela': ['GRES Portela'],
'Porto da Pedra': ['P. da Pedra'],
'Renascer de Jacarepaguá': ['Renascer', 'R. de Jacarépaguá'],
'Salgueiro': ['GRES Salgueiro', 'Acadêmicos do Salgueiro', 'A. do Salgueiro'],
'São Clemente': ['S. Clemente', 'S.Clemente'],
'Tradição': ['GRES Tradição'],
'União da Ilha do Governador': ['União da Ilha', 'U. da Ilha'],
'União da Ponte': ['U. da Ponte'],
'Unidos da Tijuca': ['Tijuca', 'U. da Tijuca', 'U.da Tijuca'],
'Unidos de Padre Miguel': ['UPM', 'U. de Padre Miguel'],
'Vila Isabel': ['Unidos de Vila Isabel', 'U. de Vila Isabel', 'U. Vila Isabel', 'V. Isabel'],
'Viradouro': ['Unidos do Viradouro', 'U. do Viradouro']
}

alias_map = {
    alias: escola
    for escola, aliases in dn.items()
    for alias in aliases
}

def normalize(csv):

    csv['escola'] = csv['escola'].replace(alias_map)

    return csv

def main():

    pasta = input('Diretório [transformed, clean, merged]: ')
    opath = DATA_NORM
    opath.mkdir(parents=True, exist_ok=True)


    if pasta in ['transformed', 'clean']:

        fpath = DATA_DIR / f'{pasta}' / 'csv'

        for file in fpath.glob('*csv'):

            f = pd.read_csv(file)

            normalize(f).to_csv(opath / f'{file.stem}_normalized.csv')

    elif pasta == 'merged':
        fpath = DATA_MERGED

        for file in fpath.glob('*csv'):
            f = pd.read_csv(file)

            normalize(f).to_csv(opath / f'{file.stem}_normalized.csv', index=False)



if __name__ == '__main__':
    main()