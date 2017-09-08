class Song():
    def __init__(self, author, title, stanzas):
        self.author = author
        self.title = title
        self.stanzas = stanzas

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def show(self):
        print('Author: %s' % self.author)
        print('Title: %s' % self.title)

        for stanza in self.stanzas:
            print('\n%s' % '\n'.join(stanza))

