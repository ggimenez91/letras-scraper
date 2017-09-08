from lyricsscraper import LyricsScraper

lyrics = LyricsScraper()
songs = lyrics.run(['https://www.letras.com/alfredo-zitarrosa/838111/'])
for song in songs:
    song.show()
