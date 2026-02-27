import pandas as pd
from config import DATA_RAW, DATA_TRANSF

# -------------------------------------------------------------------------------------
# TRANSFORMAÇÃO DE DADOS COLETADOS EM .CSV PELO SCRIPT DE EXTRAÇÃO
# -------------------------------------------------------------------------------------


# Diretório do input path

ipath = DATA_RAW


# Retorna uma lista com o formato ['escola1', ['q1', 'j1', 'n1'], ['q2, 'j2', 'n3'], ...]

def transform_resultados(csv_path):


    # Armazena a lista

    esc_notas = []


    # Loop que itera da segunda à última linha do .CSV e armazena 'escola', ['quesito', 'jurado', 'nota'],
    # adicionando-os a esc_notas

    for i in range(2, len(csv_path)):


        # Keep track da linha que corresponde a uma escola específica

        escola = i


        # Armazena ['quesito', 'jurado', 'nota']

        for q,j,e in zip(quesitos, jurados, csv_path.values[escola]):


            # Específico para o formato da tabela: se a primeira coluna da linha for 'Escolas', sabemos que e='escola'
            if 'Escolas' in q:
                esc_notas.append(e)


            # Caso contrário, sabemos que q='quesito', j='jurado', e='nota'

            else:
                esc_notas.append([q,j,e])


    # Log indicando qual ano passa pela função

    print(f'{ano_atual}: Processando...')

    return esc_notas


# Recebe como input a lista retornada de transform_resultados(csv_path) e retorna um .csv para cada ano contendo as
# colunas ['escola', 'ano', 'quesito', 'jurado', 'nota'] e os valores correspondentes

# IMPORTANTE: Não limpa a tabela para inserção no banco de dados ainda, apenas formata para facilitar o
# tratamento posterior

def formata_result(transf_result):

    # Armazena a lista de dicionários que a função transforma em .csv

    registros = []


    # Armazena o nome da escola

    escola_atual = None


    # Loop que itera pela lista retornada de transform_resultados(csv_path) e checa se é string ('escola') ou lista ['quesito', 'jurado', 'nota']

    for i in transf_result:


        # Se é escola (str), guarda o nome da escola em escola_atual e pula o resto do loop, começando outra iteração

        if isinstance(i, str):
            escola_atual = i
            continue


        # Se não é escola (list), descompacta quesito, j e nota

        quesito, j, nota = i


        # Ignora a nota total porque será calculada em queries SQL no banco de dados, posteriormente, para evitar redundâncias

        if quesito == "Total":
            continue


        # Adiciona um dicionário com esse formado à lista de dicionários

        registros.append({
            "escola": escola_atual,
            "ano": ano_atual,
            "quesito": quesito,
            "jurado": j,
            "nota": nota
        })


    # Log indicando o processamento do ano
    print(f'{ano_atual}: Processado.')
    return registros


def main():

    # Loop que roda a função transform_resultados(csv_path), passando arquivo por arquivo .csv presente no diretório
    # data/raw/csv, armazena a lista resultante em resultados_transf, passando-a em seguida por
    # formata_result(transf_result), que converte a lista de dicionários resultantes em DataFrame do Pandas e, finalmente,
    # armazena um .csv para cada ano em data/transformed/csv

    for file in ipath.glob('*.csv'):


        # Armazena o ano (nome do arquivo sem extensão)

        global ano_atual
        ano_atual = file.stem


        # Abre o arquivo .csv com o Pandas

        csv = pd.read_csv(file)


        # Caminho de saída dos arquivos, cria o diretório se não existir

        opath = DATA_TRANSF / f'{ano_atual}.csv'
        opath.parent.mkdir(parents=True, exist_ok=True)


        # Especifica a linha de quesitos e a linha de jurados antes de rodar transform_resultados(csv_path)

        global quesitos
        global jurados

        quesitos = csv.values[0]
        jurados = csv.values[1]


        # Executa as funções e armazena em .csv

        resultados_transf = transform_resultados(csv)

        pd.DataFrame(formata_result(resultados_transf)).to_csv(opath, index=False)


if __name__ == "__main__":
    main()