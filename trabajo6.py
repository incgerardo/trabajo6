from bs4 import BeautifulSoup
import requests

def spider(id):
    url=f"https://hauslondon.com/collections/all-furniture?page={id}"	#nombre de la pagina

    r=requests.get(url)		#pido la pagina r es un objeto

    print(r.status_code)

    soup = BeautifulSoup(r.content,"html.parser")		#transforma el html en un árbol de objetos

    title = soup.find_all(class_="h4")

    print(len(title))

    for i in range(len(title)):
        print(title[i].text.lstrip().rstrip())
i=1

for i in range(12):
    spider(i)