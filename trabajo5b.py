from bs4 import BeautifulSoup
import requests

url="https://www.flex.scoopforwork.com/explore?page=1"	#nombre de la pagina

r=requests.get(url)		#pido la pagina r es un objeto

print(r.status_code)

soup = BeautifulSoup(r.content,"html5lib")		#transforma el html en un árbol de objetos

title = soup.find_all(class_="text-xl")

print(len(title))

for t in title:
    print(t.text)