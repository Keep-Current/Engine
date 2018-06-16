from centrifuge.shared.domain_model import DomainModel


class Document(object):

    def __init__(self, id, url, title, content, keywords, topics, vectorized):
        self.id = id
        self.url = url
        self.title = title
        self.content = content
        self.keywords = keywords
        self.topics = topics
        self.vectorized = vectorized

    @classmethod
    def from_dict(cls, adict):
        doc = Document(
            id = adict['id'],
            url=adict['url'],
            title=adict['title'],
            content=adict['content'],
            keywords=adict['keywords'],
            topics=adict['topics'],
            vectorized=adict['vectorized'],
        )

        return doc

DomainModel.register(Document)