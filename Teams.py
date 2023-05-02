from typing import List

class Player:
    def __init__(self, fullname: str, image: str, nickname: str, country_name: str, country_flag: str):
        self.fullname = fullname
        self.image = image
        self.nickname = nickname
        self.country = {
            'name': country_name,
            'flag': country_flag
        }

class Team:
    def __init__(self, id: int, ranking: int, name: str, logo: str, players: List[Player]):
        self.id = id
        self.ranking = ranking
        self.name = name
        self.logo = logo
        self.players = players

async def getTopTeams() -> List[Team]:
    # implementation of getTopTeams function
    pass
