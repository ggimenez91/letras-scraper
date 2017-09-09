class Song():
    def __init__(self, author, title, link, stanzas):
        self.author = author
        self.title = title
        self.link = link
        if stanzas != None:
            self.stanzas = stanzas
        else:
            self.stanzas = []

    def __str__(self):
        result = 'Author: {0}\nTitle: {1}\nLink: {2}\n'.format(self.author,
                self.title, self.link)
        for stanza in self.stanzas:
            result =+ '\n{0}'.format('\n'.join(stanza))
        return result

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
