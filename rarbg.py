import requests,bs4

result = requests.get("https://rarbgproxied.org/torrents.php?order=leechers&by=DESC")

soup = bs4.BeautifulSoup(result.text,"lxml")

print(soup)