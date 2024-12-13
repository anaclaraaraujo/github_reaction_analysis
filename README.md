# GitHub Reaction Analysis

Este projeto realiza a análise de reações em issues e pull requests de repositórios GitHub. Ele utiliza a API do GitHub para buscar informações sobre os repositórios (nome, descrição, linguagem, quantidade de reações), processá-los e salvar os resultados em um arquivo CSV para análise posterior.

## 📋 Funcionalidades

- Busca de repositórios de uma organização criada a partir de 2020.
- Análise de issues e pull requests com reações específicas.
- Filtro por linguagens de programação e tipos de conteúdo (issues ou pull requests).
- Exportação dos resultados para um arquivo CSV.

## 🗂️ Estrutura do Projeto

```plaintext
github_reaction_analysis/
├── api.py               # Funções para interação com a API do GitHub
├── database.py          # Lógica para salvar dados no CSV
├── processing.py        # Processamento e filtragem dos dados
├── main.py              # Ponto de entrada do programa
├── .env                 # Configurações de ambiente (API key do GitHub)
└── requirements.txt     # Dependências do projeto
```

### Descrição dos Módulos

- **`api.py`**  
  Contém funções para interagir com a API do GitHub, como:
  - `fetch_repositories`: Busca repositórios de uma organização criados após 2020.

- **`database.py`**  
  Gerencia a gravação dos resultados processados em arquivos CSV.

- **`processing.py`**  
  Contém a lógica de processamento, como:
  - Busca de issues e pull requests com reações específicas.
  - Filtragem por data e soma de reações válidas.

- **`main.py`**  
  Ponto de entrada do programa. Organiza a execução do fluxo:
  1. Busca repositórios de uma organização.
  2. Coleta e processa dados de issues e pull requests.
  3. Salva os dados em um arquivo CSV.

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- Conta no GitHub com um token de acesso configurado

### Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/anaclaraaraujo/github_reaction_analysis.git
   cd github_reaction_analysis
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o arquivo `.env`:
   Crie um arquivo `.env` na raiz do projeto e adicione:
   ```env
   GITHUB_TOKEN=seu_token_do_github
   ```

   > Substitua `seu_token_do_github` por um [token de acesso do GitHub](https://github.com/settings/tokens). 
   A opção `public_repo` é o suficiente.

### Execução

1. Execute o programa:
   ```bash
   python main.py
   ```

2. O programa salvará os resultados no arquivo `github_reaction_analysis.csv` (ou outro nome configurado).

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **Requests**: Para realizar chamadas HTTP na API do GitHub.
- **CSV**: Para salvar os dados processados.
- **dotenv**: Para carregar variáveis de ambiente.

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).
