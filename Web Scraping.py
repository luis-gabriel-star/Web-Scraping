import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.string if soup.title else 'Título não encontrado'
    
    description_tag = soup.find('meta', attrs={'name': 'description'})
    description = description_tag['content'] if description_tag else 'Descrição não encontrada'
    
    keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
    keywords = keywords_tag['content'] if keywords_tag else 'Palavras-chave não encontradas'
    
    author_tag = soup.find('meta', attrs={'name': 'author'})
    author = author_tag['content'] if author_tag else 'Autor não encontrado'

    print(f'Título do site: {title}')
    print(f'Descrição: {description}')
    print(f'Palavras-chave: {keywords}')
    print(f'Autor: {author}')
else:
    print(f'Erro ao acessar a página: {response.status_code}')
