from api import fetch_reactions
from bd import insert_reaction  # Importe a função insert_reaction

def process_reactions(owner, repo_name, repo_id, type, items):
    for item in items:
        print(f"Processando {type}: {item['title']}")
        
        reactions = fetch_reactions(owner, repo_name, type, item['number'])
        
        reactions_summary = {
            'like': sum(1 for r in reactions if r['content'] == '+1'),
            'dislike': sum(1 for r in reactions if r['content'] == '-1'),
            'laugh': sum(1 for r in reactions if r['content'] == 'laugh'),
            'hooray': sum(1 for r in reactions if r['content'] == 'hooray'),
            'confused': sum(1 for r in reactions if r['content'] == 'confused'),
            'heart': sum(1 for r in reactions if r['content'] == 'heart'),
            'rocket': sum(1 for r in reactions if r['content'] == 'rocket'),
            'eyes': sum(1 for r in reactions if r['content'] == 'eyes')
        }
        
        if any(reactions_summary.values()):  # Verifica se há pelo menos uma reação
            insert_reaction(item, repo_id, type, reactions_summary)
