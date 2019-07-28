class Source:
    '''
    Source class to define source objects
    '''

    def __init__(self, id, name, description, category, url, country):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.url = url
        self.country = country


class Articles:
    '''
    artoicles class to define source objects
    '''

    def __init__(self, source, author, title, description, url, urlToImage, publishedAt, content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
