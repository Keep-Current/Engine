import uuid
from centrifuge.domain import document

test_url = 'https://arxiv.org/abs/1801.06605'
test_title = 'A Collaborative Filtering Recommender System'
test_content = 'The use of relevant metrics of software systems could improve various software engineering tasks, but'
test_keywords = ['recommender system', 'machine learning']
test_topics = ['recommender system']
test_vector = [1,2,3,4,5]

def test_Doc_model_init():
    code = uuid.uuid4()
    doc = document.Document(
        id=code,
        url=test_url,
        title = test_title,
        content = test_content,
        keywords = test_keywords,
        topics = test_topics,
        vector = test_vector
    )
    assert doc.id == code
    assert doc.url == test_url
    assert doc.title == test_title
    assert doc.content == test_content
    assert doc.keywords == test_keywords
    assert doc.topics == test_topics
    assert doc.vector == test_vector


def test_doc_model_from_dict():
    code = uuid.uuid4()
    doc = document.Document.from_dict(
        {
            'id': code,
            'url': test_url,
            'title': test_title,
            'content': test_content,
            'keywords': test_keywords,
            'topics': test_topics,
            'links': [
                { 
                    'title': 'pdf',
                    'href': 'https://arxiv.org/pdf/1801.06605'
                }
            ]
        }
    )
    assert doc.id == code
    assert doc.url == test_url
    assert doc.title == test_title
    assert doc.content == test_content
    assert doc.keywords == test_keywords
    assert doc.topics == test_topics
    assert doc.vector == test_vector
