import time
from api import fetch_repositories
from processing import fetch_items_with_reactions
from database import save_to_csv

def main():
    org_name = "apache"
    languages = ["php"]  # Pode adicionar mais linguagens aqui

    all_data = []

    # Buscar todos os repositórios da organização a partir de 2020
    repositories = fetch_repositories(org_name)

    for repo in repositories:
        repo_name = repo['name']
        print(f"Buscando Pull Requests e Issues para o repositório {repo_name}...")
        
        # Pausar entre os repositórios
        time.sleep(2)

        for language in languages:
            print(f"Buscando Pull Requests com reações para {language}...")
            pull_requests = fetch_items_with_reactions(org_name, language, "pr")
            all_data.extend(pull_requests)

            print(f"Buscando Issues com reações para {language}...")
            issues = fetch_items_with_reactions(org_name, language, "issue")
            all_data.extend(issues)

        time.sleep(2)


    # Salvar os dados no arquivo CSV
    save_to_csv(all_data, "php.csv")

if __name__ == "__main__":
    main()