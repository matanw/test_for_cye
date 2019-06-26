from flask import request
from flask_restplus import Namespace, Resource, fields

from word_count_service.word_stats.word_stats_service import word_count_service
from word_count_service.word_stats.word_stats_transformer import words_stats_transformer

ns = Namespace('wordsStats', description='words stats')

word_count_requests = ns.model('Words Stats Requerst', {
    'url': fields.String(required=True, description='The url to fetch'),
    'desired_words': fields.List(fields.String,required=True, description='The word fetch stats on'),
})
word_stats_item = ns.model('Words Stats Requests Items', {
    'word': fields.String(required=True, description='The word'),
    'frequency': fields.Integer(description='The word fetch stats on'),
})
word_stats = ns.model('Words Count Requests', {
    'id': fields.Integer(required=True, description='db id'),
    'url': fields.String(description='the url'),
    'results': fields.List(fields.Nested(word_stats_item),description='The word fetch stats on'),
})

@ns.route('/')
class WordsCountApi(Resource):
    @ns.doc('fetch words frequencies by url')
    @ns.expect(word_count_requests)
    @ns.marshal_with(word_stats)
    def post(self):
        payload=request.json
        stats=word_count_service.get_word_stats(payload["url"],payload["desired_words"])
        saved_entity=word_count_service.save_search_results(payload["url"],stats)
        return words_stats_transformer.entity_to_dto(saved_entity)

    @ns.doc('get listl')
    @ns.marshal_list_with(word_stats)
    def get(self):
        stats = word_count_service.get_all()
        return  words_stats_transformer.entities_to_dtos(stats)

