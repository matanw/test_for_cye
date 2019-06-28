
import requests
res=requests.post("http://localhost:5000/wordsStats/",json={ "url": "https://www.w3schools.com/python/ref_string_split.asp", "desired_words":["can","the","to"]})
print(res.text)



res=requests.post("http://localhost:5000/login/",json={ "username": "user1","password":"pass1"})
print(res.text)
token1=res.json()["access_token"]
res=requests.post("http://localhost:5000/login/",json={ "username": "user2","password":"pass2"})
print(res.text)
token2=res.json()["access_token"]
res=requests.post("http://localhost:5000/wordsStats/",json={ "url": "https://www.w3schools.com/python/ref_string_split.asp", "desired_words":["can","the"]},
                   headers={"Authorization": "Bearer "+token1})
print(res.text)
res=requests.get("http://localhost:5000/wordsStats/",
                   headers={"Authorization": "Bearer "+token1})


res=requests.post("http://localhost:5000/wordsStats/",json={ "url": "https://www.w3schools.com/python/ref_string_split.asp", "desired_words":["to"]},
                   headers={"Authorization": "Bearer "+token2})
print(res.text)
res=requests.get("http://localhost:5000/wordsStats/",
                   headers={"Authorization": "Bearer "+token2})
print(res.text)

