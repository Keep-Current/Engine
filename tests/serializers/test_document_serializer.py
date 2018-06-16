import datetime
import json
import pytest

from centrifuge.serializers.json import document_serializer as srs
from centrifuge.domain.document import Document

test_url = 'https://arxiv.org/abs/1801.06605'
test_title = 'A Collaborative Filtering Recommender System'
test_content = 'The use of relevant metrics of software systems could improve various software engineering tasks, but'
test_keywords = ['recommender system', 'machine learning']
test_topics = ['recommender system']
test_vectorized = [1,2,3,4,5]


def test_serialize_domain_document():
    doc = Document(
        id = 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
        url= test_url,
        title = test_title,
        content = test_content,
        keywords = test_keywords,
        topics = test_topics,
        vectorized = test_vectorized
        )

    expected_json = """
        {
            "id" : "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "url" : "https://arxiv.org/abs/1801.06605",
            "title" : "A Collaborative Filtering Recommender System",
            "content" : "The use of relevant metrics of software systems could improve various software engineering tasks, but",
            "keywords" : "recommender system,machine learning",
            "topics" : "recommender system",
            "vectorized" : "1,2,3,4,5"
        }
    """

    print(json.loads(json.dumps(doc, cls=srs.DocEncoder)))
    print(json.loads(expected_json))

    assert json.loads(json.dumps(doc, cls=srs.DocEncoder)) == json.loads(expected_json)

def test_serialize_domain_document_wrong_type():
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime.now(), cls=srs.DocEncoder)
