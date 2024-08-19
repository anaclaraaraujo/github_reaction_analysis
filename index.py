import requests

BASE_URL = 'https://api.github.com/search/repositories'

def fetch_one_repository(org='apache'):

    query = f'org:{org}'
    
    url = f'{BASE_URL}?q={query}&sort=stars&order=desc&per_page=1'
    
    try:
        response = requests.get(url)
        
        response.raise_for_status()
        
        repo = response.json().get('items', [])[0]
        return repo
    
    except requests.RequestException as e:
        print(f"Erro ao buscar repositório: {e}")
        return None
    except IndexError:
        print("Nenhum repositório encontrado.")
        return None

repository = fetch_one_repository()

if repository:
    print(f"Nome do Repositório: {repository['name']}")
    print(f"URL do Repositório: {repository['html_url']}")
else:
    print("Não foi possível obter informações sobre o repositório.")
