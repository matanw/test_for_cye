import requests

def get_word_stats(url,desired_words):

    return get_stats(requests.get(url).text,desired_words)

def get_stats(text,desired_words):
    result=dict()
    for word in text.split():
        if word in desired_words:
            result[word]= result[word]+1 if word in result else 1
    return result

def get_stats111(text,desired_words):
    stats={w:0 for w in desired_words}
    for word in text.split():
        if word in stats:
            stats[word]= stats[word]+1 
    return stats

url="https://www.w3schools.com/python/ref_string_split.asp"
print(get_word_stats(url,["can","the","to"]))
print(get_stats("the to to gg to",["can","the","to"]))