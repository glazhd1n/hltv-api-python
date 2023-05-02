from typing import List, Optional

class Player:
    def __init__(self, fullname: str, image: str, nickname: str, country: Optional[str] = None):
        self.fullname = fullname
        self.image = image
        self.nickname = nickname
        self.country = country

class Team:
    def __init__(self, id: int, name: str, logo: str, players: List[Player], coach: str, ranking: int, averagePlayerAge: float):
        self.id = id
        self.name = name
        self.logo = logo
        self.players = players
        self.coach = coach
        self.ranking = ranking
        self.averagePlayerAge = averagePlayerAge

async def getTeamById(id: int) -> Team:
    pass
