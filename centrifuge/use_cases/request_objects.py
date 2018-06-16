import collections

from centrifuge.shared import request_object as req


class DocumentKeywordsRequestObject(req.ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = req.InvalidRequestObject()

        if 'doc' in adict and not isinstance(adict['doc'], collections.Mapping):
            invalid_req.add_error('doc', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return DocumentKeywordsRequestObject(filters=adict.get('doc', None))
