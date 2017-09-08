class Song():
    def __init__(self, author, title, stanzas):
        self.author = author
        self.title = title
        self.stanzas = stanzas

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        print(self.__dict__)
        print(other.__dict__)
        return self.__dict__ == other.__dict__
