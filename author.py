class Author():
    def __init__(self, name, songs):
        self.name = name
        if songs != None:
            self.songs = songs
        else:
            self.songs = []
