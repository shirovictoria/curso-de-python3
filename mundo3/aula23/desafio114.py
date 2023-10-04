"""
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""
import requests

url = "http://www.pudim.com.br"

try:
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a resposta foi bem-sucedida (status code 200)
    print(f"O site {url} está acessível.")
except requests.exceptions.HTTPError as errh:
    print(f"Ocorreu um erro HTTP: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Erro de conexão: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Tempo de espera excedido: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Erro ao fazer a requisição: {err}")
