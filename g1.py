import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []


# Pega o conteudo da requisicao do site
response = requests.get('https://g1.globo.com/') 

content = response.content

# Converter o conteudo do Html do site para BS
site = BeautifulSoup(content, 'html.parser')

# Html da noticia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})
# print(noticias)

# Pegando todas as noticias ao msm tempo
for noticia in noticias:    

    # Titulo
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    # Pegue somente o texto
    # print(titulo.text)
    # print(titulo['href']) # link da noticia
    #print(noticia.prettify())


    # Pegando o subtitulo
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-metadata'})
    #if(subtitulo):
    #    print(subtitulo.text)

    if(subtitulo):
        #print(subtitulo.text)
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])


#print(lista_noticias) 

news = pd.DataFrame(lista_noticias, columns=['Título','Subtítulo','Link'])
# salva o arquivo
news.to_csv('noticias.xlsx', index=False) 
# print(news)