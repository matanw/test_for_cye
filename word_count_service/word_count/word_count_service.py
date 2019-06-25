import requests


class WordCountService():
    def get_word_stats(self, url, desired_words):
        return self.get_stats(requests.get(url).text, desired_words)

    def get_stats(self,text, desired_words):
        result = dict()
        for word in text.split():
            if word in desired_words:
                result[word] = result[word] + 1 if word in result else 1
        return result

word_count_service=WordCountService()