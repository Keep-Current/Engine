from centrifuge.shared import use_case as uc
from centrifuge.shared import response_object as res

from centrifuge.actions.topics import extract_topics

class CompareDocumentListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        unparsed_documents = self.repo.list(filters=request_object.filters)

        topic_extractor = extract_topics.TopicExtractor()
        topic_extractor.initialize_corpus()

        parsed_documents = topic_extractor.compare_docs(unparsed_documents)
        
        return res.ResponseSuccess(parsed_documents)