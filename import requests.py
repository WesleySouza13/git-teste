import requests
requisicao = requests.get('https://api.kanye.rest')

##mostra requisicao 
print(requisicao.json())