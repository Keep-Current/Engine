from centrifuge.shared import use_case as uc
from centrifuge.shared import response_object as res

from centrifuge.actions.topics import document_similarity

class GetSimilarDocumentsUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        unparsed_documents = self.repo.list(filters=request_object.filters)

        measure_similarity = document_similarity.DocSimilarity()
        measure_similarity.initialize_corpus()

        parsed_documents = measure_similarity.compare_docs(unparsed_documents)
        
        return res.ResponseSuccess(parsed_documents)
