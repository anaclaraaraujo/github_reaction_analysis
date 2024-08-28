import sqlite3

# Conectar ao banco de dados SQLite (será criado se não existir)
db_path = 'github_data.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS reactions (
                        id INTEGER PRIMARY KEY,
                        repository_id INTEGER,
                        type TEXT,
                        title TEXT,
                        html_url TEXT,
                        like INTEGER DEFAULT 0,
                        dislike INTEGER DEFAULT 0,
                        laugh INTEGER DEFAULT 0,
                        hooray INTEGER DEFAULT 0,
                        confused INTEGER DEFAULT 0,
                        heart INTEGER DEFAULT 0,
                        rocket INTEGER DEFAULT 0,
                        eyes INTEGER DEFAULT 0)''')
    conn.commit()

def insert_reaction(item, repo_id, type, reactions_summary):
    cursor.execute('''INSERT INTO reactions (id, repository_id, type, title, html_url, like, dislike, laugh, hooray, confused, heart, rocket, eyes)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                      (item['id'], repo_id, type, item['title'], item['html_url'],
                       reactions_summary['like'], reactions_summary['dislike'],
                       reactions_summary['laugh'], reactions_summary['hooray'],
                       reactions_summary['confused'], reactions_summary['heart'],
                       reactions_summary['rocket'], reactions_summary['eyes']))
    conn.commit()
