import json
from flask import Blueprint, request, Response

from centrifuge.use_cases import request_objects as req
from centrifuge.shared import response_object as res
from centrifuge.serializers.json import document_serializer as ser

from centrifuge.repository import crawler_arxiv_repo as ar
from centrifuge.use_cases import get_similar_docs_use_case as uc

blueprint = Blueprint('find_similar', __name__)

STATUS_CODES = {
    res.ResponseSuccess.
    SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500
}

@blueprint.route('/find_similar', methods=['GET'])
def arxiv():
    qrystr_params = {
        'doc': {},
    }

    for arg, values in request.args.items():
        if arg.startswith('doc_'):
            qrystr_params['doc'][arg.replace('doc_', '')] = values

    request_object = req.DocumentKeywordsRequestObject.from_dict(qrystr_params)

    repo = ar.CrawlerArxivRepo()

    use_case = uc.GetSimilarDocumentsUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.DocEncoder),
                    mimetype='application/json',
                    headers=[('Access-Control-Allow-Origin', '*')],
                    status=STATUS_CODES[response.type])