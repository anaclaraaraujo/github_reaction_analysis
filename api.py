import os
import requests
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github.squirrel-girl-preview+json",
    "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
}

def fetch_repositories(org_name):
    """
    Busca todos os repositórios de uma organização que foram criados a partir de 2020.
    """
    url = f"{GITHUB_API_URL}/orgs/{org_name}/repos"
    params = {"per_page": 100}
    repositories = []
    year_limit = 2020
    while url:
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Erro ao buscar repositórios: {response.status_code}, {response.text}")
            break

        data = response.json()
        for repo in data:
            # Verifique a data de criação e filtre repositórios a partir de 2020
            created_at = datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            if created_at.year >= year_limit:
                repositories.append(repo)
        
        url = response.links.get("next", {}).get("url")  # Paginação
        
        # Pausar por 1 segundo para evitar atingir o limite
        time.sleep(2)

    return repositories