from config import CONFIG
import cloudscraper
from bs4 import BeautifulSoup


def getTopPlayers(number_of_players):
    url = f'{CONFIG.BASE}/{CONFIG.PLAYERS}/'
    scrapper = cloudscraper.create_scraper()
    response = scrapper.get(url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    mainTable = soup.find_all('tbody')[0]
    td = mainTable.find_all('td', {'class': 'playerCol'})
    players = []
    for i in range(0, min(number_of_players, len(td))):
        link = td[i].find('a')
        name = link.text
        id = int(link['href'].split('/')[3])
        players.append((name, id))
    return players