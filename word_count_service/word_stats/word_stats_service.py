import requests

from word_count_service.db.db_manager import db
from word_count_service.word_stats.word_stats_entities import WordStats, WordStatsResult


class WordStatsService():
    def get_word_stats(self, url, desired_words):
        return self.get_stats(requests.get(url).text, desired_words)

    def get_stats(self,text, desired_words):
        result = dict()
        for word in text.split():
            if word in desired_words:
                result[word] = result[word] + 1 if word in result else 1
        return result

    def save_search_results(self,url, word_stats_result):
        word_stats=WordStats(url=url)
        db.session.add(word_stats)
        for key,value in word_stats_result.items():
            result=WordStatsResult(word=key,frequency=value)
            word_stats.results.append(result)
            db.session.add(result)
        db.session.commit()
        return  word_stats

    def get_all(self):
        return  WordStats.query.all()

word_count_service=WordStatsService()