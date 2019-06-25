
import requests
res=requests.post("http://localhost:5000/wordsCount/",json={ "url": "https://www.w3schools.com/python/ref_string_split.asp", "desired_words":["can","the","to"]})
print(res.text)