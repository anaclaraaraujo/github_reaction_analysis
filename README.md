# 📊 Análise de Sentimentos e Reações em Issues e Pull Requests no GitHub

## 📌 Visão Geral
Este projeto realiza a coleta e análise de issues e pull requests de repositórios pertencentes a uma organização no GitHub. O foco principal é identificar padrões de sentimento e interação entre os colaboradores, utilizando a API da OpenAI para análise de sentimentos e processando reações dos usuários (como 👍, 🎉, ❤️, etc.).

## 🚀 Funcionalidades
- **Coleta de dados**: Extrai issues e pull requests de repositórios de uma organização do GitHub.
- **Filtragem inteligente**: Considera apenas issues e pull requests com as labels `bug` ou `enhancement` e que receberam reações.
- **Análise de sentimento**: Utiliza a OpenAI para classificar os sentimentos das interações como **Positiva, Negativa ou Neutra**.
- **Processamento de reações**: Conta e analisa a influência das reações no tempo de resolução.
- **Geração de relatório**: Produz um relatório detalhado com insights e estatísticas.
- **Visualização de dados**: Cria gráficos para facilitar a interpretação dos resultados.

## 🛠 Tecnologias Utilizadas
- **Python** (Pandas, Matplotlib, Seaborn)
- **Google Colab** (para execução e processamento)
- **GitHub API** (coleta de issues e pull requests)
- **OpenAI API** (análise de sentimentos)
- **Google Drive** (armazenamento dos relatórios e gráficos)

## 📊 Resultados Obtidos
- **Correlação entre reações e tempo de resolução**
- **Distribuição de sentimentos em issues e pull requests**
- **Impacto das reações na resolução de problemas**
- **Tendências de sentimentos por tipo de tarefa (`bug` vs `enhancement`)**