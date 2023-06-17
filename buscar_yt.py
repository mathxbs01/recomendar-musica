from googleapiclient.discovery import build

# Configuração da chave de API do YouTube
API_KEY = "AIzaSyCP1kNve5Tj3xTEVNPwhCQMWcLjXG86fFE"


def buscar_link_youtube(musica):
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        request = youtube.search().list(q=musica + " official audio", part='id', maxResults=1)
        response = request.execute()
        if 'items' in response:
            video_id = response['items'][0]['id']['videoId']
            link = "https://www.youtube.com/watch?v=" + video_id
            return link
        else:
            print("Não foi possível encontrar o link da música no YouTube.")
            return None
    except Exception as e:
        print("Ocorreu um erro ao buscar o link da música:", str(e))
        return None
