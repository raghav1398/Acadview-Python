Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> import json
>>> r = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&key=435251")
>>> d = json.loads(r.text)
>>> print(r)
<Response [200]>
>>> print(r.status_code)
200
>>> print(r.content)
b'{"quoteText":"Build up your weaknesses until they become your strong points. ", "quoteAuthor":"Knute Rockne", "senderName":"", "senderLink":"", "quoteLink":"http://forismatic.com/en/79c116d9a5/"}'
>>> print(d["quoteText"])
Build up your weaknesses until they become your strong points. 
>>> 
