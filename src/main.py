import extract
import transform
import clean
import merge
import normalize

# -------------------------------------------------------------------------------------
# APLICAÇÃO PRINCIPAL CHAMANDO TODOS OS SCRIPTS VIA LINHA DE COMANDO
# -------------------------------------------------------------------------------------

# Essa é a aplicação principal, que reúne e chama todos os scripts (extract, transform, merge e clean) por linhas de
# comando


# Dicionário de comandos válidos

VCOM = {
    'extract': extract,
    'transform': transform,
    'clean': clean,
    'merge': merge,
    'normalize': normalize
}


# Aplicação

def main():

    try:
        cmd = input('Inserir comando: ').strip()

        if cmd == '/exit':

            return False


        try:

            print(f'Iniciando {cmd}...')

            VCOM[cmd].main()

            print(f'{cmd.capitalize()} completo.')

        except KeyError:

            print('Comando inválido.')

        return True

    except KeyboardInterrupt:

        print('Encerrando.')

        return False

while main():
    pass
