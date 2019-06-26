from flask import request
from flask_restplus import Namespace, Resource, fields

from word_count_service.word_stats.word_stats_service import word_count_service


class WordsStatsTransformer():
    def entity_to_dto(self,entity):
        return {'id':entity.id,
                'url':entity.url,
                'results':[{'word':result.word,'frequency':result.frequency} for result in entity.results]}

    def entities_to_dtos(self,entities):
        return [self.entity_to_dto(entity) for entity in entities]

words_stats_transformer=WordsStatsTransformer()