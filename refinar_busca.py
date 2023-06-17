from buscar_yt import buscar_link_youtube

def refinar_busca(ano_refinar, artista, ano_musica, nm_musica, qt_popularidade):
    opcoes_refinadas = []
    for i, ano in enumerate(ano_musica):
        if ano == ano_refinar:
            opcoes_refinadas.append((nm_musica[i], qt_popularidade[i]))

    if opcoes_refinadas:
        opcoes_refinadas = sorted(opcoes_refinadas, key=lambda x: x[1], reverse=True)[:3]
        print(f"Opções encontradas para o ano {ano_refinar}:")
        for musica, popularidade in opcoes_refinadas:
            link_youtube = buscar_link_youtube(musica)
            print("Opção:", musica)
            print("Link no YouTube:", link_youtube)

        gostou_refinado = input("Você gostou de alguma dessas opções? (sim/não): ")
        if gostou_refinado.lower() == 'sim':
            print("Ótimo! Fico feliz que tenha gostado.")
        else:
            print("Que pena. Não encontramos mais opções para você.")
    else:
        print(f"Não foram encontradas opções para o ano {ano_refinar}.")
