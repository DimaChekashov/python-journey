import requests
from bs4 import BeautifulSoup

def parser(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        titles = soup.find_all('h1')
        links = soup.find_all('a', href=True)
    
        return {
            "titles": titles,
            "links": links
        }
    else:
        print(f'Error:: {response.status_code}')
        
def print_all(titles, links):
    for title in titles:
        print(f'Title: {title.text.strip()}')
    for link in links:
        print(f'Link: {link["href"]} - Text: {link.text.strip()}')
        
def save_into_file(titles, links, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(f'Title: {title.text.strip()}')
            file.writelines('\n')
        for link in links:
            file.write(f'Link: {link["href"]} - Text: {link.text.strip()}')
            file.writelines('\n')
    
        
titles_and_links = parser('https://python-academy.org/ru/guide/files')

print_all(titles_and_links['titles'], titles_and_links['links'])

save_into_file(titles_and_links['titles'], titles_and_links['links'], 'output.txt')