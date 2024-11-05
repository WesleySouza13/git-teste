import requests
requisicao = requests.get('https://api.kanye.rest')

##mostra requisicao 
frase  = requisicao.json()

print('o absurdo que o kanye disse é:', frase)