from ll import LinkedList, Node


songs = [
    ('Losing It', 'Fisher', 'Losing It'),
    ('Rapture', 'Anyma & Massano', 'Rapture'),
    ('Red Light', 'Anyma', 'A Mirror Without Reflection'),
    ('Welcome to the Opera', 'Anyma', 'Welcome to the Opera'),
    ('Explore Your Future', 'Anyma', 'Explore Your Future'),
    ('Eternity', 'Chris Avantgarde & Anyma', 'Eternity'),
    ('Innerbloom', 'RÜFÜS DU SOL', 'Bloom'),
    ('Alive', 'Massano', 'Alive'),
    ('Pacha Massive', 'Massano', 'Pacha Massive'),
    ('Closer', 'Massano & Anyma', 'Closer'),
    ('Realm of Consciousness', 'Chris Avantgarde', 'Realm of Consciousness'),
    ('Sentient Being', 'Chris Avantgarde', 'Sentient Being'),
    ('Affection', 'Chris Avantgarde', 'Affection'),
    ('Fade to Black', 'Bicep', 'Bicep'),
    ('Glue', 'Bicep', 'Bicep'),
    ('Atlas', 'Bicep', 'Isles'),
    ('Cazenove', 'Bicep', 'Isles'),
    ('Saku', 'Bicep ft. Clara La San', 'Isles'),
    ('Human', 'Bicep', 'Isles'),
    ('Sundial', 'Bicep', 'Isles'),
    ('Last Night', 'Modjo', 'Modjo'),
    ('Music Sounds Better With You', 'Stardust', 'Music Sounds Better With You'),
    ('Together', 'Disclosure', 'Settle'),
    ('White Noise', 'Disclosure ft. AlunaGeorge', 'Settle'),
    ('Latch', 'Disclosure ft. Sam Smith', 'Settle'),
    ('You & Me', 'Disclosure ft. Eliza Doolittle', 'Settle'),
    ('Pyramid', 'Disclosure ft. Sam Smith', 'Settle'),
    ('When a Fire Starts to Burn', 'Disclosure', 'Settle'),
    ('Voices', 'Russ Yallop', 'Voices'),
    ('Go', 'Moby', 'Go'),
    ('Porcelain', 'Moby', 'Play'),
    ('Find My Baby', 'Moby', 'Play'),
    ('Why Does My Heart Feel So Bad', 'Moby', 'Play'),
    ('We Are Your Friends', 'Justice vs Simian', 'We Are Your Friends'),
    ('D.A.N.C.E.', 'Justice', 'Cross'),
    ('Civilization', 'Justice', 'Audio Video Disco'),
    ('Phantom', 'Justice', 'Cross'),
    ('Genesis', 'Justice', 'Cross'),
    ('One More Time', 'Daft Punk', 'Discovery'),
    ('Around the World', 'Daft Punk', 'Homework'),
    ('Get Lucky', 'Daft Punk ft. Pharrell Williams', 'Random Access Memories'),
    ('Instant Crush', 'Daft Punk ft. Julian Casablancas', 'Random Access Memories'),
    ('Within', 'Daft Punk', 'Random Access Memories'),
    ('Harder Better Faster Stronger', 'Daft Punk', 'Discovery'),
    ('Digital Love', 'Daft Punk', 'Discovery'),
    ('Something About Us', 'Daft Punk', 'Discovery'),
    ('Nightcall', 'Kavinsky', 'Outrun'),
    ('Testarossa Autodrive', 'Kavinsky', 'Outrun'),
    ('Protovision', 'Kavinsky', 'Outrun'),
    ('ProtoVision Remix', 'Kavinsky ft. CD Project', 'Outrun'),
]


def build_playlist(song_list: list) -> LinkedList:
    playlist = LinkedList()

    for song, artist, album in song_list:
        node = Node(song, artist, album)
        playlist.insert_at_end(node)

    return playlist


playlist = build_playlist(songs)
print(playlist)
