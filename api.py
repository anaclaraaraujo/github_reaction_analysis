import requests
from dotenv import load_dotenv
import os

load_dotenv()

# URL base da API do GitHub
BASE_URL = 'https://api.github.com'
HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'  # Use o token do arquivo .env
}

def fetch_repositories(org='apache'):
    languages_query = ' '.join([f'language:{lang}' for lang in ['JavaScript', 'Python', 'TypeScript', 'Java', 'C#']])
    query = f'org:{org} {languages_query}'
    url = f'{BASE_URL}/search/repositories?q={query}&sort=stars&order=desc'
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json().get('items', [])
    except requests.RequestException as e:
        print(f"Erro ao buscar repositórios: {e}")
        return []

def fetch_pull_requests(owner, repo):
    url = f'{BASE_URL}/repos/{owner}/{repo}/pulls?state=all'
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao buscar pull requests: {e}")
        return []

def fetch_issues(owner, repo):
    url = f'{BASE_URL}/repos/{owner}/{repo}/issues?state=all'
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao buscar issues: {e}")
        return []

def fetch_reactions(owner, repo, type, number):
    url = f'{BASE_URL}/repos/{owner}/{repo}/{type}/{number}/reactions'
    
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 404:
            print(f"Reações não encontradas para {type} #{number}")
            return []
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao buscar reações: {e}")
        return []
