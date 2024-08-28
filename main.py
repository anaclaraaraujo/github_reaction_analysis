from api import fetch_repositories, fetch_pull_requests, fetch_issues
from processing import process_reactions
from bd import create_tables

def main():
    create_tables()
    
    print(f"\nBuscando repositórios da Apache que utilizam linguagens específicas...")
    repositories = fetch_repositories()
    
    if repositories:
        for repo in repositories:
            print(f"Processando repositório: {repo['name']} ({repo['language']})")
            
            owner = repo['owner']['login']
            repo_name = repo['name']
            repo_id = repo['id']  # Para uso na inserção
            
            # Buscar e processar pull requests
            pull_requests = fetch_pull_requests(owner, repo_name)
            if pull_requests:
                process_reactions(owner, repo_name, repo_id, 'pulls', pull_requests)
            
            # Buscar e processar issues
            issues = fetch_issues(owner, repo_name)
            if issues:
                process_reactions(owner, repo_name, repo_id, 'issues', issues)
                
    else:
        print(f"Não foram encontrados repositórios com as linguagens especificadas.")

if __name__ == "__main__":
    main()
