from config import CONFIG
import cloudscraper
from bs4 import BeautifulSoup

def getPlayerById(_id):
    url = f'{CONFIG.BASE}/{CONFIG.PLAYERS}/{_id}/_'
    scrapper = cloudscraper.create_scraper()
    response = scrapper.get(url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    mainTable = soup.find('div', {'class': 'playerSummaryStatBox'})

    if mainTable == None:
        raise "There is no available player"
    
    imageBlock = mainTable.find('div', {'class': 'summaryBodyshotContainer'})
    if imageBlock.find('img', {'class': 'summaryBodyshot'}) != None:
        image = imageBlock.find('img', {'class': 'summaryBodyshot'})['src']
    else: 
        image = None
    mainTableContent = mainTable.find('div', {'class': 'summaryBreakdownContainer'})
    nickname = mainTableContent.find('h1', {'class': 'summaryNickname'}).text.strip()
    name = mainTableContent.find('div', {'class': 'summaryRealname'}).text.strip()
    teamName = mainTableContent.find('div', {'class': 'SummaryTeamname'}).text.strip()
    if teamName != 'No team':
        teamId = int(
            mainTableContent.find('div', {'class': 'SummaryTeamname'}).find('a')['href'].split('/')[3]
        )
    else:
        teamId = None
    age = int(
        mainTableContent.find('div', {'class': 'summaryPlayerAge'}).text.strip().split()[0]
    )

    statRow = mainTableContent.find_all('div', {'class': 'summaryStatBreakdownRow'})
    statRow1 = statRow[0].find_all('div', {'class': 'summaryStatBreakdownDataValue'})
    rating = float( statRow1[0].text )
    dpr = float( statRow1[1].text )
    kast = float( statRow1[2].text.replace('%', '') )
    statRow2 = statRow[1].find_all('div', {'class': 'summaryStatBreakdownDataValue'})
    impact = float( statRow2[0].text )
    adr = float( statRow2[1].text )
    kpr = float( statRow2[2].text )
    additionalStats = soup.find('div', {'class': 'statistics'}).find('div', {'class': 'columns'}).find_all('div', {'class': 'col'})

    headshots =  float( additionalStats[0].find_all('div', {'class': 'stats-row'})[1].find_all('span')[1].text.replace('%', '') )
    maps = int( additionalStats[0].find_all('div', {'class': 'stats-row'})[6].find_all('span')[1].text )

    return [
        id,
        teamId,
        teamName,
        image,
        nickname,
        name,
        age,
        rating,
        impact,
        dpr,
        adr,
        kast,
        kpr,
        headshots,
        maps
    ]