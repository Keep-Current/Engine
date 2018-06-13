from centrifuge.shared import use_case as uc
from centrifuge.shared import response_object as res

class ArxivDocumentListUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        arxiv_documents = self.repo.list(filters=request_object.filters)
        
        return res.ResponseSuccess(arxiv_documents)