import csv

# Caminho do arquivo CSV
caminho_arquivo = 'fixtures/dados_musicas.csv'


def inserir_planilha(ano, artista, explicito, musica, popularidade):
    insere_ano = ano
    insere_artista = artista
    insere_musica = musica
    insere_explicito = explicito
    insere_popularidade = popularidade
    nome_musica_completo = insere_artista + " - " + insere_musica

    insere_explicito = 1 if insere_explicito == "sim" else 0

    dados = [insere_ano, insere_artista, insere_explicito, insere_musica, (int(insere_popularidade) * 10), '', nome_musica_completo]

    with open(caminho_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
        linhas = list(csv.reader(arquivo_csv, delimiter=';'))

    linhas.append(dados)

    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv, delimiter=';')

        # Escrever as linhas atualizadas no arquivo
        writer.writerows(linhas)

    print('Dados inseridos na última linha com sucesso!')
