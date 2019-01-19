import lyricsgenius
import json

genius = lyricsgenius.Genius('secret')
genius.verbose = False
genius.excluded_terms = ["(Remix)", "(Live)", "(Demo)"]
genius.remove_section_headers = True
artist = genius.search_artist('Fall Out Boy', max_songs=200)

songs = artist.songs
path = 'lyrics/'

albums = {}

for s in songs:
    filename = "".join(x for x in s.title if x.isalnum())

    if filename:
        pass
    else:
        lyric = s.lyrics[0:30]
        filename = "".join(x for x in lyric if x.isalnum())

    file = path + filename + '.txt'

    with open(file, 'w') as f:
        f.write(s.lyrics)
        f.close()

    albums['song'] = filename
    albums['album'] = s.album

with open('albums.json', 'w') as f:
    f.write(json.dumps(albums))
    f.close()
