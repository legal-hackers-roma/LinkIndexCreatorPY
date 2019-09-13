from os import path

class Link(object):
    def __init__(self, file, index):
        self.name = file
        self.url = './' + file
        self.index = index + 1

def createLinksArray(files):
    linksArray = []
    for file, index in enumerate(files):
        linksArray.append(Link(index, file))
    return linksArray