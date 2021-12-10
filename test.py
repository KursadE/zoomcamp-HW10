import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
#data = {'url': 'https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg'}
#data = {'url': 'https://media.istockphoto.com/photos/background-elephant-picture-id479667835'}
#data = {'url': 'https://media.istockphoto.com/photos/african-elephant-bull-drinking-on-the-zambezi-river-picture-id496997908'}
data = {'url': 'https://media.istockphoto.com/photos/monarch-on-yellow-sunflowers-picture-id1210792722'}

result = requests.get(url, json=data).json()

print(result)