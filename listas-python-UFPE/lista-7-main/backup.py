    if ("Musicas" in gostos_primeiro) and ("Musicas" in gostos_segundo):
        for musica in gostos_primeiro["Musicas"]:
            if musica in gostos_segundo["Musicas"]:
                somar_pontuacao += 2
    
    if ("Series" in gostos_primeiro) and ("Series" in gostos_segundo):
        for serie in gostos_primeiro["Series"]:
            if serie in gostos_segundo["Series"]:
                somar_pontuacao += 2
    
    if ("Filmes" in gostos_primeiro) and ("Filmes" in gostos_segundo):
        for filme in gostos_primeiro["Filmes"]:
            if filme in gostos_segundo["Filmes"]:
                somar_pontuacao += 2

    if ("Livros" in gostos_primeiro) and ("Livros" in gostos_segundo):
        for livro in gostos_primeiro["Livros"]:
            if livro in gostos_segundo["Livros"]:
                somar_pontuacao += 2
