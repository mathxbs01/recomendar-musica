import random
from inserir import inserir_planilha
from refinar_busca import refinar_busca
from buscar_yt import buscar_link_youtube

caminho_arquivo = 'fixtures/dados_musicas.csv'

def ler_arquivo_csv(caminho_arquivo):
    try:
        import csv
    except ImportError:
        print("Erro: O módulo 'csv' não está disponível.")
        print("Verifique se o módulo 'csv' está instalado corretamente.")
        return
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo_csv:            
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')
        qt_popularidade = []
        nm_musica = []
        ano_musica = []

        # Ignorar a primeira linha
        next(leitor_csv)   

        while True:
            arquivo_csv.seek(1)
            encontrado = False
            artista = input("Qual o nome do seu artista preferido? (ou digite 'parar' para sair): ")
            
            if artista.lower() == 'parar':
                break            

            for coluna in leitor_csv:
                if len(coluna) >= 2 and coluna[1] == artista:
                    list_popularidade = coluna[4]
                    list_musica = coluna[6]
                    list_ano = coluna[0]
                    try:
                        popularidade = float(list_popularidade)
                        qt_popularidade.append(popularidade)
                        nm_musica.append(list_musica)
                        ano_musica.append(list_ano)
                        encontrado = True
                    except ValueError:
                        pass

            if encontrado:
                maiores_valores_indices = sorted(range(len(qt_popularidade)), key=lambda i: qt_popularidade[i], reverse=True)[:3]
                opcoes = []
                for indice in maiores_valores_indices:
                    musica = nm_musica[indice]
                    opcoes.append(musica)
                    link_youtube = buscar_link_youtube(musica)
                    print("Opção:", musica)
                    print("Link no YouTube:", link_youtube)
                
                gostou = input("Você gostou de alguma dessas opções? (sim/não): ")
                if gostou.lower() == 'sim':
                    print("Ótimo! Fico feliz que tenha gostado.")
                else:
                    ano_refinar = input("Qual o ano desejado para refinar a busca? ")
                    refinar_busca(ano_refinar, artista, ano_musica, nm_musica, qt_popularidade)

                    if gostou.lower() == 'sim':
                        print("Ótimo! Fico feliz que tenha gostado.")
                    else:
                        print("Infelizmente não foi possível encontrar a música baseadas nas informações disponibilizadas. Para que possa nos ajudar, informe outros dados:")
                        arquivo_csv.close()
                        inserir_planilha(ano = input("Digite o ano da música: "),
                           artista = input("Digite o nome do artista: "),
                           musica = input("Digite o nome da música: "),
                           explicito = input("Considera uma música explicita (sim/não)? "),
                           popularidade = input("De 0 à 10, qual a popularidade da música: ")
                           )
                break  # Encerra o loop quando a busca é encontrada
            else:
                print("Não foi possível encontrar. Tente novamente.")

ler_arquivo_csv(caminho_arquivo)
