from flask import request
from flask_restplus import Namespace, Resource, fields

from word_count_service.word_count.word_count_service import word_count_service

ns = Namespace('wordsCount', description='Cats related operations')

word_count_requests = ns.model('Words Count Requerst', {
    'url': fields.String(required=True, description='The url to fetch'),
    'desired_words': fields.List(fields.String,required=True, description='The word fetch stats on'),
})
word_stats = ns.model('Words Count Requests', {
    'word': fields.String(required=True, description='The word'),
    'frequency': fields.Integer(description='The word fetch stats on'),
})

@ns.route('/')
class WordsCountApi(Resource):
    @ns.doc('fetch words frequencies by url')
    @ns.expect(word_count_requests)
    @ns.marshal_list_with(word_stats)
    def post(self):
        payload=request.json
        stats=word_count_service.get_word_stats(payload["url"],payload["desired_words"])
        return [{'word':key,'frequency':value} for key, value in stats.items()]
