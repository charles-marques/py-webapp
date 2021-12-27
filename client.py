import requests
# from requests.models import requote_uri

url = 'http://127.0.0.1:5000/vendas'
recurso = requests.get(url)

print(url)
print(recurso)
print(recurso.json())

example_dict = recurso.json()

print(example_dict['total_vendas'])