from datetime import datetime
import time
import requests
from api import HEADERS, GITHUB_API_URL

VALID_REACTIONS = ["+1", "-1", "laugh", "hooray", "confused", "heart", "rocket", "eyes"]

def fetch_items_with_reactions(org_name, language, content_type):
    """
    Busca issues ou pull requests de um repositório de uma organização específica
    que possuem reações.
    """
    url = f"{GITHUB_API_URL}/search/issues"
    params = {
        "q": f"org:{org_name} language:{language} is:{content_type}",
        "per_page": 100,
    }
    items_with_reactions = []

    while url:
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Erro ao buscar {content_type}: {response.status_code}, {response.text}")
            break

        data = response.json()
        for item in data.get("items", []):
            created_at = datetime.strptime(item["created_at"], '%Y-%m-%dT%H:%M:%SZ')
            
            # Filtrando items criados após 01-01-2020
            if created_at < datetime(2020, 1, 1):
                continue
            
            reactions = item.get("reactions", {})

            # Filtrar apenas reações válidas e somar
            total_reactions = sum(
                int(reactions.get(key, 0)) for key in VALID_REACTIONS if key in reactions
            )
            if total_reactions > 0:
                items_with_reactions.append({
                    "type": content_type,
                    "title": item["title"],
                    "url": item["html_url"],
                    "created_at": item["created_at"],
                    "updated_at": item["updated_at"],
                    "labels": ", ".join(label["name"] for label in item.get("labels", [])),
                    **{key: reactions.get(key, 0) for key in VALID_REACTIONS},
                    "language": language,
                })

        url = response.links.get("next", {}).get("url")
        time.sleep(2)

    return items_with_reactions