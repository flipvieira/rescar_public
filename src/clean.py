from config import DATA_DIR, DATA_CLEAN
import pandas as pd

# -------------------------------------------------------------------------------------
# LIMPEZA DE DIAS DA SEMANA E ADEQUAÇÃO DOS VALORES DECIMAIS
# -------------------------------------------------------------------------------------

# Por conta da forma como as tabelas da Wikipedia são estruturadas, ocorre um ruído nos scripts de extração e
# transformação, que por vezes registram o dia do desfile como nome de uma escola desfilando. Optei por corrigir isso
# apenas na etapa de limpeza, depois da transformação, por questão de simplicidade e eficiência: buscar valores
# inadequados em uma coluna, sabendo que a estrutura de colunas está correta, permite descartar como inadequada toda
# a linha de uma só vez.


def clean(file, file_name, csv):

    # Armazena dias da semana para checagem no arquivo passado

    dias = ['Sábado', 'Sabado', 'Domingo', 'Segunda', 'Terça', 'Terca']


    # Itera index,valor pelas linhas do .csv testando se alguma delas contém algum valor na lista dias na coluna
    # 'escola' e, caso sim, elimina essa linha pelo index

    for index,row in file.iterrows():

        if any(d in row['escola'] for d in dias):
            file = file.drop(index)


    # Converte todos os valores da coluna 'nota' em float evitando que erros paralisem o fluxo

    file['nota'] = pd.to_numeric(file['nota'], errors='coerce').astype(float)


    # Itera index,valor pelas linhas do .csv corrigindo as notas para decimais caso sejam menores que 0 ou
    # maiores que 10

    for index,row in file.iterrows():

        nota = row['nota']

        if nota < 0 or nota > 10:
            file.loc[index, 'nota'] = nota/10


    # Caminho de saída do(s) arquivo(s) limpo(s), cria o diretório se não existir

    opath = DATA_CLEAN / f'{file_name}.csv'
    opath.parent.mkdir(parents=True, exist_ok=True)


    # Salva o .csv

    file.to_csv(opath, index=False)


    # Log indicando qual arquivo foi processado

    print(f'{csv.stem}: Clean completo.')

    return file


def main():

    # Pede um input do usuário indicando em qual pasta deve ocorrer a limpeza (se fez merge, deve limpar o merge; caso
    # contrário, deve limpar o conteúdo da pasta transformed

    pasta = input('Diretório [transformed, merged]: ')

    fpath = DATA_DIR / f'{pasta}' / 'csv'


    # Itera por todos os arquivos .csv da pasta, determina o nome de saída e os passa pela função clean(file)

    for csv in fpath.glob('*.csv'):

        file_name = f'{csv.stem}'

        f = pd.read_csv(csv)

        clean(f, file_name, csv)


if __name__ == "__main__":
    main()