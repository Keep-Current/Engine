import json


class DocEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'id': o.id,
                'url': o.url,
                'title': o.title,
                "content": o.content,
                "keywords": ','.join(o.keywords),
                "topics": ','.join(o.topics),
                "vectorized": ','.join(str(x) for x in o.vectorized),
            }
            return to_serialize
            
        except AttributeError:
            return super().default(o)
